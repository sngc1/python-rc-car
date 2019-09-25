#!/usr/bin/env bash

set -e

BASE_DIR=$(dirname $0)
PYTHON_MAIN_DIR="rccar"

cd ${BASE_DIR}/../

pipenv run python ${PYTHON_MAIN_DIR}/main.py $@
