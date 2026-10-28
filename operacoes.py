"""
Módulo de Operações Matemáticas
Contém todas as funções de cálculo da calculadora.
"""

def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a diferença entre dois números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de dois números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Retorna o quociente da divisão de a por b.
    Levanta ValueError caso o divisor b seja zero.
    """
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def potencia(base: float, expoente: float) -> float:
    """Retorna a base elevada ao expoente."""
    return base ** expoente


def porcentagem(valor_base: float, percentual: float) -> float:
    """
    Calcula a porcentagem de um determinado valor.
    Exemplo: porcentagem(200, 15) calcula 15% de 200 = 30.
    """
    return (valor_base * percentual) / 100
