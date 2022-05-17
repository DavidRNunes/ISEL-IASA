from pee.mec_proc.fronteira.aval.aval_aa import AvalAA
from pee.mec_proc.fronteira.aval.aval_heur import AvalHeur
from pee.mec_proc.melhor_prim.procura_informada import ProcuraInformada


class ProcuraAA(ProcuraInformada):
    """
    Classe que implementa o método de procura A*

    O método de procura A* é um método optimista e completo, ou seja, o método de
    procura é admissível - a estimativa do custo é sempre inferior ou igual ao
    custo mínimo real, o que permite garantir que a solução que se encontra é
    sempre a solução óptima. É importante verificar que a heurística utilizada no
    método de procura A* é consistente, uma vez que uma heurística admissível não
    garante que esta seja consistente, ou seja, não garante que os valores do custo
    do percurso até um dado nó não diminuam - uma heuristica consistente garante
    que os valores de f(n) (função que avalia o custo da solução) nunca diminuem
    ao longo do tempo, pois os nós a ser expandidos encontram-se num percurso
    óptimo, garantindo que qualquer outro caminho escolhido tem, na melhor das
    hipóteses, um custo igual

    @method _iniciar_avaliador: inicia o avaliador heurístico da procura A*
    """

    def _iniciar_avaliador(self):
        """
        Método que inicia o avaliador heurístico do problema

        É iniciado o avaliador A* obtendo o custo mínimo do nó até
        ao objetivo

        @returns: avaliador da procura A*
        """
        self._avaliador = AvalAA(self._heuristica)

        return self._avaliador