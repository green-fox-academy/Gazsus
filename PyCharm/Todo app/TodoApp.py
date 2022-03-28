import json

class TodoApp:
    
    def __init__(self):
        self.file_name = 'todo.txt'
        self.current_tasks = self.load_file()

    def add_task(self, task):
        self.current_tasks.append({'task': task, 'done': False})
        self.save_file()

    def remove_task(self, index):
        if index > len(self.current_tasks) or index == 0:
            print('Unable to remove: index is out of bound')
        else:
            self.current_tasks.pop(index - 1)
            self.save_file()
            
    def check_task(self, index):
        if index > len(self.current_tasks) or index == 0:
            print('Unable to do task: index is out of bound')
        else:
            self.current_tasks[index - 1]['done'] = True
            self.save_file()
        
    def list_tasks(self):
        result = ''
        index = 0

        if len(self.current_tasks) == 0:
            return 'No tasks for current day'

        for task in self.current_tasks:
            index += 1
            result += str(index) + ' - ' + ('[x] ' if task['done'] else '[ ] ') + task['task'] + '\n'
        return result

    def save_file(self):
        file = open(self.file_name, 'w')
        todo_list = json.dumps(self.current_tasks)
        file.write(todo_list)
        
    def load_file(self):
        try:
            file = open(self.file_name, 'r')
            return json.loads(file.read())
        except:
            return []