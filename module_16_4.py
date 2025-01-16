from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users", response_model=List[User])
async def get_all_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}", response_model=User)
async def create_user(
        username: Annotated[str, Path(min_length=3, max_length=15, description='Enter username')],
        age: Annotated[int, Path(ge=14, le=100, description='Enter age')]) -> User:
    user_id = max((i.id for i in users), default=0) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
        user_id: Annotated[int, Path(min_length=1, max_length=15, description='Enter user_id')],
        username: Annotated[str, Path(min_length=3, max_length=15, description='Enter username')],
        age: Annotated[int, Path(ge=14, le=100, description='Enter age')]) -> User:
    for i in users:
        if i.id == user_id:
            i.username = username
            i.age = age
            return i
    else:
        raise HTTPException(status_code=404, detail='Пользователя не существует')

@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int) -> str:
    for k, i in enumerate(users):
        if i.id == user_id:
            return users.pop(k)
    else:
        raise HTTPException(status_code=404, detail='Пользователя не существует')
