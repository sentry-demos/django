#!/usr/bin/env bash

# start web frontend

source django_demo_venv/bin/activate

if [ "${?}" -ne "0" ]; then
  echo "Error activating virtualenv: can't start dev server"
  exit 1
fi

make deploy