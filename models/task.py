class Task:
    _id_counter = 1

    def __init__(self, title: str, status: str = "pending", assigned_to: str = None):
        self.id = Task._id_counter
        self.title = title
        self._status = status
        self.assigned_to = assigned_to
        Task._id_counter += 1

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ["pending", "in-progress", "completed"]:
            raise ValueError("Invalid status")
        self._status = value

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["status"], data["assigned_to"])
        task.id = data["id"]
        return task
