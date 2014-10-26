#!/usr/bin/env bash

./scripts/make_environment.sh

source ./env/bin/activate

./scripts/install_python_requirements.sh

cp ./src/project/project/local_settings.py.development ./src/project/project/local_settings.py
