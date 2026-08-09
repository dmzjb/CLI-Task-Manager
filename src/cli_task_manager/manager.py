from cli_task_manager.models import Status, Priority, Task
from cli_task_manager.exceptions import TaskNotFoundError
import json
from typing import Any
from dataclasses import asdict
from pathlib import Path

class TaskManager:
    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)
        self.tasks: list[Task] = []

        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

        self.load_from_file()

    def load_from_file(self):
        """Odczytuje z pliku json i konwertuje slowniki na obiekty Task"""
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.tasks.clear()
        for item in data:
            task = Task(
                id=item["id"],
                name=item["name"],
                priority=Priority(item["priority"]),
                due_date=item["due_date"],
                status= Status(item["status"])
            )
            self.tasks.append(task)

    def save_task_to_json(self) -> None:
        data_to_save: list[dict[str, Any]] = []
        for task in self.tasks:
           data_to_save.append(asdict(task))

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data_to_save, file, indent=4, ensure_ascii=False)

    def add_task(self, name: str, prior: Priority, due: str) -> Task:
        task_id = max((task.id for task in self.tasks), default=0) + 1

        task = Task(
            id=task_id,
            name=name,
            priority=prior,
            due_date=due,
            status=Status.TODO,
        )
        self.tasks.append(task)
        self.save_task_to_json()
        return task

    def change_status(self, task_id: int, status: Status) -> None:
        for task in self.tasks:
            if task.id == task_id:
                task.status = status
                self.save_task_to_json()
                return
        raise TaskNotFoundError(f"Task {task_id} doesn't exist")

    def delete_task(self, task_id: int) -> None:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_task_to_json()
                return
        raise TaskNotFoundError(f"Task {task_id} doesn't exist")
    