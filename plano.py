
class Plano:
    def __init__(self, tarifas):
        self.tarifas = tarifas

    def simularCusto(self, origem, destino, duracao):
        tarifa = self.buscaTarifa(origem, destino)

        if(tarifa is not None):
            return tarifa.simularCusto(duracao)
        else:
            return None

    def buscaTarifa(self, origem, destino):
        for tarifa in self.tarifas:
            if(tarifa.isAplicavel(origem,destino)):
                return tarifa
            