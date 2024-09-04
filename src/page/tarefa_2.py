"""Tela Tarefa 2: Verificação de Número na Sequência de Fibonacci."""

from utils.functions.fibonacci import e_fibonacci_num
import streamlit as st
from utils.load import load_toml


labels = load_toml('ui_labels')

def fibonacci_visualize() -> None:
    """Visualização do Número na Sequência de Fibonacci."""

    # Inputs do usuário
    numero = st.number_input("Informe um número", min_value=0, value=0)

    # Botão para verificar o número
    if st.button("Verificar Número"):
        if e_fibonacci_num(numero):
            st.success(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            st.error(f"O número {numero} não pertence à sequência de Fibonacci.")

def show_page() -> None:
    """Mostra a página Tarefa 1."""
    
    # Título e descrição
    st.title(labels['tarefa_2']['titulo'])
    st.write(labels['tarefa_2']['descricao'])
    
    # Exibe a funcionalidade visualização de número na sequência de Fibonacci
    fibonacci_visualize()
