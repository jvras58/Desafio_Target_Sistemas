"""Tela Tarefa 4: Cálculo da Representação Percentual por Estado."""

import streamlit as st
import pandas as pd
import altair as alt
from utils.functions.percentual import (
    calcular_percentual,
    calcular_soma,
)
from utils.load import load_dataset, load_toml


labels = load_toml('ui_labels')


def load_data():
    data = load_dataset('dados')
    return data


data = load_data()
soma = calcular_soma(data)
percentual = calcular_percentual(data)

# Converte os dados percentuais em um DataFrame para visualização
df_percentual = pd.DataFrame(percentual.items(), columns=['Estado', 'Percentual'])

def Visualize() -> None:
    """Função para obter as visualizações da representação percentual."""

    col = st.columns(1)[0]
    total = soma.get('Total', 0)
    col.metric("Somatório dos valores de faturamento", f"{total:,.2f}")

    st.subheader("Representação Percentual por Estado (Tabela)")
    st.table(df_percentual)
    
    st.subheader("Representação Percentual por Estado (Gráfico)")
    chart = alt.Chart(df_percentual).mark_bar().encode(
        x=alt.X('Estado', sort='-y'),
        y='Percentual',
        color='Estado',
        tooltip=['Estado', 'Percentual']
    ).properties(
        width=600,
        height=400
    )
    
    st.altair_chart(chart)

def show_page() -> None:
    """Mostra a página Tarefa 4."""
    
    # Título e descrição da tarefa
    st.title(labels['tarefa_4']['titulo'])
    st.write(labels['tarefa_4']['descricao'])
    
    # Exibe a função de visualização
    Visualize()
