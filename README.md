# README

# covid-api app for CROPY さん

# For build project

1. go to right path
2. docker-compose build

# For start project

- docker-compose up

# For creating new app use

- docker-compose run --rm app sh -c "python manage.py startapp [app_name]"

# For migration

- docker-compose run --rm app sh -c "python manage.py makemigrations"
