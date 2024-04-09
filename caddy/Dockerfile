FROM caddy/caddy:2.7.6-alpine

RUN mkdir /app

COPY start.sh /app/start.sh

COPY Caddyfile /etc/caddy/Caddyfile

ENV PROXY_BACKEND=api
ENV PROXY_PORT=8000
ENV DOMAIN="marinemoneybanking.works"

EXPOSE 443 80

CMD ["sh", "/app/start.sh"]
