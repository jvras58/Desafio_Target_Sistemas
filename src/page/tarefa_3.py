"""Tela Tarefa 3: Análise de Faturamento Diário."""

import streamlit as st
import pandas as pd
import altair as alt
from utils.functions.faturamento import (
    calcular_faturamento_mensal, 
    calcular_menor_faturamento_mensal, 
    calcular_media_faturamento_mensal
)
from utils.load import load_json, load_toml

# Carrega labels de UI
labels = load_toml('ui_labels')

# Função para carregar os dados de faturamento
def load_faturamento():
    faturamento = load_json('faturamento_mensal')
    return faturamento

# Carrega os dados de faturamento
faturamento = load_faturamento()

# Calcula as métricas
maior_faturamento = calcular_faturamento_mensal(faturamento)
menor_faturamento = calcular_menor_faturamento_mensal(faturamento)
media_faturamento = calcular_media_faturamento_mensal(faturamento)

def Visualize() -> None:
    """Função para obter as visualizações do Faturamento."""

    col1, col2, col3 = st.columns(3)
    col1.metric("Maior Faturamento", f"R$ {maior_faturamento:,.2f}")
    col2.metric("Menor Faturamento", f"R$ {menor_faturamento:,.2f}")
    col3.metric("Média de Faturamento", f"R$ {media_faturamento:,.2f}")
    
    # Criando um DataFrame para facilitar a visualização
    df_faturamento = pd.DataFrame(faturamento)
    
    # Ordenando o DataFrame por dia para garantir a visualização correta
    df_faturamento = df_faturamento.sort_values(by="dia")
    
    # Gráfico de linha para mostrar o faturamento diário
    st.line_chart(df_faturamento.set_index("dia")["valor"])
    
    # Gráfico de barras usando Altair para uma visualização alternativa
    chart = alt.Chart(df_faturamento).mark_bar().encode(
        x=alt.X('dia:O', title='Dia'),
        y=alt.Y('valor:Q', title='Faturamento (R$)'),
        tooltip=['dia', 'valor']
    ).properties(
        title="Faturamento Diário"
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    st.dataframe(df_faturamento)

def show_page() -> None:
    """Mostra a página Tarefa 3."""
    
    # Título e descrição
    st.title(labels['tarefa_3']['titulo'])
    st.write(labels['tarefa_3']['descricao'])
    
    # Exibe a função de visualização
    Visualize()
