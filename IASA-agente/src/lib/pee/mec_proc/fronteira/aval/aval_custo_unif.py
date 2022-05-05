from pee.mec_proc.fronteira.aval.avaliador import Avaliador


class AvalCustoUnif(Avaliador):
    """
    Classe que implementa a interface Avaliador e obtém a prioridade de
    um nó em função do custo do caminho até atingir o nó

    @method prioridade: método que permite obter a prioridade do nó em
        função do custo do caminho até ele
    """

    def prioridade(self, no):
        """
        Método que obtem o valor de prioridade do nó em função do custo
        do caminho até este nó

        @param no: nó em estudo
        @returns: custo do nó e dos seus antecessores correspondente ao
            custo do caminho até ao nó fornecido, valor em double
        """
        custo = no.custo
        self._no = no
        while self._no.antecessor:
            custo += self._no.antecessor.custo
            self._no = no.antecessor

        return custo