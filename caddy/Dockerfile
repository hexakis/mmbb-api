FROM caddy/caddy:2.7.6-alpine

RUN mkdir /caddy

COPY start.sh /caddy/start.sh
COPY cert.crt /caddy/cert.crt
COPY priv.key /caddy/priv.key

COPY Caddyfile /etc/caddy/Caddyfile

EXPOSE 443 80

CMD ["sh", "/caddy/start.sh"]
