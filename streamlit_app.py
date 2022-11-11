
import streamlit

streamlit.title("My parents new healthy diner")

streamlit.header("Breakfast")
streamlit.text("Churros con chocolate saludable")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

