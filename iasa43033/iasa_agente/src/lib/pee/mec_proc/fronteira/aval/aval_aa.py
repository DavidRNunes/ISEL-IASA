from pee.mec_proc.fronteira.aval.aval_heur import AvalHeur


class AvalAA(AvalHeur):

    def prioridade(self, no):
        """
        
        """
        return no.custo + self._heuristica.h(no.estado)