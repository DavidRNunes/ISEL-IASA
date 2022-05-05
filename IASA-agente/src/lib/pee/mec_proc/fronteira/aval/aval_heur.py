from pee.mec_proc.fronteira.aval.avaliador import Avaliador
from pee.mec_proc.fronteira.aval.heuristica import Heuristica


class AvalHeur(Avaliador):

    _heuristica: Heuristica

    def __init__(self, heuristica):
        """
        
        """
        self._heuristica = heuristica
