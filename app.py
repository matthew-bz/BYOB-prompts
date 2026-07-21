import pandas as pd
import random
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv('BYOBook.csv', sep=",", header=1)

df = load_data()

st.title("BYOBook: prompt generator")
st.write("Prompts for the game BYOBook")

categories = ["All"] + sorted(df['Category'].dropna().unique().tolist())

selected_category = st.selectbox("Select a Category", categories)

if selected_category == "All":
    filtered_df = df
else:
    filtered_df = df[df['Category'] == selected_category]

if not filtered_df.empty:
    prompt_list = filtered_df['Card'].tolist()
    prompt = random.choice(prompt_list)
    st.info(f"{prompt}")
else:
    st.warning("No prompts found for this category.")

if st.button("Generate Another"):
    st.rerun()