#!/bin/sh
# This is a slightly modified version of the install instructions at https://lnbits.org/guide/installation.html
git clone https://github.com/lnbits/lnbits.git
cd lnbits/
# going with latest commit for now
# This is a commit I know to be working correctly
# git checkout "83137ba0a0cc541608482cc43182e26009f63814"
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
cp .env.example .env
mkdir data
./venv/bin/quart assets
./venv/bin/quart migrate
# Run this to catch potential issues in stdout
./venv/bin/hypercorn -k trio --bind 0.0.0.0:5000 'lnbits.app:create_app()'
