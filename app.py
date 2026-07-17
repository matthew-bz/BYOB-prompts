import pandas as pd
import math
import csv
import random
from random import shuffle
import streamlit as st


def generate_prompt():
	df = pd.read_csv('BYOBook.csv', sep=",", header=1)

	#print(df.head())
	prompt_list = df['Card'].tolist()
	#print(prompt_list)
	def pick_prompt():
    return random.choice(prompt_list)
return pick_prompt()

st.title("BYOBook: prompt generator")
st.write("Prompts for the game BYOBook")

prompt = pick_prompt()
st.info(f"{prompt}")


if st.button("Generate Another"):
    st.rerun()