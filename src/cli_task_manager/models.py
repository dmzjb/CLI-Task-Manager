from dataclasses import dataclass, field
from enum import StrEnum
from datetime import datetime
import itertools

class Status(StrEnum):
    DONE = "done"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"

class Priority(StrEnum):
    HIGH = "high"
    MID = "mid"
    LOW = "low"

@dataclass
class Task:
    name: str
    priority: Priority
    due_date: datetime
    status: Status
    id: int = field(default_factory=lambda: next(Task.id_iter))

    id_iter = itertools.count()


