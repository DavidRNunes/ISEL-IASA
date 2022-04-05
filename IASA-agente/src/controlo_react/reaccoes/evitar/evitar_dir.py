
from controlo_react.reaccoes.evitar.estimulo_obst import EstimuloObst
from controlo_react.reaccoes.resposta.resposta_evitar import RespostaEvitar
from ecr.reaccao import Reaccao


class EvitarDir(Reaccao):
    """
    Classe que implementa a Reaccao e permite ao agente evitar os obstáculos
    """

    def __init__(self, direccao, resposta):
        super().__init__(EstimuloObst(direccao), resposta)