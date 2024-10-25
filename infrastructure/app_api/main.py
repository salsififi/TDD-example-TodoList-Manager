"""Implémentation (partielle) avec FastAPI"""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from infrastructure.database.connexion import get_session
from infrastructure.repositories.sqlite_todo_repository import SQLiteTodoRepository
from todolist.todo_entity import Todo, TodoCreate
from todolist.todo_exceptions import TodoNotFoundError
from todolist.todo_repository_protocol import TodoRepository
from todolist.todo_usecase import CreateTodoUseCase, ToggleDoneUseCase

app = FastAPI()


def repository(db: Session = Depends(get_session)) -> TodoRepository:
    return SQLiteTodoRepository(db)


@app.get('/todos')
def get_todos(repository: TodoRepository = Depends(repository)):
    return repository.get_all()


@app.post('/todos')
def create_todo(todo: TodoCreate, repository: TodoRepository = Depends(repository)):
    create_todo_use_case = CreateTodoUseCase(repository)
    return create_todo_use_case(todo.title)


@app.put('/todos/toggle/id')
def toggle_done(id: str, repository: TodoRepository = Depends(repository)):
    toggle_done_usecase = ToggleDoneUseCase(repository)
    try:
        toggle_done_usecase(id)
    except TodoNotFoundError as e:
        return JSONResponse(
            status_code=404,
            content={"message": str(e)}
        )
