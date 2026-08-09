from pathlib import Path

import pytest

from cli_task_manager.manager import TaskManager, TaskNotFoundError
from cli_task_manager.models import Priority, Status


def test_nowy_manager_tworzy_pusty_plik(tmp_path: Path) -> None:
    plik_testowy: Path = tmp_path / "test_tasks.json"

    manager = TaskManager(plik_testowy)

    assert len(manager.tasks) == 0
    assert plik_testowy.exists()


def test_dodawanie_zadania_zapisuje_do_pliku(tmp_path: Path) -> None:
    plik_testowy: Path = tmp_path / "test_tasks.json"
    manager = TaskManager(plik_testowy)

    zadanie = manager.add_task("Nauczyć się Pytesta", Priority.HIGH, "2026-10-10")

    assert len(manager.tasks) == 1
    assert manager.tasks[0].name == "Nauczyć się Pytesta"
    assert zadanie.id == 1

    nowy_manager = TaskManager(plik_testowy)
    assert len(nowy_manager.tasks) == 1
    assert nowy_manager.tasks[0].name == "Nauczyć się Pytesta"


def test_zmiana_statusu_na_nieistniejacym_zadaniu_rzuca_blad(tmp_path: Path) -> None:
    plik_testowy: Path = tmp_path / "test_tasks.json"
    manager = TaskManager(plik_testowy)

    with pytest.raises(TaskNotFoundError, match="Task 999 doesn't exist"):
        manager.change_status(999, Status.DONE)


def test_zmiana_statusu_na_done(tmp_path: Path) -> None:
    plik_testowy: Path = tmp_path / "test_tasks.json"
    manager = TaskManager(plik_testowy)

    manager.add_task("Nauczyć się Pytesta", Priority.HIGH, "2026-10-10")
    manager.change_status(1, Status.DONE)
    assert manager.tasks[0].status == Status.DONE


def test_usuwanianie_zadania(tmp_path: Path) -> None:
    plik_testowy: Path = tmp_path / "test_tasks.json"
    manager = TaskManager(plik_testowy)

    manager.add_task("Nauczyć się Pytesta", Priority.HIGH, "2026-10-10")
    assert len(manager.tasks) == 1
    manager.delete_task(1)
    assert len(manager.tasks) == 0


def test_usuwanianie_nieistniejacego_zadania(tmp_path: Path) -> None:
    plik_testowy: Path = tmp_path / "test_tasks.json"
    manager = TaskManager(plik_testowy)

    with pytest.raises(TaskNotFoundError, match="Task 999 doesn't exist"):
        manager.delete_task(999)
