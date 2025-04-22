FILENAME = 'todo.txt'

def get_todos(filename = FILENAME):
    with open(filename) as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg,filename = FILENAME):
    with open(filename,'w') as file:
        file.writelines(todos_arg)
