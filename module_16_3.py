from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=3, max_length=15, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=14, le=100, description='Enter age', example='18')]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[str, Path(min_length=1, max_length=15, description='Enter user_id', example='1')],
        username: Annotated[str, Path(min_length=3, max_length=15, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=14, le=100, description='Enter age', example='18')]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[str, Path(min_length=1, max_length=15, description='Enter user_id', example='1')]) -> str:
    users.pop(user_id)
    return f"User {user_id} has deleted."