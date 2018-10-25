# Django Example for [getsentry](https://github.com/getsentry)

### Table of Contents
- [About This Demo](#about-this-demo)
- [Installing Dependencies](#installing-dependencies)
- [Configuring Sentry](#configuring-sentry)
- [Running The Demo](#running-the-demo)
- [Cleaning Up](#cleaning-up)

## About This Demo

This demo provides a basic example of instrumenting [a Django project with Sentry](https://docs.sentry.io/clients/python/integrations/django/). To play with this demo, you'll need to create a Sentry account, and [update the project configuration](#configuring-sentry) with your DSN.

The code for this demo is split up in a similar manner to the Django tutorial and most of the code was generated from `django-admin startproject` and `python manage.py startapp`. It includes a single "project", `myproject`, and a single "app", `myapp`. `myproject` contains the settings and global URL routing, and `myapp` contains views, templates, and static files.

This demo uses Python, pip, and virtualenv.

## Installing Dependencies

1. Install sentry-python
`pip install --upgrade sentry-sdk==0.5.0`

2. Make sure `sentry-sdk` is included in [`requirements.txt`](https://github.com/sentry-demos/django/blob/master/requirements.txt#L2)

These steps are abridged from the [official documentation](https://docs.sentry.io/platforms/python/django/), which is a much better reference.


## Configuring Sentry

Raven, the Sentry client library, uses a [DSN generated from Sentry](https://docs.sentry.io/quickstart/#configure-the-dsn) to collect errors and send them to the right place.

Specify the DSN as an environment variable. DSN can be found under Project Settings > Client Keys (DSN) on the Sentry dashboard.

```
export SENTRY_PRIVATE_DSN='https://<PUBLIC_DSN_KEY>:<PRIVATE_DSN_KEY>@sentry.io/<PROJECT_ID>'
```


## Running The Demo

For ease of isolating the demonstration code, it is best to use a [Python virtualenv](https://virtualenv.pypa.io/en/stable/) to contain the installed packages. Installing Python, pip, and virtualenv are outside the scope of this demo.

This demo includes two scripts: one to create a virtual environment and install packages and the other to start the web frontend.

### Setup Script

You can set up by running the following commands:

```
virtualenv django_example              # create a new virtual environment
. django_example/bin/activate          # and use it
pip install -r ./requirements.txt      # install python packages
```

Or run the set up script (`setup.sh`) in this directory:
`./setup.sh`


### Starting The Web Frontend

Run `./web.sh` from within this directory. This will start Django's development server (`runserver`) on the local machine.

Go to http://127.0.0.1:8000/ to see the demo page.


## Cleaning Up

Pressing Ctrl-C once in each terminal window should stop Django's development server.

`rm -r django_example` will delete the virtualenv directory containing all the installed Python packages.

## Contributing
To keep the demo light, many key Django features were commented out of the generated code. In particular, no ORM models are defined so there is no need to create or apply migrations. (A sqlite database file may get generated but it's safe to delete.)

> Note: This demo uses Django 1.11 which is a "long-term support" (LTS) release but not the latest version. This was selected on the assumption that existing applications might not have upgraded yet. The procedure for integrating Raven/Sentry with Django 2.0+ should be very similar.

Sentry is open source! Want to get started contributing to Sentry? Our [internal documentation](https://docs.sentry.io/internal/) has you covered.

## Anything Else?

[Docs](https://docs.sentry.io), [Tweet](https://twitter.com/getsentry), [email](hello@sentry.io), or visit our [forum](https://forum.sentry.io)!
