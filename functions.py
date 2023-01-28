


def get_todos(filepath=r'C:\Users\Team OS\PycharmProjects\Python programs\Main\todos.txt'):

    with open(filepath, 'r') as fileLocal:
        todosLocal = fileLocal.readlines()
    return todosLocal


def writeTodos(todos_arg, filepath=r'C:\Users\Team OS\PycharmProjects\Python programs\Main\todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print(__name__)

