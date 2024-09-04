"""Tela Tarefa 4: Cálculo da Representação Percentual por Estado."""

from pprint import pprint
import streamlit as st
# import pandas as pd
# import altair as alt
from utils.functions.percentual import (
    calcular_percentual,
)
from utils.load import load_dataset, load_toml


labels = load_toml('ui_labels')


def load_data():
    data = load_dataset('dados')
    return data


data = load_data()


percentual = calcular_percentual(data)

#TODO: Implementar a função de visualização
#TODO: Implementar Soma dos valores de faturamento dos estados


def Visualize() -> None:
    """Função para obter as visualizações da representação percentual."""
    pprint(percentual)

def show_page() -> None:
    """Mostra a página Tarefa 4."""
    
    # Título e descrição
    st.title(labels['tarefa_4']['titulo'])
    st.write(labels['tarefa_4']['descricao'])
    
    # Exibe a função de visualização
    Visualize()
