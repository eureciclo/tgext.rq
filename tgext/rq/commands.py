from __future__ import absolute_import
import importlib
from os import getcwd

from gearbox.command import Command
from paste.deploy import loadapp

from tg import config

class RQCommand(Command):
    def get_description(self):
        return "Starts RQ in turbogears"

    def get_parser(self, prog_name):
        parser = super(RQCommand, self).get_parser(prog_name)

        parser.add_argument("-c", "--config",
                            help='application config file to read (default: development.ini)',
                            dest='config_file', default="development.ini")
        return parser

    def take_action(self, opts):
        from tgext.rq.redis_config import RedisConfig
        from rq import Connection, Worker

        config_file = opts.config_file
        config_name = 'config:%s' % config_file
        here_dir = getcwd()

        # Load the wsgi app first so that everything is initialized right
        loadapp(config_name, relative_to=here_dir)

        module_path = config.get('tgext.rq.application_queues_module')
        function_name = config.get('tgext.rq.application_queues_function')
        if module_path is None or function_name is None:
            raise Exception("""tgext.rq.application_queues_module and/or """
                """tgext.rq.application_queues_function configs are not set.\n"""
                """Please read README.md / Configuration / Queues""")
        module = importlib.import_module(module_path)
        application_queues = getattr(module, function_name)

        redis = RedisConfig().client()
        with Connection(redis):
            queues = application_queues()

            w = Worker(queues)
            w.work()
