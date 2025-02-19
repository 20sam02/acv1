from fastapi import FastAPI
from routes.user import user

main = FastAPI()

main.include_router(user)
