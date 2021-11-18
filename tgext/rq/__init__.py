from tg import config
from tg import hooks
from tg.configuration import milestones

import logging
log = logging.getLogger('tgext.rq')


# This is the entry point of your extension, will be called
# both when the user plugs the extension manually or through tgext.pluggable
# What you write here has the same effect as writing it into app_cfg.py
# So it is possible to plug other extensions you depend on.
def plugme(configurator, options=None):
    if options is None:
        options = {}

    log.info('Setting up tgext.rq extension...')
    milestones.config_ready.register(SetupExtension(configurator))

    # This is required to be compatible with the
    # tgext.pluggable interface
    return dict(appid='tgext.rq')


# Most of your extension initialization should probably happen here,
# where it's granted that .ini configuration file has already been loaded
# in tg.config but you can still register hooks or other milestones.
class SetupExtension(object):
    def __init__(self, configurator):
        self.configurator = configurator

    def __call__(self):
        pass

    def on_startup(self):
        log.info('+ Application Running!')



