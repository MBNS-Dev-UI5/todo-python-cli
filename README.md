# Python CLI To‑Do List App

A simple, lightweight command‑line To‑Do List application in Python. Add, view, and delete tasks—deleted ones are archived with timestamps for easy tracking.


## Table of Contents
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [File Structure](#file-structure)  
- [Data Format](#data-format)  
- [Customization Ideas](#customization-ideas)  
- [Contributing](#contributing)  

---

## Features
- **Add tasks**: Records tasks with description and timestamp (`created_at`)
- **List tasks**: Shows current tasks with their index and creation times
- **Delete tasks**: Removes tasks by index, archiving them with a deletion timestamp (`deleted_at`)

---

## Requirements
- Python 3.x

---

## Installation
No special setup required. Just have Python installed on your system.

---

## Usage
1. Open your terminal and go to the project directory.  
2. Run the script:
   ```bash
   python todo_app.py
3. Use the interactive menu:
   Welcome to the To‑Do List App :)
   Please select one of the following options:
   1. Add New Task
   2. Delete a Task
   3. Check All Tasks
   4. Quit
4. Input a number to perform the corresponding action.

---

## File Structure
 .<br>
 ├── todo_app.py            # Main Python script<br>
 ├── README.md              # This file<br>
 ├── tasks.json             # Active task storage<br>
 └── deleted_tasks.json     # Archive for deleted tasks

---

## Data Format
#### tasks.json:

      [
        {
          "description": "Buy groceries",
          "created_at": "2025-08-12 10:23:45"
        }
      ]
      
#### deleted_tasks.json:

      [
        {
          "description": "Buy groceries",
          "created_at": "2025-08-12 10:23:45",
          "deleted_at": "2025-08-12 14:07:20"
        }
      ]

---

## Customization Ideas
- Modify the timestamp format in get_current_time()
- Add features like priority, due date, or categories
- Enhance UI with color libraries like colorama
- Upgrade storage from JSON to SQLite for better scalability
- Add batch operations (e.g., delete multiple tasks, restore deleted items)

---

## Contributing

Contributions are welcome! Feel free to fork, enhance features, or submit bug fixes.
