from sae import Controlo
from sae import Simulador
from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.plan_pee import PlanPEE

"""
Teste ao agente usando um controlo de teste
"""
class ControloTeste(Controlo):
    def processar(self, percepcao):
        print("processar")

"""
Teste ao agente usando um controlador reactivo
"""


"""
Teste ao agente usando um controlador deliberativo
"""
planeador = PlanPEE()
controlo = ControloDelib(planeador)


"""
Ativação do controlador
"""
Simulador(4, controlo).executar()
