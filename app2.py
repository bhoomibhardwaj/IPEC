import streamlit as st
st.titile("my age and city app")
age-st.number_input("enter your age",1,100)
city=st.selectbox("select your city",["mumbai","delhi","bangalore","chennai"])
if st.button("submit"):
    st.write("your age is",age)
    st.write("your city is",city)