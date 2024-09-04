"""Módulo para verificar se um número pertence à sequência de Fibonacci"""

"""
https://www.bosontreinamentos.com.br/logica-de-programacao/algoritmo-para-verificar-se-um-numero-pertence-a-serie-de-fibonacci/
"""

def fibonacci_sequencia(num_max: int) -> list:
    """
    Gera uma sequência de Fibonacci até um determinado número máximo.

    Parametros:
    num_max (int): O número máximo até o qual a sequência de Fibonacci deve ser gerada.

    Returns:
    list: A sequência de Fibonacci como uma lista de inteiros.

    """
    sequencia = [0, 1]
    while sequencia[-1] < num_max:
        prox_valor = sequencia[-1] + sequencia[-2]
        sequencia.append(prox_valor)
    return sequencia

def e_fibonacci_num(numero: int) -> bool:
    """
    Verifica se um determinado número é um número de Fibonacci.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        bool: Verdadeiro se o número for um número de Fibonacci, falso caso contrário.
    """

    fibonacci_seq = fibonacci_sequencia(numero)
    return numero in fibonacci_seq
