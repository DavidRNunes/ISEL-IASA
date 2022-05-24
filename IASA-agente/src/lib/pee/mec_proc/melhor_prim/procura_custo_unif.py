from ..fronteira.aval.aval_custo_unif import AvalCustoUnif
from .procura_melhor_prim import ProcuraMelhorPrim


class ProcuraCustoUnif(ProcuraMelhorPrim):
    """
    Classe que implementa a superclasse ProcuraMelhorPrim fornecendo o
    avaliador que permite obter a prioridade de selecção dos nós

    A procura por custo uniforme confere aos nós a prioridade de expansão
    em função do custo do caminho até ao nó em estudo, sendo os nós cujo
    custo é menor expandidos primeiro

    @method _iniciar_avaliador: método que fornece o avaliador de custo uniforme
    """

    def _iniciar_avaliador(self):
        """
        Método que inicia o avaliador da prioridade entre nós

        Nesta situação inicia o avaliador de custo uniforme, obtendo
        o nó prioritário em função do custo do caminho até ao nó

        @returns: avaliador da prioridade custo uniforme
        """

        return AvalCustoUnif()
