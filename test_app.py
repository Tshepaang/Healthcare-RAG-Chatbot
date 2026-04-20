import streamlit as st

st.title("🏥 Netcare AI Assistant Test")
st.markdown("This is a test to see if Streamlit works.")

user_input = st.text_input("Type anything:")
if user_input:
    st.write(f"You typed: {user_input}")
