import streamlit as st
import functions

if "todos" not in st.session_state:
    st.session_state.todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:
        st.session_state.todos.append(todo + "\n")
        functions.write_todos(st.session_state.todos)
        st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

todos_to_remove = []
for index, todo in enumerate(st.session_state.todos):
    if st.checkbox(todo.strip(), key=f"todo_{index}"):
        todos_to_remove.append(index)

for index in reversed(todos_to_remove):
    st.session_state.todos.pop(index)
functions.write_todos(st.session_state.todos)

st.text_input(
    label="Add todo",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo",
    label_visibility="collapsed"
)
