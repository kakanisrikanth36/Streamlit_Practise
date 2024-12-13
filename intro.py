import streamlit as st

st.title("My web application")

st.header("My first app", divider="green")

st.subheader("Favourite colour")

st.write("Learning streamlit for the first time")

agree = st.checkbox("I agree with the terms and conditions.")

if agree:
    st.write("Great")
else:
    st.write("Please read the terms and conditions and provide your acceptance")

genre = st.radio("Whats your fav genre?", ["Comedy", "Drama", "Documentary"])

if genre == "Comedy":
    st.write("You are a comedy person")
elif genre == "Drama":
    st.write("You are a dramatic person")
elif genre == "Documentary":
    st.write("You are a documentary person")
