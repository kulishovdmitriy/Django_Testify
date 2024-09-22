# Application Web University

### University application, allows you to automatize accounting for students, teachers

## Install app

clone repository:

    git clone https://github.com/kulishovdmitriy/Django_website_University

Create a virtual environment:

    python3 -m venv venv
    source ./venv/bin/activate

Re -check the correctness of the location python:

    which python

Set addictions from requirements.txt

    pip install -r requirements.txt

install docker:

    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt update
    sudo apt install docker-ce -y
    sudo systemctl status docker
    sudo usermod -aG docker ${USER}
    newgrp docker
    docker --version

Install docker-compose:

    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose --version

Set up environment:

    Create a file .env as described in the example .env.example and fill in your values

In file .env you can switch between prod (FOR PRODUCTION):


    RUN_MODE=

In project 2 files decker-compose `(decker-compose.dev.yml) to launch the application in development mode` and 
`(decker-compose.prod.yml) to launch the application in production mode` 

### Follow the starting command for docker-compose (dev)

    docker compose -f docker-compose.dev.yml up --build

You need to collect staticfiles:

    docker compose -f docker-compose.dev.yml exec backend_dev python manage.py collectstatic

and media:

    docker compose -f docker-compose.dev.yml exec backend_dev cp -r media/ /var/www/web_universe/media

In the container `postgres`,follow the command to create a new user.
Here `psql` - is a customer utility for PostgreSQL, and `-U postgres` indicates that you are in as a super - user Postgressql `postgres`.
Replace `your_database` and `new_user`. 

    docker compose exec postgres psql -U postgres
    
    CREATE USER new_user WITH PASSWORD 'password123'

    ALTER USER new_user CREATEDB;

    GRANT ALL PRIVILEGES ON DATABASE your_database TO new_user;

Exit `psql` from customer utility

    /q

In the container `backend_dev`, execute the command to perform migrations

    docker compose -f docker-compose.dev.yml exec backend_dev python manage.py migrate

Recreate docker-compose:

    docker compose -f docker-compose.dev.yml restart

`To use the admin panel, follow the next command in the container "backend_dev":`
(Follow the finished steps)
 
    python manage.py createsuperuser


### For `docker-compose.prod.yml` you need to make what commands

### It is possible to use the `API interface`

