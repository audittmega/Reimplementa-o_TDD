class CalculadoraIR:
    def __init__(self):
        self.total_rendimentos = 0
        self.numero_dependentes = 0

    def cadastrar_rendimento(self, valor):
        self.total_rendimentos += valor

    def get_total_rendimentos(self):
        return self.total_rendimentos

    def get_previdencia_oficial(self):
        previdencia = self.total_rendimentos * 0.10
        return min(previdencia, 700)

    def cadastrar_dependentes(self, numero):
        self.numero_dependentes = numero

    def get_deducao_dependentes(self):
        return self.numero_dependentes * 189.59
