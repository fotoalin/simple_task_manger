import uuid
from datetime import datetime


class Task:
    def __init__(self, content):
        self._id = None
        self.content = content
        self.completed = False
        self._created_at = datetime.now()
        self._updated_at = None

    def __repr__(self):
        return f"<Task: {self.content}>"

    def __str__(self):
        return self.content


class Database:
    def __init__(self, content=None, tasks=[]):
        self.content = content
        self.tasks = []

    def add(self, task):
        task.id = str(uuid.uuid4())
        task.created_at = datetime.now()
        self.tasks.append(task)
        return task

    def update(self, task, new_content):
        task.content = new_content
        task.updated_at = datetime.now()
        return task

    def get(self, id=None):
        if id is not None:
            for task in self.tasks:
                if task.id == id:
                    return task
            # If no task matches the ID, return None
            return None
        else:
            raise ValueError("No id provided")

    def filter(self, completed=False):
        return [task for task in self.tasks if task.completed == completed]

    def search(self, term):
        return [task for task in self.tasks if term.lower() in task.content.lower()]

    def all(self):
        return self.tasks

    def delete(self, task):
        # Check if the task is actually in the list
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            # Handle the case where the task is not found
            raise ValueError("Task not found")

    def update(self, task, new_content):
        task.content = new_content
