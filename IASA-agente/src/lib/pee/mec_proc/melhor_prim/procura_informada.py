from abc import ABC
from pee.mec_proc.fronteira.aval.heuristica import Heuristica
from pee.mec_proc.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim


class ProcuraInformada(ProcuraMelhorPrim, ABC):
    """
    Classe abstrata que define o mecanismo de procura informada

    Procura informada tira partido de conhecimento do domínio do problema
    para ordenar a fronteira de exploração, fazendo uso dessa avaliação
    sobre o conhecimento para colocar os nós mais promissores numa posição
    prioritária para serem explorados primeiro. Esta procura torna-se muito
    mais eficiente a encontrar soluções do que a procura não informada, mas
    é necessário ter em atenção ao método de avaliação heuristico, uma vez
    que este deve ser simples de calcular de forma a não aumentar o tempo
    necessário para as estimações da prioridade.

    @method resolver:
    """

    _heuristica: Heuristica

    def resolver(self, problema, heuristica):
        """
        Método

        @param problema:
        @param heuristica:
        @returns:
        """
        self._heuristica = heuristica

        return super().resolver(problema)