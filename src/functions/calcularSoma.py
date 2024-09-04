"""Módulo para calcular a soma dos números inteiros de 1 até um índice informado"""

def calcular_soma(indice: int, soma: int = 0, k: int = 0) -> int:
    """Função para calcular a soma dos números inteiros de 1 até um índice informado"""
    while k < indice:
        k += 1
        soma += k
    return soma
