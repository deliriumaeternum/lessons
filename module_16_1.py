from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> str:
    return {"Главная страница"}

@app.get("/user/admin")
async def admin() -> str:
    return {"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_num(user_id: int) -> str:
    return {f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def user_info(username: str, age: int) -> str:
    return {f"Информация о пользователе: имя - {username}, возраст - {age}"}
