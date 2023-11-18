## How to run this project ?

### Frist time:
Step 0: Clone this repo and create venv, I have used python 3.11
Step 1: create new `.env` file with following keys:(replace values accordingly)
    DB_USER=postgres
    DB_PASSWORD=password
    DB_NAME=book_db
    PGADMIN_EMAIL=admin@admin.com
    PGADMIN_PASSWORD=password
    DATABASE_URL=postgresql+psycopg2://postgres:password@db:5432/book_db

Step 2: run this command `alembic init alembic`

Step 3: run these docker-compose commands:
'''
>  docker-compose up --build
>  docker-compose run app alembic revision --autogenerate -m "New Migration"
>  docker-compose run app alembic upgrade head
'''

## What am i trying to acheive here ? 
Build a FastAPI based backend for a bookshop application, allowing to create and maintain inventory of books and related entities. 

## what can i learn from this project ? 
I have used various modern tools such as FastAPI, Docker, docker-compose, sqlalchemy, fastapi-sqlalchemy, alembic, pydantic. You can learn how all this fit together in a application. 

## What is the database schema used here ? 
This is evolving project, Currently there is:
1. Author
2. Books 

## what is the scope of this project ?
To be able to support day-to-day operations of a bookshop.

## Is there any UI for this backend ? 
Currently No, feel free to use this API to create Frontend

