from pee.mec_proc.fronteira.aval.aval_aa import AvalAA
from pee.mec_proc.fronteira.aval.aval_heur import AvalHeur
from pee.mec_proc.melhor_prim.procura_informada import ProcuraInformada


class ProcuraAA(ProcuraInformada):
    """
    Classe que implementa o método de procura A*

    O método de procura A* é um método optimista e completo,
    
    procura optimista - sempre que o custo estimado é menor
    ou igual ao custo real
    """

    def _iniciar_avaliador(self):
        """
        
        """
        self._avaliador = AvalAA(self._heuristica)

        return self._avaliador