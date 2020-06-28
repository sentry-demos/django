# Must have `sentry-cli` installed globally
# Require SENTRY_AUTH_TOKEN environment variable
#  SENTRY_AUTH_TOKEN=<your_auth_token>

SENTRY_ORG=testorg-az
SENTRY_PROJECT=django-lr
VERSION=`sentry-cli releases propose-version`
REPO=sentry-demos/django

deploy: install create_release associate_commits run_django

install:
	pip install -r ./requirements.txt

create_release:
	sentry-cli releases -o $(SENTRY_ORG) new -p $(SENTRY_PROJECT) $(VERSION)

associate_commits:
	sentry-cli releases -o $(SENTRY_ORG) -p $(SENTRY_PROJECT) \
		set-commits $(VERSION) --commit "$(REPO)@$(VERSION)"

run_django:
	VERSION=$(VERSION) python manage.py runserver
