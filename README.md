# Dornawing Django API

## Installation
  - git clone git@github.com:097karimi/dornawing-django-api.git

First install docker 
  - https://docs.docker.com/engine/install/ubuntu/

Second 
  - docker build .

Third
  - docker-compose up 


===========================================================================================<br>
- docker-compose up -d or  docker-compose up -detach -> run in background
- docker-compose logs  - > see logs

In order to install packages u need to use this command to install it and then rebuild the image
- docker-compose exec web pipenv install psycopg2-binary==2.8.5

rebuild the image -> docker-compose up -d --build

In order to run sth like $ python manage.py createsuperuser
  - $ docker-compose exec web python manage.py createsuperuser
  
 - docker-compose down -> Stop the container and release the memmory
