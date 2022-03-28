import sys
from TodoApp import TodoApp

sys.argv.pop(0)
args = sys.argv
if len(args) == 0:
    print('Command Line Todo application\n'
          '=============================\n'
          'Command line arguments:\n'
          '    -l   Lists all the tasks\n'
          '    -a   Adds a new task\n'
          '    -r   Removes an task\n'
          '    -c   Completes an task')
else:
    todo = TodoApp()
    if args[0] == '-l':
        print(todo.list_tasks())
    elif args[0] == '-a':
        if len(args) == 1:
            print('Unable to add: no task provided')
        else:
            todo.add_task(args[1])
    elif args[0] == '-r':
        if len(args) == 1:
            print('Unable to remove: no index provided')
        else:   
            try:
                todo.remove_task(int(args[1]))
            except:
                print('Unable to remove: index is not a number')
    elif args[0] == '-c':
        if len(args) == 1:
            print('Task checking failed: no index provided')
        else:
            todo.check_task(int(args[1]))
    else:
        print('Unsupported argument')