from colorama import Fore, Style

priority_li = ['low', 'mid', 'high']
status_li = ['to do', 'on going', 'done']

def add_task(datas, title, priority, status):
    "Add a task to the list of tasks"
    if datas:
        # Calculating ID for each new task :
        id = len(datas) + 1
        # Formatting task into a dictionnary and adding it to the list :
        if priority not in priority_li:
            print(f'\n{Fore.RED}Invalid priority {priority_li}{Style.RESET_ALL}\n')
        elif status not in status_li:
            print(f'\n{Fore.RED}Invalid status {status_li}{Style.RESET_ALL}\n')
        else:
            datas.append({'id':id, 'title':title, 'priority':priority, 'status':status})
            # Printing confirmation :
            print(f'\n{Fore.GREEN}{title} - Task added ✓{Style.RESET_ALL}')
            print() # Blank line
    else:
        # If this is the first task :
        id = 1
        datas = [{'id':id, 'title':title, 'priority':priority, 'status':status}]
        print(f'\n{Fore.GREEN}\n{title} - Task added ✓{Style.RESET_ALL}\n')
    return datas # Return full list with new task(s) included

def delete_task(datas, id):
    "Delete an existing task"
    if datas: 
        # Searching for the existence of the ID :
        try:
            task = datas[int(id) -1]
            answer = input(f'\n{Fore.YELLOW}Are you sure to delete task : {task['title']} ? (y/n){Style.RESET_ALL}\n') # Asking for confirmation
            if answer.upper() == 'Y':
                print(f"\n{Fore.RED}'{task['title']}' - Task removed x{Style.RESET_ALL}\n") # Printing confirmation of delete
                datas.remove(task) # Removing task
            else:
                return datas# Exit program if 'no' was entered by user
        except IndexError as err:
            print(f'\n{Fore.RED}This task does not exist x{Style.RESET_ALL}\n')
        # Reorganise IDs after delete :
        else:
            id = 1
            for el in datas:
                el['id'] = id
                id += 1
            return datas
    else:
        print(f"\n{Fore.RED}You haven't added any tasks yet. Try 'add' to create a task.{Style.RESET_ALL}\n")
    
def list_tasks(datas):
    "Print out the list of tasks"
    if datas:
        print() # first blank separator
        # Tab titles
        print(f"{'ID':<4}{'STATUS':<17}{'PRIORITY':<17}{'TASK':<30}")
        # Creating tilt separator :
        separator = ""
        for n in 2, 0, 15, 0, 15, 0, 30:
            if n != 0:
                for space in range(n):
                    separator += '-'
            else:
                separator += '  '
        print(separator)
        # Formatting data :
        for el in datas:
            # Defining priority color :
            if el['priority'] == 'high':
                col = Fore.RED
            elif el['priority'] == 'mid':
                col = Fore.YELLOW
            elif el['priority'] == 'low':
                col = Fore.GREEN
            # Display datas : 
            print(f'#{el['id']:<3}{f'[{el['status'].upper()}]':<17}{col+el['priority']+Style.RESET_ALL:<26}{el['title']:<30}')
        print() # Last blank separator
    else:
        print(f"\n{Fore.YELLOW}You haven't added any tasks yet. Try 'add' to create a task.{Style.RESET_ALL}\n")

def modify_task(datas, **params):
    "Modify an existing task"
    if not datas:
        print(f"\n{Fore.YELLOW}You haven't added any tasks yet. Try 'add' to create a task.{Style.RESET_ALL}\n")
    elif not params['id']:
        print(f"\n{Fore.RED}Please enter an ID to identify a task{Style.RESET_ALL}\n")
    else:
        try:
            id = params['id']
            task = datas[int(id) - 1]
            for key in params.keys():
                if params[key] is not None:
                    if key == 'priority' and params[key] not in priority_li:
                        print(f'\nInvalid priority {priority_li}\n')
                    elif key == 'status' and params[key] not in status_li:
                        print(f'\nInvalid status {status_li}\n')                    
                    else: 
                        task[key] = params[key]
                        if key != "id":
                            print(f'\n{Fore.GREEN}{task['title']} : {key} changed to {task[key]} {Style.RESET_ALL}\n')
        except IndexError:
            print(f'\n{Fore.RED}There is no task with this ID{Style.RESET_ALL}\n')
    return datas

def clear_tasks(datas):
    "Clear all tasks at once"
    answer = input(f'\n{Fore.YELLOW}Delete all tasks ? (y/n){Style.RESET_ALL}') # Asking for confirmation
    if answer.upper() == 'Y':
        datas.clear()
        print(f'\n{Fore.GREEN}✓ Done! - Nothing in there anymore{Style.RESET_ALL}\n')
    return datas

def sort_tasks(datas, **kwargs):
    "Sort tasks by parameter"
    if kwargs['priority'] and kwargs['status']:
        print(f'\n{Fore.RED}Choose --Priority OR --Status to sort data{Style.RESET_ALL}\n')
        return
    elif kwargs['priority']:
        option = kwargs['priority']
        datas = sorted(datas, key=lambda x: x['priority'] == option, reverse=True)
    elif kwargs['status']:
        option = kwargs['status']
        datas = sorted(datas, key=lambda x: x['status'] == option, reverse=True)
    list_tasks(datas)

def print_stats(datas):
    "Print stats of existing tasks"
    total_tasks = len(datas)
    total_done = sum(1 for el in datas if el['status'] == 'done')
    total_ongoing = sum(1 for el in datas if el['status'] == 'on going')
    total_todo = sum(1 for el in datas if el['status'] == 'to do')
    print('\nStats')
    print('--------------')
    print(f'Total : {total_tasks}\nDone : {total_done}\nOn going : {total_ongoing}\nTo do : {total_todo}\n')


   

    
        

