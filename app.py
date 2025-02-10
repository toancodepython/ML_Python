import streamlit as st

st.title('Hello Streamlit')


name = st.text_input('Enter your name')

if st.button('Say Hello'):
    st.write(f'Hello, {name}!')
    
number = st.slider('Pick a numnber', 0, 100)
st.write(f'You selected: {number}')
