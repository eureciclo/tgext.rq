tgext.rq
========

tgext.rq is a TurboGears2 extension that simplify rq usage for async jobs.

TLDR
----

Install

```
pip install tgext.rq #or
install_requires = [
    "TurboGears2 >= 2.4.3",
    "rq",
    ...,
    "tgext.rq"
```

Plug into TurboGears:

```
#config/app_cfg.py

import tgext.rq
tgext.rq.plugme(base_config)
```

Add configs:

```
#development.ini

redis.url = redis://127.0.0.1:6379/0
tgext.rq.application_queues_module = app.workers.queue
tgext.rq.application_queues_function = application_queues
```

Provide a method so tgext.rq know all queues that your application uses:

```
#app.workers.queue.py

def application_queues():
  return ['high_priority', 'default_priority', 'low_priority']
```

Run worker:

```
gearbox rq
```

Installing
----------

Add tgext.rq to your `setup.cfg`, inside `install_requires`, something like:

```
install_requires = [
    "TurboGears2 >= 2.4.3",
    "rq",
    ...,
    "tgext.rq"
```

or install via pypi:

```
pip install tgext.rq
```

Enabling
--------

To enable tgext.rq put inside your application
`config/app_cfg.py` the following:

```
#config/app_cfg.py

import tgext.rq
tgext.rq.plugme(base_config)
```

Configuration
-------------

All configurations listed here should be done on tg .ini files, like
`development.ini` or `production.ini`

### Redis URL

```
#development.ini

redis.url = redis://USERNAME:PASSWORD@IP.ADDRESS.0.1:6379/DATABASE_NUMBER
redis.url = redis://user:test@127.0.0.1:6379/0
redis.url = redis://127.0.0.1:6379/0
redis.url = redis://redis/0 #If you use docker-compose to up redis
```

This config is required.

### Queues

tgext.rq needs to know what queues it should listen and your application have to
supply a module and function to do that. For example:

Imagine that your application have the following module: `app.workers.queue.py`:

```
#app.workers.queue.py

def application_queues():
  return ['high_priority', 'default_priority', 'low_priority']
```

You need to set these configs:

```
#development.ini

tgext.rq.application_queues_module = app.workers.queue
tgext.rq.application_queues_function = application_queues
```

ps: For now, only modules are supported. No classes.

This config is required.

### Optional configs

```
#development.ini

tgext.rq.default_job_timeout = 180 #default value is 180.
```

Run RQ
------

tgext.rq provides a tg command to run a rq worker:

```
gearbox rq -c production.ini
```

or using the default development.ini file:

```
gearbox rq
```

Multithreding with Gevent
-------------------------

tgext.rq comes with a Gevent worker to enable more concurrency on job execution,
to enable:

```
#development.ini

tgext.rq.worker_class = GeventWorker #default value is: Worker
tgext.rq.gevent_pool_size = 3 #default value is: 20
```

If you receive any errors related to gevent patches, like:

```
super(SSLContext, SSLContext).options.__set__(self, value) [Previous line repeated 473 more times] RecursionError: maximum recursion depth exceeded
```

You need to patch manually your application before it loads, add these lines
before everything else on `app_cfg.py`

```
from gevent import monkey
monkey.patch_all()
```

Contributions
-------------

Future Needs:

* tests
* more rq config options
* [add your needs here]

PRs are welcome!

How to upload to Pip
--------------------

```
python setup.py sdist
pip install twine
twine upload dist/*
```