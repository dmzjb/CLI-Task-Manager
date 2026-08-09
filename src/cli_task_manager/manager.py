from cli_task_manager.models import Status, Priority, Task
import itertools
import json
from dataclasses import asdict
from pathlib import Path


id_iter = itertools.count()

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
                priority=item["priority"],
                due_date=item["due_date"],
                status= item["status"]
            )
            self.tasks.append(task)

    def save_task_to_json(self) -> None:
       data_to_save: list[dict[str, str]] = []
       for task in self.tasks:
           data_to_save.append(asdict(task))

       with self.file_path.open("w",encoding="utf-8"):
           json.dumps(data_to_save, indent=4, ensure_ascii=False)

    def add_task(self, name: str, prior: Priority, due: str) -> Task:
        if not self.tasks:
            task_id = 1
        else: 
            task_id = next(id_iter)

        task = Task(
            id=task_id,
            name=name,
            priority=prior,
            due_date=due,
            status=Status.TODO,
        )
        self.tasks.append(task)
        self.save_task_to_json
        return task
