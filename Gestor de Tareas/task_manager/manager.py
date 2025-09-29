import json
from task_manager.task import Task
import os

class TaskManager:
    def __init__(self, filepath="data/tasks.json"):
        self.filepath = filepath
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                tasks_data = json.load(f)
                for t in tasks_data:
                    self.tasks.append(Task(**t))

    def save_tasks(self):
        with open(self.filepath, "w") as f:
            json.dump([t.__dict__ for t in self.tasks], f, indent=4)

    def add_task(self, title, description):
        id = len(self.tasks) + 1
        task = Task(id, title, description)
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        for t in self.tasks:
            status = "✔" if t.completed else "❌"
            print(f"{t.id}. {t.title} - {status}")

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save_tasks()