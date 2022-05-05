from abc import ABC, abstractmethod


class Avaliador(ABC):
    """
    Interface abstrata que representa o avaliador de nós

    Permite considerar o nó fornecido e avaliar a prioridade do mesmo
    em função do custo do nó

    @method prioridade: método abstrato que permite auferir a prioridade
        do nó em função do custo do mesmo
    """

    @abstractmethod
    def prioridade(self, no):
        """
        Método abstrato que quando implementado obtém a prioridade do nó
        em função do seu custo

        @param no: nó que se pretende avaliar        
        @returns: valor da prioridade do nó em double
        """
