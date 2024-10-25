from infrastructure.database.todo_model import TodoModel
from todolist.todo_entity import Todo


class TodoConverter:
    """C'est ce qu'on appelle un helper"""
    
    @staticmethod
    def model_to_entity(model: TodoModel) -> Todo:
        return Todo.model_validate(model)

    @staticmethod
    def entity_to_model(entity: Todo) -> TodoModel:
        return TodoModel(id=entity.id,
                         title=entity.title,
                         done=entity.done)
