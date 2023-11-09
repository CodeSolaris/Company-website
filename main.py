import streamlit as st
import pandas as pd
from faker import Faker

fake = Faker()
lorem = Faker("en_US")
st.set_page_config(layout="wide")

st.header("The Best Company")
st.write(lorem.text(max_nb_chars=1000))
st.write("")
st.header("Our Team")
st.write("#")

with open("data.csv") as db_file:
    db = pd.read_csv(db_file, sep=",")

column1, empty_column1, column2, empty_column2, column3 = st.columns(
    [1.5, 0.5, 1.5, 0.5, 1.5]
)


def display_team_members(row):
    st.subheader(row["first name"] + " " + row["last name"])
    st.write(row["role"])
    st.image("images/" + row["image"])

with column1:
    for index, row in db[:4].iterrows():
        display_team_members(row)

with column2:
    for index, row in db[4:8].iterrows():
        display_team_members(row)

with column3:
    for index, row in db[8:].iterrows():
        display_team_members(row)