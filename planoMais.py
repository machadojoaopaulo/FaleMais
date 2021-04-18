from plano import Plano
class PlanoMais(Plano):

    def __init__(self, minutosInclusos, tarifas, acrescimo):
        super().__init__(tarifas)
        self.minutosInclusos = minutosInclusos
        self.acrescimo = acrescimo

    def calcularMinutosExedentes(self,duracao):
        return duracao - self.minutosInclusos

    def simularCusto(self, origem, destino, duracao):
        if(super().buscaTarifa(origem,destino) is None):
            return None

        duracaoFinal = self.calcularMinutosExedentes(duracao)

        if(duracaoFinal <= 0):
            return 0
        else:
            return super().simularCusto(origem, destino, duracaoFinal*self.acrescimo)