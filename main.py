from fastapi import FastAPI
from schema import Author as SchemaAuthor
from models import Author as ModelAuthor

from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv
import os

load_dotenv(".env")

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/")
def main_page():
    return {"message": "success"}


@app.post("/add-author/", response_model=SchemaAuthor)
def add_author(author: SchemaAuthor):
    db_author = ModelAuthor(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author
