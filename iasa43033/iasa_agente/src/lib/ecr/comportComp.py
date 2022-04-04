from abc import ABC, abstractmethod
from .comportamento import Comportamento

"""
Classe abstrata que establece a possibilidade de formar comportamentos
compostos, ou seja, comportamentos que englobam neles outros comportamentos
permitindo assim criar um comportamento que permite ao agente reagir de
formas diferentes perante o ambiente. Esta implementação traduz-se na
possibilidade de perante uma percepção ser efectuada uma decisão da
prioridade de acção a tomar pelo agente.
"""
class ComportComp(Comportamento, ABC):

    """
    Método construtor da classe que guarda a variável dos comportamentos
    da classe composta
    """
    def __init__(self, comportamentos):
        self._comportamentos = comportamentos

    """
    Método que activa a detecção de estímulos dos vários comportamentos
    do comportamento composto. 
    """
    def activar(self, percepcao):
        accoes = []
    
        for i in range(len(self._comportamentos)):
            accao = self._comportamentos[i].activar(percepcao)
            if accao is not None:
                accoes.append(accao)

        if accoes:
            if len(accoes) > 1:
                return self.seleccionar_accao(accoes)
                
            return accoes[0]

    """
    Método abstrato que permite selecionar uma acção por entre
    as várias acções dos comportamentos do comportamento composto.
    """
    @abstractmethod
    def seleccionar_accao(self, accoes):
        """Seleciona accao por hierarquia ou prioridade"""