from pee.mec_proc.fronteira.aval.aval_sofrega import AvalSofrega
from pee.mec_proc.melhor_prim.procura_informada import ProcuraInformada


class ProcuraSofrega(ProcuraInformada):
    """
    Classe que implementa a classe abstrata da ProcuraInformada 
    """

    def _iniciar_avaliador(self):
        """
        Método que inicia o avaliador heurístico do problema

        É iniciado o avaliador de procura sôfrega obtendo o custo mínimo
        local do nó, ou seja, apenas o custo desde o estado actual até ao
        objetivo, sem ter em conta o custo do percurso explorado

        @returns: avaliador da procura sôfrega
        """
        self._avaliador = AvalSofrega(self._heuristica)

        return self._avaliador