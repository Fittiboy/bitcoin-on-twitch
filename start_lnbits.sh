#!/bin/sh
cd lnbits
./venv/bin/hypercorn -k trio --bind 0.0.0.0:5000 'lnbits.app:create_app()' & disown
cd ..
