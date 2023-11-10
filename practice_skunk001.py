import streamlit as st

import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

st.title("#Password Generator Project")
st.markdown("Welcome to the Password Generator!")

with st.form(key="input_form"):
    nr_letters = st.number_input("How many letters would you like in your password?",0)
    nr_symbols = st.number_input("How many symbols would you like?",0)
    nr_numbers = st.number_input("How many numbers would you like?",0)

    submit_botton = st.form_submit_button("Go!")
    cancel_botton = st.form_submit_button("Cancel")
    
    pw = []
    
    for num in range(1, nr_letters + 1):
        pw.append(random.choice(letters))
    
    for num in range(1, nr_symbols + 1):
        pw.append(random.choice(symbols))
    
    for num in range(1, nr_numbers + 1):
        pw.append(random.choice(numbers))
    
    random.shuffle(pw)
    
    ff2 = ""
    for num in pw:
        ff2 += num

    if submit_botton:
        st.text(f"Your uncrackable password is: {ff2}.")

