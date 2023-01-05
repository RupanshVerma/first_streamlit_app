import streamlit
import pandas

streamlit.title('New Healthy Dinner')
streamlit.header('Healthy Breakfast Menu')
streamlit.text('🥣Oatmeals')
streamlit.text('🥗Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔Hard Boiled Egg')
streamlit.text('🥑🍞Avocade Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
