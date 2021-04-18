from tarifa import Tarifa
from plano import Plano
from planoMais120 import PlanoMais120
from planoMais60 import PlanoMais60
from planoMais30 import PlanoMais30
from tarifaDao import TarifaDao

tarifaDao = TarifaDao()

planoSem = Plano(tarifaDao.getTarifas())
plano30 = PlanoMais30(tarifaDao.getTarifas())
plano60 = PlanoMais60(tarifaDao.getTarifas())
plano120 = PlanoMais120(tarifaDao.getTarifas())

print("Origem: 011 , Destino: 016, Duração: 20")
print("Plano 30: {}".format(plano30.simularCusto(11,16,20)))
print("Sem Plano Mais: {}".format(planoSem.simularCusto(11,16,20)))

print("Origem: 011 , Destino: 017, Duração: 80")
print("Plano 60: {}".format(plano60.simularCusto(11,17,80)))
print("Sem Plano Mais: {}".format(planoSem.simularCusto(11,17,80)))

print("Origem: 018 , Destino: 011, Duração: 200")
print("Plano 120: {}".format(plano120.simularCusto(18,11,200)))
print("Sem Plano Mais: {}".format(planoSem.simularCusto(18,11,200)))

print("Origem: 018 , Destino: 017, Duração: 100")
print("Plano 30: {}".format(plano30.simularCusto(18,17,100)))
print("Sem Plano Mais: {}".format(planoSem.simularCusto(18,17,100)))