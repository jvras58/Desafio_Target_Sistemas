"""Tela Tarefa 3: Análise de Faturamento Diário."""

import streamlit as st
import pandas as pd
import altair as alt
from utils.functions.faturamento import (
    calcular_faturamento_mensal,
    calcular_faturamento_superior_faturamento_mensal, 
    calcular_menor_faturamento_mensal, 
    calcular_media_faturamento_mensal
)
from utils.load import load_json, load_toml


labels = load_toml('ui_labels')


def load_faturamento():
    faturamento = load_json('faturamento_mensal')
    return faturamento


faturamento = load_faturamento()


maior_faturamento = calcular_faturamento_mensal(faturamento)
menor_faturamento = calcular_menor_faturamento_mensal(faturamento)
media_faturamento = calcular_media_faturamento_mensal(faturamento)
superior_media_faturamento = calcular_faturamento_superior_faturamento_mensal(faturamento, media_faturamento)

def Visualize() -> None:
    """Função para obter as visualizações do Faturamento."""

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Maior Faturamento", f"R$ {maior_faturamento:,.2f}")
    col2.metric("Menor Faturamento", f"R$ {menor_faturamento:,.2f}")
    col3.metric("Média de Faturamento", f"R$ {media_faturamento:,.2f}")
    col4.metric("Dias Fatur. Superior à Média", len(superior_media_faturamento))

    df_faturamento = pd.DataFrame(faturamento)
    
    df_faturamento = df_faturamento.sort_values(by="dia")
    
    st.line_chart(df_faturamento.set_index("dia")["valor"])
    
    chart = alt.Chart(df_faturamento).mark_bar().encode(
        x=alt.X('dia:O', title='Dia'),
        y=alt.Y('valor:Q', title='Faturamento (R$)'),
        tooltip=['dia', 'valor']
    ).properties(
        title="Faturamento Diário"
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    st.write("Tabela de Faturamento Diário")
    st.dataframe(df_faturamento)

def show_page() -> None:
    """Mostra a página Tarefa 3."""
    
    # Título e descrição
    st.title(labels['tarefa_3']['titulo'])
    st.write(labels['tarefa_3']['descricao'])
    
    # Exibe a função de visualização
    Visualize()
