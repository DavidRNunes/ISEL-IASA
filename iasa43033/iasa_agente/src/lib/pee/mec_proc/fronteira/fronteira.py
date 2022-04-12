from abc import ABC, abstractmethod


class Fronteira(ABC):
    """
    
    """

    def __init__(self):
        """
        criar lista de nós
        """
        self._nos = []
    
    def vazia(self):
        """
        verifica se a fronteira está vazia
        @returns: valor booleano que permite saber se a lista está
            vazia, retorna true se estiver vazia
        """
        return not len(self._nos)

    @abstractmethod
    def inserir(self, no):
        """
        
        """

    def remover(self):
        """
        remove o primeiro nó da fronteira e retorna-o
        @returns: nó
        """
        return self._nos.pop(0)