import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import Smartphone

engine = create_engine("sqlite:///mydatabase.sqlite")

makeSession = sessionmaker(bind=engine)
sess = makeSession()

st.title('Add New SmartPhone Data')
st.markdown("---")

