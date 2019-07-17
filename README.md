## Table of Contents
- [Installing Dependencies](#installing-dependencies)
- [Configuring Sentry](#configuring-sentry)
- [Running The Demo](#running-the-demo)
- [Cleaning Up](#cleaning-up)

## Installing Dependencies
This project uses Django 2.2 that requires Python 3

1. Install Python 3:
`brew install python3`

2. Install Sentry's command line tool to use release tracking and Github integration for commit data:
`npm install -g @sentry/cli`

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

This demo includes two scripts: one to create a virtual environment (`django_demo_venv`) and install packages and the other to start the web frontend.

### Setup Script

Run the set up script (`setup.sh`) in this directory:
`./setup.sh`


You can also set up by running the following commands:
```
virtualenv django_demo_venv              # create a new virtual environment
. django_demo_venv/bin/activate          # and use it
pip install -r ./requirements.txt      # install python packages
```

### Creating a Release & Starting the Server

To start Django's development server (`runserver`) on the local machine, run the `web.sh` script from within this directory:
`./web.sh`


### Demo Script

This demo uses Django's rest-framework package and offers 3 API endpoints:
1. http://localhost:8000/handled - generates a runtime error excplicitly reported to Sentry though the SDk's captureException
2. http://localhost:8000/unhandled - generates an unhandled runtime error reported 
3. http://localhost:8000/checkout - can be used with the [Sentry REACT demo store front demo](https://github.com/sentry-demos/react)
    This endpoint can also be used with directly through the Django REST Framework web UI. To generate an error paste the following JSON payload in the POST payload text area:


```
    {
    "cart": [
        {"id": "wrench", "name": "Wrench", "price": 500, "img": "/static/media/wrench.0371ec11.png"},
        {"id": "wrench", "name": "Wrench", "price": 500, "img": "/static/media/wrench.0371ec11.png"}
    ],
    "email": "0s5r@yahoo.com"
    }

```



![Alt Text](django_demo_setup.gif)


## Cleaning Up

Pressing Ctrl-C once in each terminal window should stop Django's development server.

`rm -r django_demo_venv` will delete the virtualenv directory containing all the installed Python packages.