from pee.mec_proc.fronteira.aval.aval_heur import AvalHeur


class AvalSofrega(AvalHeur):
    """
    Classe que implementa a classe da avaliação heurística através de uma
    procura sôfrega, que consiste em considerar apenas o custo estimado
    desde o nó actual até ao objetivo

    @method prioridade: obtém uma estimativa do custo desde o nó em estudo
        até ao objetivo
    """

    def prioridade(self, no):
        """
        Método que obtém o valor de prioridade do nó em função da avaliação
        sôfrega do mesmo, ou seja, através da obtenção do custo estimado 
        desde o nó actual até ao objetivo para a heurística definida

        @param no: nó actual em estudo
        @returns: estimativa do custo desde o nó actual até ao objetivo
        """
        return self._heuristica.h(no.estado)