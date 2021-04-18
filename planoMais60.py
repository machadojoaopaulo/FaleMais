from planoMais import PlanoMais

class PlanoMais60(PlanoMais):

    def __init__(self, tarifas):
        super().__init__(60, tarifas, 1.1)
