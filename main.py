import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import fetch_one_todo, fetch_all_todos, create_todo, update_todo, remove_todo

from model import Todo

app = FastAPI()


origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Ping": "Pong"}


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no TODO item with {title}")


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, f"Something went wrong.")


@app.put("/api/todo{title}", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(400, f"Something went wrong.")


@app.delete("/api/todo{title}")
async def delete_todo_by_title(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted item!"
    raise HTTPException(404, f"There is no TODO with title {title}.")


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
