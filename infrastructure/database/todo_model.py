from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import declarative_base

from infrastructure.database.connexion import get_engine

Base = declarative_base()
engine = get_engine()


class TodoModel(Base):
    __tablename__ = "todo"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    done = Column(Boolean, nullable=False, default=False)


Base.metadata.create_all(engine)
