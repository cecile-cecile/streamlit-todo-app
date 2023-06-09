import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(
    page_title="My TODO App",
    page_icon=":memo"
)


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My TODO App")
st.subheader("Things to do")
st.markdown(":sunglasses: Let's cross these off!")

st.text_input(label="Add a new TODO:", placeholder="",
              on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        # Update todos list
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# st.session_state
