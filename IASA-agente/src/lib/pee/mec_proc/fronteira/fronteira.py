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
        remove o último nó da fronteira e retorna-o, ou seja, o nó
        do topo da lista, sendo este o nó mais antigo no caso da
        fronteira FIFO e o mais recente no caso da fronteira LIFO
        @returns: nó
        """
        return self._nos.pop(-1)