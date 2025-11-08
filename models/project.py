from models.task import Task

class Project:
    _id_counter = 1

    def __init__(self, title: str, description: str, due_date: str):
        self.id = Project._id_counter
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []
        Project._id_counter += 1

    def add_task(self, task: Task):
        self.tasks.append(task)

    def __repr__(self):
        return f"Project(id={self.id}, title={self.title}, due_date={self.due_date})"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [t.to_dict() for t in self.tasks],
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(data["title"], data["description"], data["due_date"])
        project.id = data["id"]
        project.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        return project
