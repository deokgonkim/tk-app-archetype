#!/bin/bash

if [ "b$1" == "b" ]; then
    echo Please specify file name. ex. ./subst.sh tkapp.pot
    exit 1
fi

INPUT=$1
INT_I=/tmp/tkapp_temp_i.txt
INT_O=/tmp/tkapp_temp_o.txt

cp $INPUT $INT_I

while IFS='=' read -r SUB VALUE
do 
    echo Replacing $SUB =\> $VALUE
    cat $INT_I | sed s/"$SUB"/"$VALUE"/g > $INT_O
    cp $INT_O $INT_I
    echo ======================================================================
done < subst_header.txt

cp $INT_O $INPUT

