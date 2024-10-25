from todolist.todo_entity import Todo


class InMemoryTodoRepository:
    def __init__(self):
        self.todos = {}

    def delete(self, id: str) -> None:
        del self.todos[id]

    def get_by_id(self, id: str) -> Todo | None:
        return self.todos.get(id)

    def save(self, todo: Todo) -> None:
        self.todos[todo.id] = todo

    def update(self, id: str, updated_todo: Todo) -> None:
        self.todos[id] = updated_todo

    def get_all(self) -> list[Todo]:
        return list(self.todos.values())
