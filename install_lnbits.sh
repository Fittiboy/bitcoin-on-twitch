#!/bin/sh
# This is a slightly modified version of the install instructions at https://lnbits.org/guide/installation.html
git clone https://github.com/lnbits/lnbits.git
cd lnbits/
# This is a commit I know to be working correctly
git checkout "1e0367a451ee34f380ce8ad22395690b3826a0c8"
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
cp .env.example .env
mkdir data
./venv/bin/quart assets
./venv/bin/quart migrate
# Run this to catch potential issues in stdout
./venv/bin/hypercorn -k trio --bind 0.0.0.0:5000 'lnbits.app:create_app()'
