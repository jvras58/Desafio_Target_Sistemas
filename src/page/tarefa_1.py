"""Tela Tarefa 1: Cálculo da Soma."""

import streamlit as st
from utils.load import load_toml
from utils.functions.calcularSoma import calcular_soma

labels = load_toml('ui_labels')

def calculo_soma() -> None:
    """Calcula a soma de um número inteiro"""
    
    # Inputs do usuário
    indice = st.number_input("Valor de INDICE", min_value=1, value=13)
    soma = st.number_input("Valor inicial de SOMA", min_value=0, value=0)
    k = st.number_input("Valor inicial de K", min_value=0, value=0)

    # Botão para calcular a soma
    if st.button("Calcular SOMA"):
        resultado = calcular_soma(indice, soma, k)
        st.success(f"O valor final de SOMA é: {resultado}")

def show_page() -> None:
    """Mostra a página Tarefa 1."""
    
    # Título e descrição
    st.title(labels['tarefa_1']['titulo'])
    st.write(labels['tarefa_1']['descricao'])
    
    # Exibe a funcionalidade de cálculo da soma
    calculo_soma()
