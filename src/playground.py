"""Módulo EntryPoint da aplicação"""

from functions.calcularSoma import calcular_soma
from functions.fibonacci import e_fibonacci_num
import streamlit as st


st.set_page_config(page_title='Playground - Desafio')


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
    st.subheader("Tarefa 2: Verificação de Número na Sequência de Fibonacci")

    numero = st.number_input("Informe um número", min_value=0, value=0)

    if st.button("Verificar Número"):
        if e_fibonacci_num(numero):
            st.write(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            st.write(f"O número {numero} não pertence à sequência de Fibonacci.")


elif opcao == "3":
    st.subheader("A3")
    
