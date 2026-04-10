echo Seeding data into the web application database. Please wait...
sleep 0.75
docker compose exec -T api python manage.py shell < add_data.py
sleep 0.5
echo Data seeding complete.
sleep 0.75