## Table of Contents
- [Installing Dependencies](#installing-dependencies)
- [Configuring Sentry](#configuring-sentry)
- [Running The Demo](#running-the-demo)
- [Cleaning Up](#cleaning-up)

## Installing Dependencies
This project uses Django 2.2 that requires Python 3

1. Install Python 3:
```
brew install python3
```

2. Install `virtualenv` and `virtualenvwrapper`
```
pip3 install virtualenv virtualenvwrapper
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
exec bash
```

3. Install Sentry's command line tool to use release tracking and Github integration for commit data:
```
npm install -g @sentry/cli
```

This demo uses npm, pip, and virtualenv.

## Configuring Sentry

The Sentry client library requires a [DSN generated from Sentry](https://docs.sentry.io/quickstart/#configure-the-dsn) which  specifies the project events will be sent to. Add the import and configuration code to `settings.py`:

 ```
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://yourdsn@sentry.io/1234567"
)
```

Further details on configuring Sentry [here](https://docs.sentry.io/platforms/python/django/).

## Running The Demo

Create a python-3 virtualenv (see below) and run `deploy` target in `Makefile`.

### Virtualenv setup

Setup and activate a Python 3 virtual environment in the project root:
```
mkvirtualenv --python=python3 sentry-demo-django
```

To use virtualenv:
```
workon sentry-demo-django
```


### Runing Django

Running the following command will install relevant python libraries and run django server
```
make deploy
```


### Demo Specs

This demo uses Django's rest-framework package and offers 3 API endpoints:
1. http://localhost:8000/handled - generates a runtime error excplicitly reported to Sentry though the SDk's captureException
2. http://localhost:8000/unhandled - generates an unhandled runtime error reported
3. http://localhost:8000/checkout - can be used with the [Sentry REACT demo store front demo](https://github.com/sentry-demos/react)
    This endpoint can also be used with directly through the Django REST Framework web UI. To generate an error paste the following JSON payload in the POST payload text area:


```
    {
    "cart": [
        {"id": "wrench", "name": "Wrench", "price": 500},
        {"id": "wrench", "name": "Wrench", "price": 500}
    ],
    "email": "user@email.com"
    }
```

![Alt Text](django_demo_setup.gif)

## Cleaning Up

Pressing Ctrl-C once in each terminal window should stop Django's development server.

To deactivate the virtualenv sentry-demo-django:
```
deactivate
```

To remove the virtualenv: 
```
rmvirtualenv sentry-demo-django
```
