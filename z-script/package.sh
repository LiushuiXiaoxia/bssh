#!/bin/bash

set -x
export QT_MAC_WANTS_LAYER=1

source venv/bin/activate

pip install PyInstaller

APP_NAME=bssh

# pyinstaller main.py --noconsole --hidden-import PySide2.QtXml --icon="logo.ico"
pyinstaller main.py --name "$APP_NAME" --noconsole --windowed \
      --osx-bundle-identifier cn.mycommons.bssh \
      --hidden-import PySide2.QtXml
