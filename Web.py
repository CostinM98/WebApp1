
import streamlit as gl
import functions

todos = functions.get_todos()

def add_todo():
    todo_local = gl.session_state["new_todo"] + '\n'
    todos.append(todo_local)
    functions.writeTodos(todos)



gl.title('My Todo APP')
gl.write("This app is to increase your productivity")

gl.text_input(label='', placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox =gl.checkbox(todo, key=f'checkbox_{index}')
    if checkbox:
        todos.pop(index)
        functions.writeTodos(todos)
        del gl.session_state[f'checkbox_{index}']
        gl.experimental_rerun()


