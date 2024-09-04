"""Modulo com Funções de Calculo de percentual / Soma."""

import streamlit as st



@st.cache_data
def calcular_percentual(dados: dict) -> dict:
    """Calcula o percentual de cada valor em relação ao total."""
    # Calcula o total dos valores
    total = dados['Valor'].sum()
    
    # Calcula o percentual de cada valor em relação ao total
    dados['Percentual'] = (dados['Valor'] / total) * 100
    
    # Converte para dicionário
    percentuais = dados.set_index('Estado')['Percentual'].to_dict()
    
    return percentuais

#TODO: Implementar Soma dos valores de faturamento dos estados
