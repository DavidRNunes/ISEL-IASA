
from controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from controlo_react.reaccoes.resposta.resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao


class EvitarObst(Hierarquia):
    """
    Classe que implementa a classe Hierarquia e permite ao agente evitar os
    obstáculos que se encontram no ambiente, nomeadamente as paredes
    """

    def __init__(self):
        super().__init__([
            EvitarDir(direccao, RespostaEvitar(direccao)) for direccao in list(Direccao)
        ])