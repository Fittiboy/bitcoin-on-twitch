#!/bin/sh
cd lnbits/lnbits/extensions/ngrok
mv config.json.example config.json
cd ../../..
./venv/bin/quart assets
./venv/bin/quart migrate
