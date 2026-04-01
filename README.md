# To do App

A simple command line task manager in python

## Installation

git clone https://github.com/kevin-teisseire/todo-py
cd todo-py
pip install -r requirements.txt

## Use

python3 td_main.py add --title "Take out the trash" --priority "high" --status "to do"
python3 td_main.py list
python3 td_main.py modify --id 2 -s "done"

## Commands

* add
* list
* modify
* delete
* sort
* clear
* stats

For more details : python3 td_main.py --help
