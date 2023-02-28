#!/bin/bash

set -x

source venv/bin/activate

python3 -m pip install --upgrade pip

pip install PyInstaller
pip install -r requirements.txt
