#!/bin/bash

echo Removing '*.pyc' files
find . -name '*.pyc' -exec rm {} \;
