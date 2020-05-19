#!/bin/bash
echo "========Installing python3-venv dependence ...========"
apt-get -y install  python3-venv
echo "========Seting up python-plugins-test vitural environment ...========"
python3 -m venv ~/venvs/python-plugins-test
source ~/venvs/python-plugins-test/bin/activate
echo "========Installing setuptools dependence ...========"
pip3 install --upgrade pip setuptools wheel

echo "========Entering plugin-gitee directory...========"
cd plugin-gitee
echo "========Packaging plugin-gitee...========"
python3 setup.py develop

echo "========Entering plugin-gitlab directory...========"
cd ../plugin-gitlab
echo "========Packaging plugin-gitlab...========"
python3 setup.py develop

echo "========Entering plugin directory...========"
cd ../plugin
echo "========Packaging plugin...========"
python3 setup.py develop

echo "========Running test...========"
cd ..
python3 test.py