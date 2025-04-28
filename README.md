# Setup Local Testing
Prerequisites: Docker & docker-compose already installed

1. Clone the github repo `git clone git@github.com:samuelmjn/dtpl-manud-jaya.git`
2. cd dtpl-manud-jaya
3. Run `docker-compose build && docker-compose up -d`

## Create Admin user
1. Enter the container, `docker exec -it container_id /bin/bash`
2. Run `python manage.py createsuperuser`
3. Finish the user creation wizard