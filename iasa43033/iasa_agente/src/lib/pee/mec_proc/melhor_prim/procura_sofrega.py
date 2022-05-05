from pee.mec_proc.fronteira.aval.aval_sofrega import AvalSofrega
from pee.mec_proc.melhor_prim.procura_informada import ProcuraInformada


class ProcuraSofrega(ProcuraInformada):

    def _iniciar_avaliador(self):
        """
        
        """
        self._avaliador = AvalSofrega(self._heuristica)

        return self._avaliador