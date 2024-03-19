#!/bin/bash

set -e

if [ -z "$DOMAIN" ]
then
    export DOMAIN="marinemoneybanking.works"
fi

caddy run --config /etc/caddy/Caddyfile --adapter caddyfile