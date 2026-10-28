"""
Testes Unitários da Calculadora Modular
Verifica todas as funções matemáticas do módulo operacoes.py,
incluindo casos normais e casos de erro/exceção.
"""

import unittest
from operacoes import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    potencia,
    porcentagem
)


class TestOperacoesCalculadora(unittest.TestCase):

    # 1. Testes de Adição
    def test_somar_positivos(self):
        self.assertEqual(somar(10, 5), 15)

    def test_somar_negativos(self):
        self.assertEqual(somar(-10, 4), -6)

    def test_somar_decimais(self):
        self.assertAlmostEqual(somar(2.5, 3.1), 5.6)

    # 2. Testes de Subtração
    def test_subtrair_positivos(self):
        self.assertEqual(subtrair(10, 4), 6)

    def test_subtrair_resultado_negativo(self):
        self.assertEqual(subtrair(5, 12), -7)

    # 3. Testes de Multiplicação
    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(6, 7), 42)

    def test_multiplicar_por_zero(self):
        self.assertEqual(multiplicar(99, 0), 0)

    def test_multiplicar_decimais(self):
        self.assertEqual(multiplicar(2.5, 4), 10.0)

    # 4. Testes de Divisão
    def test_dividir_exata(self):
        self.assertEqual(dividir(20, 4), 5.0)

    def test_dividir_fracionaria(self):
        self.assertAlmostEqual(dividir(10, 3), 3.3333333333333335)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError) as context:
            dividir(10, 0)
        self.assertIn("Não é possível dividir por zero", str(context.exception))

    # 5. Testes de Potência
    def test_potencia_inteira(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_potencia_expoente_zero(self):
        self.assertEqual(potencia(5, 0), 1)

    def test_potencia_fracionaria_raiz(self):
        self.assertEqual(potencia(4, 0.5), 2.0)

    # 6. Testes de Porcentagem
    def test_porcentagem_padrao(self):
        # 15% de 200 deve ser 30.0
        self.assertEqual(porcentagem(200, 15), 30.0)

    def test_porcentagem_metade(self):
        # 50% de 80 deve ser 40.0
        self.assertEqual(porcentagem(80, 50), 40.0)

    def test_porcentagem_zero(self):
        # 0% de 500 deve ser 0.0
        self.assertEqual(porcentagem(500, 0), 0.0)

    def test_porcentagem_total(self):
        # 100% de 75 deve ser 75.0
        self.assertEqual(porcentagem(75, 100), 75.0)


if __name__ == "__main__":
    print("Iniciando bateria de testes automatizados da calculadora...\n")
    unittest.main(verbosity=2)
