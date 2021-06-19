#!/bin/sh
git clone https://github.com/lnbits/lnbits.git
cd lnbits/
git checkout "1e0367a451ee34f380ce8ad22395690b3826a0c8"
# ensure you have virtualenv installed, on debian/ubuntu 'apt install python3-venv' should work
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
cp .env.example .env
mkdir data
./venv/bin/quart assets
./venv/bin/quart migrate
./venv/bin/hypercorn -k trio --bind 0.0.0.0:5000 'lnbits.app:create_app()'
