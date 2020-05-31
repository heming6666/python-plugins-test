#!/bin/bash
echo "======================Seting up python-plugins-test vitural environment ...======================"
apt-get -y install  python3-venv
python3 -m venv ~/venvs/python-plugins-test
source ~/venvs/python-plugins-test/bin/activate
pip3 install --upgrade pip setuptools wheel

echo "======================Packaging grimoirelab-elk-gitee ...======================"
cd grimoirelab-elk-gitee
python3 setup.py develop

echo "======================Packaging grimoirelab-elk...======================"
cd ../grimoirelab-elk
python3 setup.py develop

echo "======================Running test...======================"
cd ..
python3 test.py
