from pathlib import Path
from typing import Annotated

import typer

from cli_task_manager.manager import TaskManager, TaskNotFoundError
from cli_task_manager.models import Priority, Status

app = typer.Typer(help="CLI Task Manager")

db_file = Path("tasks.json")
manager = TaskManager(db_file)


@app.command()
def add(
    name: Annotated[str, typer.Argument(help="Title of the task")],
    priority: Annotated[
        Priority, typer.Option("--priority", "-p", help="Priority of the task")
    ] = Priority.LOW,
    due: Annotated[
        str, typer.Option("--due", "-d", help="Due date in format YYYY-MM-DD")
    ] = "2026-12-31",
) -> None:
    """Adds new task to the list"""
    task = manager.add_task(name, priority, due)
    typer.secho(f"Added task '{task.name}' with ID '{task.id}", fg=typer.colors.GREEN)


@app.command()
def in_progress(
    task_id: Annotated[int, typer.Argument(help="ID of the task to be in progress")],
) -> None:
    """Marks the task as IN PROGRESS"""
    try:
        manager.change_status(task_id, Status.IN_PROGRESS)
    except TaskNotFoundError as e:
        typer.secho(str(e), fg=typer.colors.RED)


@app.command()
def done(
    task_id: Annotated[int, typer.Argument(help="Task ID to mark it DONE")],
) -> None:
    """Marks the task as DONE"""
    try:
        manager.change_status(task_id, Status.DONE)
    except TaskNotFoundError as e:
        typer.secho(str(e), fg=typer.colors.RED)


@app.command()
def delete(
    task_id: Annotated[int, typer.Argument(help="ID of the task to delete")],
) -> None:
    """Delete the task forever"""
    try:
        manager.delete_task(task_id)
    except TaskNotFoundError as e:
        typer.secho(str(e), fg=typer.colors.RED)


@app.command()
def list_tasks() -> None:
    """Shows list of the tasks"""
    if len(manager.tasks) == 0:
        typer.secho("There is no tasks", fg=typer.colors.RED)
        return
    for task in manager.tasks:
        msg = f"[{task.id}] {task.name} | Priority: {task.priority.value} | Due: {task.due_date} | Status: {task.status.value}"
        typer.secho(f"{msg}", fg=typer.colors.GREEN)


if __name__ == "__main__":
    app()
