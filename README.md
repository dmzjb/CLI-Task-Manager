# 🚀 CLI Task Manager

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Framework](https://img.shields.io/badge/CLI-Typer-black.svg)
![Package Manager](https://img.shields.io/badge/Package_Manager-uv-purple.svg)
![Code Style](https://img.shields.io/badge/Code_Style-Ruff-orange.svg)

A simple, fast, and strictly-typed Command Line Interface (CLI) Task Manager built with Python. It allows you to manage your daily tasks directly from the terminal, storing all data locally in a JSON file.

Built with modern Python standards, featuring **Typer** for the CLI interface, strict type hinting, and **Pytest** for testing.

---

## ✨ Features

*   **➕ Add Tasks:** Create new tasks with custom priorities (`low`, `mid`, `high`) and due dates.
*   **📈 Track Progress:** Update task statuses to "In Progress" or "Done".
*   **📋 List Tasks:** View all your current tasks in the terminal with a clean layout.
*   **🗑️ Delete Tasks:** Remove tasks you no longer need.
*   **💾 Persistent Storage:** All data is safely saved in a local `tasks.json` file.
*   **🛡️ Robust Error Handling:** Clean, user-friendly error messages (e.g., when trying to modify a non-existent task ID).

## 🛠️ Tech Stack

*   **Language:** Python 3.10+
*   **CLI Framework:** Typer
*   **Package Manager:** uv
*   **Testing:** Pytest
*   **Linter & Formatter:** Ruff

---

## 📦 Installation

This project uses `uv` for lightning-fast dependency management.

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/dmzjb/CLI-Task-Manager.git
   ```

2. Navigate to the project root directory:
   ```bash
   cd cli-task-manager
   ```

3. Sync the environment and install dependencies:
   ```bash
   uv sync
   ```
   > 💡 **Note:** If you are running this project inside a cloud-synced folder (like OneDrive or Google Drive), you might need to enforce copy mode for uv using `uv sync --link-mode=copy`.

---

## 💻 Usage

The application uses the modern `src-layout`. All commands should be run from the root directory of the project.

### Adding a Task
Add a new task with a title. You can optionally set a priority (`low`, `mid`, `high`) and a due date (`YYYY-MM-DD`).
```bash
python src/cli_task_manager/main.py add "Learn Pytest" --priority high --due 2026-10-10
```

### Listing Tasks
Display all tasks currently saved in your manager.
```bash
python src/cli_task_manager/main.py list-tasks
```

### Changing Task Status
Mark a task as "In Progress" or "Done" using its ID.
```bash
python src/cli_task_manager/main.py 1 in-progress
python src/cli_task_manager/main.py 1 done
```

### Deleting a Task
Permanently remove a task by its ID.
```bash
python src/cli_task_manager/main.py 1 delete
```

---

## 🧪 Development & Testing

This project emphasizes code quality and reliability.

### Running Tests
Tests are written using **Pytest** and utilize `tmp_path` fixtures to ensure your actual `tasks.json` data is never overwritten during testing. To run the test suite:
```bash
pytest
```

### Formatting and Linting
To maintain consistent code style, use **Ruff** before committing any changes:
```bash
ruff format
ruff check --fix
```