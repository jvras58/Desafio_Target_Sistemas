
import streamlit as st


@st.cache_data
def calcular_faturamento_mensal(faturamento):
    """Calcula o faturamento mensal."""
    faturamento = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
    return sum(faturamento)

@st.cache_data
def calcular_menor_faturamento_mensal(faturamento):
    """Calcula o menor faturamento mensal."""
    faturamento = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
    return min(faturamento)

@st.cache_data
def calcular_media_faturamento_mensal(faturamento):
    """Calcula a média do faturamento mensal."""
    faturamento = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
    return sum(faturamento) / len(faturamento)
