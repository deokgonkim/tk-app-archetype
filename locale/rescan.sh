#!/bin/bash

# On MacOS, there is no pygettext.py
# so, the file is copied from source distribution
PYGETTEXT=../tools/i18n/pygettext.py

if [ "b$1" == "b" ]; then
    echo Please specify program name. ex. ./rescan.sh tkapp
    exit 1
fi

DOMAIN=$1

$PYGETTEXT -d ${DOMAIN} -o ./${DOMAIN}.pot ../src

