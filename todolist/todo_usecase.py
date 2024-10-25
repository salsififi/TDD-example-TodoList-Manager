from abc import ABC
from uuid import uuid4

from todolist.todo_entity import Todo
from todolist.todo_exceptions import TodoNotDoneError, TodoNotFoundError
from todolist.todo_repository_protocol import TodoRepository


class UseCase(ABC):
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def __call__(self, *args, **kwargs):
        ...


class CreateTodoUseCase(UseCase):
    def __call__(self, title: str):
        todo = Todo(id=uuid4().hex, title=title)
        self.repository.save(todo)
        return todo


class ToggleDoneUseCase(UseCase):
    def __call__(self, id: str):
        todo = self.repository.get_by_id(id)
        if todo is None:
            raise TodoNotFoundError()

        todo.done = not todo.done
        self.repository.update(todo.id, todo)


class DeleteTodoUseCase(UseCase):
    def __call__(self, id: str):
        todo = self.repository.get_by_id(id)
        if todo is None:
            raise TodoNotFoundError()
        if not todo.done:
            raise TodoNotDoneError()
        self.repository.delete(todo.id)


class UpdateTodoUseCase(UseCase):
    def __call__(self, id: str, new_title: str):
        todo = self.repository.get_by_id(id)
        if todo is None:
            raise TodoNotFoundError()
        todo.title = new_title
        self.repository.update(id, todo)
