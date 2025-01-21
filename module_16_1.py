from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Главная сраница"}

@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id(user_id: int):
    return {"message": f"Вы вошли как пользователь №{user_id}"}

@app.get("/user")
async def user_paginator(username: str = 'Lada', age: int = 25):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
