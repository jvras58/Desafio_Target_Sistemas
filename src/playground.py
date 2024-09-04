"""Módulo EntryPoint da aplicação"""

from functions.calcularSoma import calcular_soma
import streamlit as st


st.title("Playground - Desafio")

st.sidebar.header("Escolha uma Tarefa")
opcao = st.sidebar.selectbox(
    "Tarefas",
    ("1", "2", "3")
)

if opcao == "1":
    st.subheader("Tarefa 1: Cálculo da Soma")

    indice = st.number_input("Valor de INDICE", min_value=1, value=13)
    soma = st.number_input("Valor inicial de SOMA", min_value=0, value=0)
    k = st.number_input("Valor inicial de K", min_value=0, value=0)

    if st.button("Calcular SOMA"):
        resultado = calcular_soma(indice, soma, k)
        st.write(f"O valor final de SOMA é: {resultado}")


elif opcao == "2":
    st.subheader("A2")

elif opcao == "3":
    st.subheader("A3")
    
