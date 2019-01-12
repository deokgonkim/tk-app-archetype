#!/bin/bash

# remove build directory
python setup.py clean -a

# remove MANIFEST
echo 'Removing file MANIFEST (for source distribution)'
if [ -f MANIFEST ]; then
   rm MANIFEST
fi

# remove dist files
if [ -d dist ]; then
    rm -Rf dist
fi

# remove .pyc files
echo Removing '*.pyc' files
find . -name '*.pyc' -exec rm {} \;

# remove .mo files
echo Removing '*.mo' files
find locale -name '*.mo' -exec rm {} \;
