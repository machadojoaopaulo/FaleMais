from planoMais import PlanoMais

class PlanoMais120(PlanoMais):

    def __init__(self, tarifas):
        super().__init__(120, tarifas, 1.1)
