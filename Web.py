
import streamlit as st
import functions

todos = functions.get_todos()
# https://github.com/CostinM98/repository/blob/master/WebAppNo.1.py
# https://github.com/CostinM98/repository/master/WebAppNo.1
def add_todo():
    todo_local = st.session_state["new_todo"] + '\n'
    todos.append(todo_local)
    functions.writeTodos(todos)



st.title('My Todo APP')
st.write("This app is to increase your productivity")

st.text_input(label='', placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f'checkbox_{index}')
    if checkbox:
        todos.pop(index)
        functions.writeTodos(todos)
        del st.session_state[f'checkbox_{index}']
        st.experimental_rerun()


