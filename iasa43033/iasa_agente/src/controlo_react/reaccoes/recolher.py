from controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from controlo_react.reaccoes.explorar.explorar import Explorar
from ecr.hierarquia import Hierarquia


class Recolher(Hierarquia):
    """
    Classe correspondente ao comportamento composto Recolher que engloba os
    comportamentos AproximarAlvo, EvitarObst e Explorar, permitindo ao agente
    alternar entre os vários comportamentos neste comportamento de acordo com
    o nível hieráriquico definido

    Esta classe implementa a classe Hierarquia que por sua vez implementa a
    classe ComportComp
    """

    def __init__(self):
        """
        Método construtor da classe Recolher

        Implementa o método construtor da classe abstrata ComportComp
        fornecendo a lista de comportamentos que constituem o comportamento
        Recolher
        """
        super().__init__([
            AproximarAlvo(),
            EvitarObst(),
            Explorar()
        ])
