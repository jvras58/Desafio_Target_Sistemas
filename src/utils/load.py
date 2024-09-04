"""Funções utilitárias para carregar arquivos."""

from pathlib import Path
from typing import Any

import json
import streamlit as st
import toml
from PIL import Image


def get_project_root() -> str:
    """Retorna o caminho raiz do projeto.

    Returns
    -------
    str
        Caminho raiz do projeto.

    """
    return str(Path(__file__).parent.parent.parent)


def load_image(image_name: str) -> Image:
    """Exibe uma imagem.

    Parameters
    ----------
    image_name : str
        Caminho local da imagem.

    Returns
    -------
    Image
        Imagem a ser exibida..

    """
    return Image.open(
        Path(get_project_root()) / f'src/assets/imgs/{image_name}',
    )


def load_toml(toml_file: str) -> dict[Any, Any]:
    """Carrega o arquivo toml de configuração do sistema de arquivos do usuário como um dicionário.

    Parameters
    ----------
    toml_file : str
        Arquivo de configuração toml carregado..

    Returns
    -------
    dict
        Dicionário de configuração carregado.

    """
    toml_loaded = toml.load(
        Path(get_project_root())
        / f'src/assets/lang/{toml_file}.toml',
    )

    return dict(toml_loaded)


@st.cache_data
def load_json(json_name: str) -> dict:
    """Carrega um conjunto de dados de um arquivo json.

    Parameters
    ----------
    json_name : str
        Nome do conjunto de dados a ser carregado.

    Returns
    -------
    dict
        Conjunto de dados carregado.

    """
    with open(Path(get_project_root()) / f'src/data/{json_name}.json', 'r') as file:
        data = json.load(file)
    return data
