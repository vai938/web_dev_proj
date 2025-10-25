import streamlit as st
import task_functions as tf

todos= tf.get_todos()
def add_todo():
    todo= st.session_state["new_todo"]
    todos.append(todo)
    tf.write_todos(todos)


st.title("My Todo App")
st.subheader("This is sub header")
st.write("This app is for text")

for index,todo in enumerate(todos):
    check_box= st.checkbox(todo,key=todo)
    if check_box:
        todos.pop(index)
        tf.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a todo:",placeholder="Add a todo.......",
              on_change=add_todo,key= 'new_todo')