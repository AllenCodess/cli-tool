import pytest
from models.user import User
from models.project import Project
from models.task import Task

def test_user_creation():
    user = User("Alice", "alice@example.com")
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    assert isinstance(user.projects, list)

def test_project_creation():
    project = Project("Test Project", "Some description", "2025-12-01")
    assert project.title == "Test Project"
    assert project.due_date == "2025-12-01"
    assert project.tasks == []

def test_add_project_to_user():
    user = User("Bob", "bob@example.com")
    project = Project("Proj", "Desc", "2025-10-10")
    user.add_project(project)
    assert len(user.projects) == 1
    assert user.projects[0].title == "Proj"

def test_task_creation_and_status():
    task = Task("Implement feature")
    assert task.status == "pending"
    task.status = "completed"
    assert task.status == "completed"

def test_invalid_task_status():
    task = Task("Bad status test")
    with pytest.raises(ValueError):
        task.status = "unknown"
