## Table of Contents
- [Installing Dependencies](#installing-dependencies)
- [Configuring Sentry](#configuring-sentry)
- [Running The Demo](#running-the-demo)
- [Cleaning Up](#cleaning-up)

## Installing Dependencies

1. Install the Raven library:
`npm install -g @sentry/cli`

2. Install sentry-python:
`pip install --upgrade sentry-sdk`

3. Include `sentry-sdk` in [`requirements.txt`](https://github.com/sentry-demos/django/blob/master/requirements.txt#L2). Verfiy that the version is accurate:
`pip show sentry-sdk | grep Version`

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

This demo includes two scripts: one to create a virtual environment and install packages and the other to start the web frontend.

### Setup Script

Run the set up script (`setup.sh`) in this directory:
`./setup.sh`


You can also set up by running the following commands:
```
virtualenv django_example              # create a new virtual environment
. django_example/bin/activate          # and use it
pip install -r ./requirements.txt      # install python packages
```

### Starting The Web Frontend

To start Django's development server (`runserver`) on the local machine, run the `web.sh` script from within this directory:
`./web.sh`

Go to http://127.0.0.1:8000/ to see the demo page.


## Cleaning Up

Pressing Ctrl-C once in each terminal window should stop Django's development server.

`rm -r django_example` will delete the virtualenv directory containing all the installed Python packages.

## About This Demo

This demo provides a basic example of instrumenting [a Django project with Sentry](https://docs.sentry.io/clients/python/integrations/django/). To play with this demo, you'll need to create a Sentry account, and [update the project configuration](#configuring-sentry) with your DSN.

The code for this demo is split up in a similar manner to the Django tutorial and most of the code was generated from `django-admin startproject` and `python manage.py startapp`. It includes a single "project", `myproject`, and a single "app", `myapp`. `myproject` contains the settings and global URL routing, and `myapp` contains views, templates, and static files.

## Contributing

To keep the demo light, many key Django features were commented out of the generated code. In particular, no ORM models are defined so there is no need to create or apply migrations. (A sqlite database file may get generated but it's safe to delete.)

> Note: This demo uses Django 1.11 which is a "long-term support" (LTS) release but not the latest version. This was selected on the assumption that existing applications might not have upgraded yet. The procedure for integrating Raven/Sentry with Django 2.0+ should be very similar.

Sentry is open source! Want to get started contributing to Sentry? Our [internal documentation](https://docs.sentry.io/internal/) has you covered.

## Anything Else?

[Docs](https://docs.sentry.io), [Tweet](https://twitter.com/getsentry), [email](hello@sentry.io), or visit our [forum](https://forum.sentry.io)!
