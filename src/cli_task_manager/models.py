from dataclasses import dataclass
from enum import StrEnum

class Status(StrEnum):
    DONE = "done"
    IN_PROGRESS = "in_progress"
    TODO = "to do"

class Priority(StrEnum):
    HIGH = "high"
    MID = "mid"
    LOW = "low"

@dataclass
class Task:
    id :int
    name: str
    priority: Priority
    due_date: str
    status: Status = Status.TODO
    