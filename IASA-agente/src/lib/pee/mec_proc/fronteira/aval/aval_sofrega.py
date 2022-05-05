from pee.mec_proc.fronteira.aval.aval_heur import AvalHeur


class AvalSofrega(AvalHeur):

    def prioridade(self, no):
        """
        Método que obtém o valor de prioridade do nó em função
        da avaliação sôfrega do mesmo, ou seja, é fornecido o
        seu custo local, o custo do nó
        """
        return self._heuristica.h(no.estado)