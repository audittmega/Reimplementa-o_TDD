import unittest
from calculadora_ir import CalculadoraIR

class TestCalculadoraIR(unittest.TestCase):
    def test_cadastro_rendimentos_red(self):
        calc = CalculadoraIR()
        calc.cadastrar_rendimento(5000)
        self.assertEqual(calc.get_total_rendimentos(), 5000)

    def test_calculo_previdencia_red(self):
        calc = CalculadoraIR()
        calc.cadastrar_rendimento(7000) # Adicionando rendimento para o cálculo da previdência
        self.assertEqual(calc.get_previdencia_oficial(), 700)

    def test_deducao_dependentes_red(self):
        calc = CalculadoraIR()
        calc.cadastrar_dependentes(1)
        self.assertEqual(calc.get_deducao_dependentes(), 189.59)

if __name__ == '__main__':
    unittest.main()
