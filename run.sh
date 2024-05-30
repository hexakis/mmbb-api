git pull
sudo docker build -t caddyproxy ./caddy
sudo docker build -t mmb ./api
sudo docker build -t postgres-prod ./api
sudo docker compose up -d --force-recreate --renew-anon-volumes