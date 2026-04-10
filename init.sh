echo Initializing the dockerized web application. Please wait...
sleep 0.75
docker compose up -d
sleep 3
docker ps
sleep 2
docker compose exec api python manage.py makemigrations 
sleep 2
docker compose exec api python manage.py migrate
sleep 2
docker compose exec -T api python manage.py shell < add_data.py
sleep 2
docker compose exec api python manage.py createsuperuser
sleep 0.5
echo Initialization complete. Please proceed to http://127.0.0.1:81 or http://localhost:81 to confirm.
sleep 0.75