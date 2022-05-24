from heapq import heappop, heappush

from .aval.avaliador import Avaliador
from .fronteira import Fronteira


class FronteiraPrioridade(Fronteira):
    """
    Classe que herda os métodos da classe fronteira e implementa alterações de
    forma a criar uma fronteira em função de um avaliador de prioridade dos nós

    A fronteira prioridade consiste em listar os nós na lista da fronteira de
    exploração em função de uma avaliação fornecida, seja ela em função do custo
    dos nós, profundidade, ou outra avaliação implementada. Os elementos são
    adicionados a uma heap queue que permite obter os elementos mais prioritários
    da lista, ou seja, os com menor valor, sem alterar a estrutura da lista

    @param avaliador: função que permite obter a prioridade dos nós
    @method inserir: implementação do método inserir da fronteira prioridade - 
        nós são adicionados à lista mantendo-a invariável
    @method remover: permite obter o nó prioritário da lista da fronteira
    """

    def __init__(self, avaliador):
        """
        Método construtor da fronteira prioridade, guarda a variável do
        avaliador que permite obter a prioridade dos nós e chama a superclasse
        """
        self._avaliador = avaliador
        super().__init__()

    def inserir(self, no):
        """
        Método que permite colocar nós na lista sem alterar a sua estrutura

        @param no: nó que se pretende adicionar à lista da fronteira
        """
        prioridade_no = self._avaliador.prioridade(no)
        heappush(self._nos, (prioridade_no, no))

    def remover(self):
        """
        Método que obtém o nó mais prioritário da lista da fronteira

        @returns: nó prioritário em função do que foi definido pelo avaliador
        """
        _, no = heappop(self._nos)
        return no
