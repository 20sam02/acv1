from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()

@user.get("/users")

def get_users():
        return conn.execute(users.select()).fetchall()

@user.post("/users")

def create_user(user:User):
        print(User)
        return "hello world 2"

@user.get("/users")

def helloworld():
        return "hello world 2"

@user.get("/users")

def helloworld():
        return "hello world 2"
