import os
from tg import config
from redis import Redis

class RedisConfig:
    def url(self):
        redis_url = config.get('redis.url', os.getenv('REDIS_URL'))

        if redis_url == None:
            raise Exception("""redis.url config or REDIS_URL env var not set."""
                """Redis cannot be found.""")
        return redis_url

    def client(self):
        redis_url = self.url()
        return Redis.from_url(redis_url)

    def rq_queue(self, name):
        from rq import Queue as RqQueue
        default_timeout = config.get('tgext.rq.default_job_timeout', 180)
        return RqQueue(name, connection=self.client(), default_timeout = default_timeout)
