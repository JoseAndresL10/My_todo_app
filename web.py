import streamlit as st
import functions
st.set_page_config(layout="wide")

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title('My TODO app')
st.subheader('Esta página te ayudará a ser más productivo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:                         #SI ESTA MARCADO
        todos.pop(index)                #ELIMINAMOS DE LA LISTA EL TODO
        functions.write_todos(todos)   #UPDATE EL ARCHIVO TXT
        del st.session_state[todo]  #LO ELIMINAMOS DEL DICCIONARIO
        st.rerun() #COMO SI RECARGASRAS LA PÁGINA AUTOMÁTICAMENTE

st.text_input(label = "", placeholder = "Enter a text", key = "new_todo", on_change = add_todo)

st.session_state

