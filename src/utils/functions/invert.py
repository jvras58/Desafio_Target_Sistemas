"""Módulo para Inverter a String."""

"""
https://acervolima.com/string-reversa-em-python-5-maneiras-diferentes/
"""
def invert_string(input_string: str) -> str:
    """Inverte a string."""
    inverted = ""
    for char in input_string:
        inverted = char + inverted
    return inverted
