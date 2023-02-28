#!/bin/bash

source venv/bin/activate

set -x
echo "gen ui file start"

python3 z-script/gen.py ui

echo "gen ui file stop"
