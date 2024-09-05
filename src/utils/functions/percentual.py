"""Modulo com Funções de Calculo de percentual / Soma."""

import streamlit as st

@st.cache_data
def calcular_percentual(dados: dict) -> dict:
    """Calcula o percentual de cada valor em relação ao total."""

    total = dados['Valor'].sum()
    
    dados['Percentual'] = (dados['Valor'] / total) * 100
    
    percentuais = dados.set_index('Estado')['Percentual'].to_dict()
    
    return percentuais

@st.cache_data
def calcular_soma(dados: dict) -> dict:
    """Calcula a soma dos valores de faturamento dos estados."""
    
    soma_total = dados['Valor'].sum()
    
    somas = dados.set_index('Estado')['Valor'].to_dict()
    
    somas['Total'] = soma_total
    
    return somas
