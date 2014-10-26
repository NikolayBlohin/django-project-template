#!/usr/bin/env bash

./scripts/make_environment.sh

source ./env/bin/activate

./scripts/install_python_requirements.sh

#cp ./src/project/local_settings.py.development ./src/project/local_settings.py

#mkdir ./data/ && ./scripts/sync_db.sh
