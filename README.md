A simple task tracker with a command line interface that allows you to add, update, delete tasks and track their status.

Functionality
--- Add tasks: add <task>
--- View all tasks: list
--- View completed tasks: list-done
--- View tasks in progress: list-in-progress
--- View tasks to do: list-todo
--- Update a task: update <id> <new task>
--- Delete a task: delete <id>
--- Mark a task in progress: mark-in-progress <id>
--- Mark a task done: mark-done <id>
--- Clear all tasks: clear
--- Show help: help
--- Exit the application: exit

Example of use
  task-cli add buy milk
  Id 0 assigned to task
  task-cli list
  0: {'task': 'buy milk', 'status': 'not done', 'date of creation': '...', 'date of update': ''}

Structure of project
task-tracker-cli/
├─ task_tracker.py       # Main script of application
├─ tasklist.json         # Storage of tasks in JSON format
└─ README.md             # Documentation of project

Requires python 3.7+

This project is distributed under the MIT license. For more information, see the file LICENSE.
