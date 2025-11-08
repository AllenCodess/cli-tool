from models.project import Project

class User:
    _id_counter = 1

    def __init__(self, name: str, email: str):
        self.id = User._id_counter
        self.name = name
        self.email = email
        self.projects = []
        User._id_counter += 1

    def add_project(self, project: Project):
        self.projects.append(project)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [p.to_dict() for p in self.projects],
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"], data["email"])
        user.id = data["id"]
        user.projects = [Project.from_dict(p) for p in data.get("projects", [])]
        return user
