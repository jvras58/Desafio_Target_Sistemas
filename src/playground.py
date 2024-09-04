"""Módulo EntryPoint da aplicação"""

import streamlit as st


st.title(" Playground - Desafio")

st.sidebar.header("Escolha uma Tarefa")

opcao = st.sidebar.selectbox(
    "Tarefas",
    ("1", "2", "3")
)

if opcao == "1":
    st.subheader("A1")

elif opcao == "2":
    st.subheader("A2")

elif opcao == "3":
    st.subheader("A3")
    
