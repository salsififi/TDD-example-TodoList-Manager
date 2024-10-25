from pydantic import BaseModel, ConfigDict


class Todo(BaseModel):
    id: str
    title: str
    done: bool = False

    model_config = ConfigDict(from_attributes=True)


class TodoCreate(BaseModel):
    title: str
