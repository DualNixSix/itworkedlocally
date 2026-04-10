echo Starting the dockerized web application. Please wait...
sleep 0.75
docker compose up -d
sleep 3
docker ps
sleep 0.5
echo Start complete. Please proceed to http://127.0.0.1:81 or http://localhost:81 to confirm.
sleep 0.75