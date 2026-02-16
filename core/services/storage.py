import json
import os
from core.models.task import Task


class StorageService:
    def __init__(self, filename="tasks.json"):
        # Store in a 'data' folder
        self.data_dir = os.path.join(os.getcwd(), "data")
        self.file_path = os.path.join(self.data_dir, filename)

        # Ensure directory exists
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        # Ensure file exists
        if not os.path.exists(self.file_path):
            self.save_tasks([])

    def save_tasks(self, tasks):
        """Save a list of Task objects to JSON."""
        with open(self.file_path, "w") as f:
            json_data = [task.to_dict() for task in tasks]
            json.dump(json_data, f, indent=4)

    def load_tasks(self):
        """Load tasks from JSON and return a list of Task objects."""
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def add_task(self, task):
        """Helper to add a single task and save immediately."""
        tasks = self.load_tasks()
        tasks.append(task)
        self.save_tasks(tasks)

    def delete_task(self, task_id):
        """Helper to delete a task by ID."""
        tasks = self.load_tasks()
        tasks = [t for t in tasks if t.id != task_id]
        self.save_tasks(tasks)
