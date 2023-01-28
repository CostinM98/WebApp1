import functions
import time
import PySimpleGUI as gl
gl.theme('DarkPurple4')

clock=gl.Text('',key='clock')

label = gl.Text('Type in a to-do')
inputBox = gl.InputText(tooltip='Enter a ToDo', key='todo')

addButton = gl.Button('Add',size=20)
listBox = gl.Listbox(values=functions.get_todos(), key='todos',
                     enable_events=True, size=[45, 10])

editButton = gl.Button("Edit")
completeButton=gl.Button('Complete')
exitbutton=gl.Button('Exit')
window = gl.Window('My To-Do App',
                   layout=[[clock],
                       [label]
                       , [inputBox, addButton]
                       , [listBox, editButton,completeButton],
                           [exitbutton]],

                   font=('Verdana', 21))

while True:
    event, values = window.read(timeout=2000)

    window['clock'].update(value=time.strftime('%b %d,%Y %H:%M:%S'))
    print(event)
    print(values)
    print(values['todos'])

    match event:
        case "Add":


            todos = functions.get_todos()
            newtodo = values['todo'] + '\n'
            todos.append(newtodo)
            functions.writeTodos(todos)

        case 'Edit':
            try:
                todoToEdit = values['todos'][0]
                newTodo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todoToEdit)
                todos[index] = newTodo
                functions.writeTodos(todos)
                window['todos'].update(values=todos,font=('Verdana', 21))
            except IndexError:
                gl.popup('Please select an item first')

        case "Complete":
            try:
                toDoToComplete=values['todos'][0]
                todos=functions.get_todos()
                todos.remove(toDoToComplete)
                functions.writeTodos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                gl.popup('Please select an item to complete',font=('Verdana', 21))

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case gl.WINDOW_CLOSED:
            break
