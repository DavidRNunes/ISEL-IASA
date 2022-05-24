from ecr import Hierarquia

from .aproximar.aproximar_alvo import AproximarAlvo
from .evitar.evitar_obst import EvitarObst
from .explorar.explorar import Explorar


class Recolher(Hierarquia):
    """
    Classe que herda as propriedades da classe Hierarquia que por sua vez
    herda as propriedades da classe abstrata ComportComp, implementando os
    métodos das superclasses traduz-se no comportamento composto que engloba os
    comportamentos AproximarAlvo, EvitarObst e Explorar

    Permite ao agente activar cada comportamento de acordo com o ambiente que o
    rodeia e de acordo com a hierarquia pré-definida para cada um deles, ou seja,
    quando é ativado o comportamento Recolher, o agente executa os comportamentos
    inseridos neste comportamento com o objetivo de recolher todos os alvos:
    Explora o ambiente em busca de alvos evitando as paredes (EvitarObst) e
    aproxima-se dos alvos quando deteta um alvo (AproximarAlvo) com o objetivo
    de o recolher
    """

    def __init__(self):
        """
        Método construtor da classe Recolher

        Implementa o método construtor da classe abstrata ComportComp fornecendo
        a lista de comportamentos que constituem o comportamento Recolher
        """
        super().__init__([
            AproximarAlvo(),
            EvitarObst(),
            Explorar()
        ])
