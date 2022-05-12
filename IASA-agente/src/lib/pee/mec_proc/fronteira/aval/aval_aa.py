from pee.mec_proc.fronteira.aval.aval_heur import AvalHeur


class AvalAA(AvalHeur):
    """
    Classe que implementa a interface Avaliador obtendo a prioridade do nó
    em função do custo do trajeto até ao nó atual e do custo mínimo até ao
    nó objetivo - Avaliação A*

    @method prioridade: calcula a prioridade do nó em função do custo mínimo
        global
    """

    def prioridade(self, no):
        """
        Método que permite obter a prioridade do nó em função da minimização
        do custo global

        @param no: nó em estudo
        @returns: custo do caminho até ao nó com o custo mínimo até ao objetivo
        """
        return no.custo + self._heuristica.h(no.estado)