from abc import ABC, abstractmethod


class Problema(ABC):
    """
    Classe representativa de um problema

    Problema de procura consiste nos estados possíveis em que o ambiente
    se pode encontrar, o estado inicial em que se encontra o agente, os
    objetivos (um ou mais), as acções que o agente pode praticar, os
    operadores que descrevem o que a acção faz gerando a transformação
    de estado e o custo de cada acção. A sequência de acções forma um
    caminho e a solução é o caminho que leva o agente do estado inicial
    ao objetivo final.
    """

    def __init__(self, estado_inicial, operadores):
        """
        
        """
        self._estado_inicial = estado_inicial
        self._operadores = operadores

    @abstractmethod
    def objectivo(self, estado):
        """
        
        @returns: boolean
        """