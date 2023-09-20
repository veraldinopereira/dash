import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu Site Deus")

with st.container():
    st.subheader("Meu senhor ajuda")
    st.title("Dash")
    st.write("Infor")
    st.write("Quer aprender [clique aqui](https://docs.streamlit.io/library/get-started/create-an-app)")

with st.container():
    st.write("---")
    dados=pd.read_csv("resultados.csv")
    st.area_chart(dados, x="Data",y="Contratos")

with st.container():
    st.write("---")
    st.subheader("Ja acabou jessica")
    st.write("---")