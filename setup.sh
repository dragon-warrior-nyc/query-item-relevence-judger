#!/usr/bin/env bash
 
VIRTUALENV_HOME=~/virtualenv
mkdir -p ${VIRTUALENV_HOME}
VENV_HOME=${VIRTUALENV_HOME}/google-adk
 
rm -rf ${VENV_HOME}  # remove any previous virtualenv with this name

python3.10 -m venv ${VENV_HOME} #installed at ~/develop/virtualenv/google-adk
# virtualenv -p python3 ${VENV_HOME} 
 
source $VENV_HOME/bin/activate #activate the env
# source /Users/mum0018/virtualenv/google-adk/bin/activate
pip install -r requirements.txt