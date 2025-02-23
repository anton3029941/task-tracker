from datetime import datetime
import json
import sys

# start of the code
try:
    # loads json in code task list
    with open('tasklist.json', "r") as f:
        storage = json.load(f)
except (json.decoder.JSONDecodeError, FileNotFoundError):
    storage = {}
    with open('tasklist.json', "w") as f:
        json.dump(storage, f)

command = sys.argv[1:]
if not command:
    print("Enter the command. use 'python task-cli.py help' for help.")
    sys.exit(1)

# id for new tasks
id_num = max(map(int, storage.keys()), default=-1) + 1 if storage else 0

action = command[0]

# Adds a new task to the storage
if action == "add":
    if len(command) <= 1:
        print("Task not entered.")
    else:
        task_description = " ".join(command[1:])
        storage[str(id_num)] = {
            "task": task_description,
            "status": "not done",
            "date of creation": str(datetime.now()),
            "date of update": ""
        }
        print(f"Id {id_num} assigned to task")
        id_num += 1

# output task list
elif action == "list":
    for key, value in storage.items():
        print(f"{key}: {value}")

# output done, in progress or to_do tasks
elif action in ["list-done", "list-in-progress", "list-todo"]:
    status_filter = {
        "list-done": "done",
        "list-in-progress": "in progress",
        "list-todo": "not done"
    }[action]
    filtered_tasks = {k: v for k, v in storage.items() if v["status"] == status_filter}
    for key, value in filtered_tasks.items():
        print(f"{key}: {value}")

# updates the task
elif action == "update":
    if len(command) < 3:
        print("Usage: update <id> <new task>")

    task_id = command[1]
    if task_id not in storage:
        print("This ID is not on the list")
    else:
        new_task = " ".join(command[2:])
        storage[task_id]["task"] = new_task
        storage[task_id]["date of update"] = str(datetime.now())

# deletes the task
elif action == "delete":
    if len(command) < 2:
        print("Usage: delete <id>")

    task_id = command[1]
    if task_id not in storage:
        print("This ID is not on the list")
    else:
        del storage[task_id]

# marking task to do, in progress and done
elif action in ["mark-todo", "mark-in-progress", "mark-done"]:
    if len(command) < 2:
        print(f"Usage: {action} <id>")

    task_id = command[1]
    if task_id not in storage:
        print("This ID is not on the list")
    else:
        new_status = {
            "mark-todo": "not done",
            "mark-in-progress": "in progress",
            "mark-done": "done"
        }[action]
        storage[task_id]["status"] = new_status
        storage[task_id]["date of update"] = str(datetime.now())

# output all commands
elif command[0] == "help":
    print("""
Available commands:
  add <task>               - Add a new task
  list                     - List all tasks
  list-done                - List completed tasks
  list-in-progress         - List tasks in progress
  list-todo                - List tasks not done
  update <id> <new task>   - Update a task
  delete <id>              - Delete a task
  mark-in-progress <id>    - Mark a task as in progress
  mark-done <id>           - Mark a task as done
  clear                    - Clear all tasks
  exit                     - Exit the application
  help                     - Show this help message
""")


# clears tasklist
elif action == "clear":
    storage = {}
    print("Task list cleared.")

else:
    print("Unknown command")

# saves tasklist to json file
with open('tasklist.json', 'w') as f:
    json.dump(storage, f, indent=4)
