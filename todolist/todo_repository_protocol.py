from typing import Protocol

from todolist.todo_entity import Todo


class TodoRepository(Protocol):
    todos: dict[str, Todo]
    def get_by_id(self, id: str) -> Todo | None: ...
    def save(self, todo: Todo) -> None: ...
    def update(self, id: str, todo: Todo) -> None: ...
    def delete(self, id: str) -> None: ...
    def get_all(self) -> list[Todo]: ...
