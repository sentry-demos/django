#!/usr/bin/env bash

if [ -f .setup_already_run ]; then
  echo "Setup has already run"
  exit 1
fi

# create empty virtual environment
virtualenv -p python3 django_demo_venv

if [ "${?}" -ne "0" ]; then
  echo "Error creating virtualenv: quitting setup"
  exit 1
fi

# activate the new virtual environment
source django_demo_venv/bin/activate

if [ "${?}" -ne "0" ]; then
  echo "Error activating virtualenv: quitting setup"
  exit 1
fi

# install python packages
pip install -r ./requirements.txt

if [ "${?}" -ne "0" ]; then
  echo "Error installing Python requirements: quitting setup"
  exit 1
fi

touch .setup_already_run
echo "Setup completed successfully"
exit 0
