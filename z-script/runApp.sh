#!/bin/bash

set -x

d="Darwin"
l="Linux"

os=$(uname)

if [[ $os =~ $d ]];then
    open dist/bssh.app
elif [[ $os =~ $l ]];then
    ./dist/bssh/bssh
else
    echo "can not run bssh on $os"
fi
