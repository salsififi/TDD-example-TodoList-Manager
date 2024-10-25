from sqlalchemy.orm import Session

from infrastructure.database.todo_converter import TodoConverter
from infrastructure.database.todo_model import TodoModel
from todolist.todo_entity import Todo


class SQLiteTodoRepository:

    todos: dict[str, Todo]

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: str) -> Todo | None:
        todo = self.session.query(TodoModel).filter(TodoModel.id == id).first()
        return TodoConverter.model_to_entity(todo) if todo else None

    def save(self, todo: Todo) -> None:
        model = TodoConverter.entity_to_model(todo)
        self.session.add(model)
        self.session.commit()

    def update(self, id: str, todo: Todo) -> None:
        self.session.query(TodoModel).filter(TodoModel.id == id).update({
            "title": todo.title,
            "done": todo.done})
        self.session.commit()

    def delete(self, id: str) -> None:
        self.session.query(TodoModel).filter(TodoModel.id == id).delete()
        self.session.commit()

    def get_all(self) -> list[Todo]:
        todos = self.session.query(TodoModel).all()
        return [TodoConverter.model_to_entity(todo) for todo in todos]
