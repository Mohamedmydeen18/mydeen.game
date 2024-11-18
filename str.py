import streamlit as st
import random

# Initialize the game
if 'number' not in st.session_state:
    st.session_state['number'] = random.randint(1, 10)
    st.session_state['attempts'] = 0

st.title("Number Guessing Game")

# Input from the user
guess = st.number_input('Guess the number (between 1 and 10)', min_value=1, max_value=10, step=1)
if st.button('Submit'):
    st.session_state['attempts'] += 1
    if guess < st.session_state['number']:
        st.write('Your guess is too low. Try again!')
    elif guess > st.session_state['number']:
        st.write('Your guess is too high. Try again!')
    else:
        st.write(f'Congratulations! You guessed the number in {st.session_state["attempts"]} attempts.')
        st.session_state['number'] = random.randint(1, 10)
        st.session_state['attempts'] = 0

st.write(f'Number of attempts: {st.session_state["attempts"]}')
