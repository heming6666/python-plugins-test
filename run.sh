#!/bin/bash
echo "======================Seting up python-plugins-test vitural environment ...======================"
apt-get -y install  python3-venv
python3 -m venv ~/venvs/python-plugins-test
source ~/venvs/python-plugins-test/bin/activate
pip3 install --upgrade pip setuptools wheel

echo "======================Packaging plugin-gitee ...======================"
cd plugin-gitee
python3 setup.py develop

echo "======================Packaging plugin-gitlab...======================"
cd ../plugin-gitlab
python3 setup.py develop

echo "======================Packaging core...======================"
cd ../core
python3 setup.py develop

echo "======================Running test...======================"
cd ..
python3 test.py