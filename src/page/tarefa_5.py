"""Tela Tarefa 5: Inversão de String."""

from utils.functions.invert import invert_string
import streamlit as st
from utils.load import load_toml

labels = load_toml('ui_labels')

def invert_caracter() -> None:
    """Função para inverter String."""

    # Inputs do usuário
    string = st.text_input("Digite uma string para inverter:", "Exemplo")

    # Botão para inverter a string
    if st.button("Inverter"):
        inverted_string = invert_string(string)
        st.success(f"String invertida: {inverted_string}")

def show_page() -> None:
    """Mostra a página Tarefa 5."""
    
    # Título e descrição
    st.title(labels['tarefa_5']['titulo'])
    st.write(labels['tarefa_5']['descricao'])
    
    # Exibe a função 
    invert_caracter()
