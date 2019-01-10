#!/bin/bash

# On MacOS, there is no pygettext.py
# so, the file is copied from source distribution
MSGFMT=../../../tools/i18n/msgfmt.py

if [ "b$2" == "b" ]; then
    echo Please specify program name and locale. ex. ./rescan.sh tkapp ko
    exit 1
fi

DOMAIN=$1
LOCALE=$2

cd ${LOCALE}/LC_MESSAGES

$MSGFMT ${DOMAIN}

