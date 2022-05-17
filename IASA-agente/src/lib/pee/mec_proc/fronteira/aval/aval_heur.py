from pee.mec_proc.fronteira.aval.avaliador import Avaliador
from pee.mec_proc.fronteira.aval.heuristica import Heuristica


class AvalHeur(Avaliador):
    """
    Classe abstrata que extende a interface do Avaliador de forma a 
    incorporar as avaliações que implementam heurística para obter
    a prioridade dos nós

    A avaliação heurística consiste na obtenção de uma estimativa do
    custo desde o estado actual até ao objetivo, dividindo-se ainda em
    duas variantes principais: a heurística que incorpora ainda o custo
    do percurso até ao nó actual e a heurística que ignora esse custo
    apresentando apenas a estimativa até ao objetivo

    @param heuristica: função heurística que permite obter a estimativa
        do custo até ao objetivo
    """

    _heuristica: Heuristica

    def __init__(self, heuristica):
        """
        Método construtor das classes de avaliação heurística
        
        @param heuristica: função que permite obter a estimativa do custo
            desde o nó actual até ao objetivo
        """
        self._heuristica = heuristica
