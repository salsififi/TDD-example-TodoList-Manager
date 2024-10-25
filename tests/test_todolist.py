import pytest

from todolist.in_memory_todo_repository import InMemoryTodoRepository
from todolist.todo_exceptions import TodoNotFoundError, TodoNotDoneError
from todolist.todo_usecase import CreateTodoUseCase, ToggleDoneUseCase, DeleteTodoUseCase, UpdateTodoUseCase


@pytest.fixture
def repository():
    return InMemoryTodoRepository()


@pytest.fixture
def new_todo(repository):
    create_todo_usecase = CreateTodoUseCase(repository)
    return create_todo_usecase("A new todo")


@pytest.fixture
def new_todo_done(repository, new_todo):
    toggle_done_use_case = ToggleDoneUseCase(repository)
    toggle_done_use_case(new_todo.id)
    return new_todo


def test_todo(repository):
    create_usecase = CreateTodoUseCase(repository)
    created_todo = create_usecase("A new todo")
    fetched_todo = repository.get_by_id(created_todo.id)

    assert fetched_todo is not None
    assert fetched_todo.title == "A new todo"


def test_cant_toggle_todo_not_existing(repository):
    toggle_done_usecase = ToggleDoneUseCase(repository)

    with pytest.raises(TodoNotFoundError):
        toggle_done_usecase("non_existing_id")


def test_toggle_todo(repository, new_todo):
    fetched_todo = repository.get_by_id(new_todo.id)

    toggle_done_use_case = ToggleDoneUseCase(repository)
    toggle_done_use_case(new_todo.id)

    assert fetched_todo is not None
    assert fetched_todo.done


def test_cant_delete_todo_not_existing(repository):
    delete_todo_usecase = DeleteTodoUseCase(repository)

    with pytest.raises(TodoNotFoundError):
        delete_todo_usecase("not_existing_id")


def test_cant_delete_todo_not_done(repository, new_todo):
    delete_todo_usecase = DeleteTodoUseCase(repository)

    with pytest.raises(TodoNotDoneError):
        delete_todo_usecase(new_todo.id)


def test_delete_todo_done(repository, new_todo_done):
    delete_todo_usecase = DeleteTodoUseCase(repository)
    delete_todo_usecase(new_todo_done.id)

    assert repository.get_by_id(new_todo_done.id) is None


def test_cant_update_todo_not_existing(repository):
    update_todo_usecase = UpdateTodoUseCase(repository)

    with pytest.raises(TodoNotFoundError):
        update_todo_usecase("not_existing_id", "New title")


def test_update_todo(repository, new_todo):
    update_todo_usecase = UpdateTodoUseCase(repository)
    update_todo_usecase(new_todo.id, "New title")

    fetched_todo = repository.get_by_id(new_todo.id)

    assert fetched_todo is not None
    assert new_todo.title == "New title"
