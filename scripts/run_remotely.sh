#!/usr/bin/env bash

set -ue

PROJECT="python-rc-car"

BASE_DIR=$(dirname $0)
TARGET_HOST=$1
ARGS=""
if [[ $# -gt 1 ]]; then
    ARGS=${@:2:($#-1)}
fi

RSYNC="rsync -vaz --delete --exclude pipfile_lock.md5sum \
--exclude .git --exclude-from ${BASE_DIR}/../.gitignore \
-e \"ssh \" ${BASE_DIR}/../. pi@${TARGET_HOST}:/home/pi/${PROJECT}"
set -x
bash -c "$RSYNC"

SSH="ssh -t pi@${TARGET_HOST}"
${SSH} "/home/pi/${PROJECT}/scripts/run_car.sh ${ARGS}"
