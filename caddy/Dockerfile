FROM caddy/caddy:2.7.6-alpine

RUN mkdir /app

COPY start.sh /app/start.sh
COPY cert.crt /app/cert.crt
COPY priv.key /app/priv.key

COPY Caddyfile /app/Caddyfile

EXPOSE 443 80

CMD ["sh", "/app/start.sh"]
