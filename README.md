# To do App

A simple command line task manager in python

## Installation
```
git clone https://github.com/kevin-teisseire/todo-py
cd todo-py
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Use
```
python3 td_main.py add --title "Take out the trash" --priority "high" --status "to do"
python3 td_main.py list
python3 td_main.py modify --id 2 -s "done"
```
## Commands

| Command | Description |
| ------- | ----------- |
| add     | Add a new task |
| list    | List all tasks |
| modify  | Modify an existing task |
| delete  | Delete an existing task |
| sort    | Sort tasks by parameter |
| clear   | Delete all tasks |
| stats   | Display tasks statistics |

## Options

For all available options : python3 td_main.py --help
