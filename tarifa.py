
class Tarifa:

    def __init__(self,dddOrigem,dddDestino,tarifa):
        self.dddOrigem = dddOrigem
        self.dddDestino = dddDestino
        self.tarifa = tarifa

    def simularCusto(self, duracao):
        return float(self.tarifa) * duracao

    def isAplicavel(self,origem, destino):
        if(self.dddOrigem == origem and self.dddDestino == destino):
            return True
        else:
            return False
