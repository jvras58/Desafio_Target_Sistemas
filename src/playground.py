"""Módulo EntryPoint da aplicação"""

import streamlit as st

# Page config
st.set_page_config(page_title='Playground - Desafio')

import page.home as home_page
import page.tarefa_1 as tarefa_1
import page.tarefa_2 as tarefa_2
import page.tarefa_3 as tarefa_3
import page.tarefa_5 as tarefa_5

from utils.load import load_image


def show_page() -> None:
    """Mostra a página HOME e menu do dashboard."""
    st.sidebar.image(load_image('logo-target.png'), use_column_width=True)

    pages = {
        '🏠 Home': home_page,
        '📄 Cálculo da Soma': tarefa_1,
        '📄 N! na Sequência de Fibonacci': tarefa_2,
        '📄 Análise de Faturamento Diário': tarefa_3,
        '📄 Inverter String': tarefa_5,
    }

    st.sidebar.title('Menu')
    selection = st.sidebar.radio('Go to', list(pages.keys()))

    page = pages[selection]
    page.show_page()


if __name__ == '__main__':
    show_page()
