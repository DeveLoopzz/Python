##A currency conversion calculator
##Given a Dollar cuantity we need to convert it to euros and print it on de console.

import streamlit as st

st.title("Dollar to Euros conversor")

dollars = st.number_input("Dollars: ") ##Getting the dollars from the user

euros = dollars * 1.1

st.button("Process", on_click=print("Here you will see the result"))
print(euros)