# Task Tracker Cli Application

import sys
import os
import json as js
from datetime import datetime as dt

FILE_NAME = 'tasks.json'


def load_file():
    """ Looks for the json file and loads the data present in the file"""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME,'r') as f:
        try:
            return js.load(f)
        except js.JSONDecodeError:
            return []
        
tasks = load_file()

def task_present(description):
    """Checks wether any task with the same description is present or not"""
    for task in tasks:
        if task['description']  == description:
            return 'present'
    return 'not present'



def add_task(description):
    """Adds the new task to the Tasks file"""

    if task_present(description) == 'present':
        return "Task is already present"
    
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = max(task['id'] for task in tasks) + 1

    new_task = {
            'id':new_id,
            'description': description,
            'status':"to-do",
            'date':dt.now().isoformat()
            }

    tasks.append(new_task)

    with open(FILE_NAME,'w') as f:
        js.dump(tasks,f,indent=4)

    return f"The Task has been added with ID:{new_id}"


def task_list():
    """Returns the list of tasks present in the file"""
    if len(tasks) == 0:
        print("No tasks are present")
    else:
        for task in tasks:
            print(f"ID:{task['id']}\nDescription:{task['description']}\nStatus:{task['status']}\nDate Crated:{task['date']}")

def update_task(id):
    """Updates a task based on the task id"""
    

def main():
    while True:
        print("""Choices you have 
            1. Adding Task (add)
            2. List of tasks (list)
            3. exit (exit/quit)
            """)
        choice = input("Enter your choice:")
        match choice:
            case 'add': 
                describe = input('Enter the task description:').lower()
                result = add_task(describe)
                print(result)
                
            case 'list':
                task_list()

            case 'exit' | 'quit':
                sys.exit()
                
            case _:
                print("Enter a Valid choice")


if __name__ == "__main__":
    main()
                

