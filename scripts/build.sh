#/bin/bash

apt update && apt upgrade -y
apt install python3-pip -y
pip install Flask