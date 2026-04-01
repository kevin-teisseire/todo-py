import argparse, storage, tasks

# Creating parser object
parser = argparse.ArgumentParser(description="A simple command line task manager")

# Defining the commands in use
parser.add_argument('command', help='Commands are : list, add, modify, sort, stats, delete or clear')
parser.add_argument('-t', '--title')
parser.add_argument('-p', '--priority')
parser.add_argument('-s', '--status')
parser.add_argument('-id', '--id')

# Getting arguments
arguments = parser.parse_args()

### Main program ###
if __name__ == '__main__':
    datas = storage.loadF()
    if arguments.command == 'add':
        mod_datas = tasks.add_task(datas, arguments.title, arguments.priority, arguments.status)
        storage.saveF(mod_datas)
    elif arguments.command == 'delete':
        mod_datas = tasks.delete_task(datas, arguments.id)
        storage.saveF(mod_datas)
    elif arguments.command == 'modify':
        mod_datas = tasks.modify_task(datas, id=arguments.id, title=arguments.title, priority=arguments.priority, status=arguments.status)
        storage.saveF(mod_datas)
    elif arguments.command == 'clear':
        mod_datas = tasks.clear_tasks(datas)
        storage.saveF(mod_datas)
    elif arguments.command == 'list':
        tasks.list_tasks(datas)
    elif arguments.command == 'sort':
        tasks.sort_tasks(datas, priority=arguments.priority, status=arguments.status)
    elif arguments.command == 'stats':
        tasks.print_stats(datas)



        

        



