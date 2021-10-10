#/bin/bash

sudo apt install python3-venv python3-pip -y
python3 -m venv venv_evaluate
source venv_evaluate/bin/activate
pip install -r requirements.txt
python3 evaluate.py
deactivate