echo Stopping the dockerized web application. Please wait...
sleep 0.75
docker compose down
sleep 3
docker ps
sleep 0.5
echo Stop complete. Use ./run.sh to start the web application.
sleep 0.75