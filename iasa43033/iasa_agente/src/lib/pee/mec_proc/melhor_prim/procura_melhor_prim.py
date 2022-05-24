from abc import ABC, abstractmethod

from ..fronteira.aval.avaliador import Avaliador
from ..fronteira.fronteira_prioridade import FronteiraPrioridade
from ..procura_grafo import ProcuraGrafo


class ProcuraMelhorPrim(ProcuraGrafo, ABC):
    """
    Classe abstrata que expande sobre a superclasse ProcuraGrafo introduzindo
    o conceito de prioridade entre nós

    Através do uso de um avaliador é obtida uma aproximação geral de qual nó
    deve ser expandido de seguida, em função do resultado devolvido pelo
    avaliador. No fim de cada iteração é avaliado o nó com prioridade mais
    elevada, neste caso com menor custo. É feita uma verificação à redundância
    recorrendo à superclasse ProcuraGrafo mas é ainda tido em conta o valor
    obtido pelo avaliador, que caso seja menor do que o nó previamente memorizado
    e identificado pela superclasse, o mesmo é substituido pelo nó em estudo que
    apresenta um melhor valor em função da avaliação feita

    @method _iniciar_fronteira: inicia uma fronteira de prioridade sem nós com
        o avaliador fornecido
    @method _manter: método que fazendo uso da verificação da superclasse por
        estados explorados anteriormente verifica recorrendo ao avaliador se o
        nó actual é melhor do que o nó memorizado e actualiza-o em caso positivo
    @method _iniciar_avaliador: método abstrato que inicia o avaliador quando
        implementado
    """

    def _iniciar_fronteira(self):
        """
        Método que inicia a fronteira da classe com uma fronteira de prioridade
        fornecendo ainda o avaliador fornecido pelo método _iniciar_avaliador

        @returns: fronteira de prioridade com o avaliador fornecido
        """
        self._avaliador = self._iniciar_avaliador()

        return FronteiraPrioridade(self._avaliador)

    def _manter(self, no):
        """
        Método que recorre à superclasse para verificar se o nó em estudo já foi
        explorado antes e em caso positivo verifica se o nó em estudo é melhor que
        o nó anteriormente explorado através do avaliador fornecido

        @param no: nó em estudo
        @returns: True caso o nó deva ser mantido, ou seja, caso ainda não tenha
            sido explorado ou caso o nó actual seja melhor do que o memorizado,
            ou False caso já tenha sido explorado anteriormente e seja melhor do
            que o nó atual
        """
        no_aberto = super()._manter(no)
        if not no_aberto:
            no_explorado = self._explorados[no.estado]
            prioridade_no = self._avaliador.prioridade(no)
            prioridade_explorado = self._avaliador.prioridade(no_explorado)
            avaliar = prioridade_no < prioridade_explorado
            return no_aberto or avaliar

        return no_aberto

    @abstractmethod
    def _iniciar_avaliador(self):
        """
        Método abstrato que quando implementado inicia o avaliador da
        prioridade entre nós

        @returns: avaliador da prioridade
        """
