import streamlit as st
st.title("simple imput app")
name=st.text_input("enter your name")
if st.button("submit"):
    st.write(f"hello ",name)