#!/bin/bash
apt-get -y install  python3-venv
python3 -m venv ~/venvs/python-plugins-test
source ~/venvs/python-plugins-test/bin/activate
pip3 install --upgrade pip setuptools wheel

cd plugin-gitee
python3 setup.py develop

cd ../plugin-gitlab
python3 setup.py develop

cd ../plugin
python3 setup.py develop

cd ..
python3 test.py