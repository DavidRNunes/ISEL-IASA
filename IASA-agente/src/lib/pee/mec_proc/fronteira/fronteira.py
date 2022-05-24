from abc import ABC, abstractmethod

from ..no import No


class Fronteira(ABC):
    """
    Classe abstrata que representa a fronteira de exploração da árvore

    A fronteira de exploração da árvore de procura consiste nos nós filho
    ainda não expandidos dos nós já anteriormente expandidos, sendo esta
    estrutura de dados o que permite definir a estratégia da procura em
    função da ordenação dos elementos - fronteira LIFO, FIFO ou prioritária.
    Em termos de programação consiste na lista de nós filhos que ainda não
    foram explorados, sendo então adicionados à lista os nós filho do nó em
    estudo quando este é expandido

    @method vazia: método que permite verificar se a fronteira está vazia
    @method inserir: método abstrato implementado em função da fronteira,
        insere um nó na lista da fronteira
    @method remover: método que remove e retorna o último nó da lista
    """

    _nos: list

    def __init__(self):
        """
        Método construtor da classe, inicia a fronteira como uma lista de
        nós vazia
        """
        self._nos = []

    def vazia(self):
        """
        Método que permite verificar se a fronteira se encontra vazia,
        ou seja, se não existem nós na lista

        @returns: True caso a fronteira esteja vazia, False em caso
            negativo
        """
        return not self._nos

    @abstractmethod
    def inserir(self, no):
        """
        Método abstrato implementado em função do tipo de fronteira,
        insere nós na lista da fronteira

        @param no: nó que se pretende inserir na lista da fronteira
        """

    def remover(self):
        """
        Método que permite obter o último nó da lista, removendo-o e
        retornando o seu valor

        No caso da fronteira FIFO este será o nó mais antigo e no caso
        da fronteira LIFO é o nó mais recente

        @returns: nó que se encontra na última posição da lista
        """
        return self._nos.pop()
