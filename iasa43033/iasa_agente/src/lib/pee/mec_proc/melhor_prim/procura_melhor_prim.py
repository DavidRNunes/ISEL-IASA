from abc import ABC, abstractmethod
from pee.mec_proc.procura_grafo import ProcuraGrafo


class ProcuraMelhorPrim(ProcuraGrafo, ABC):
    """
    
    """

    def _iniciar_fronteira(self):
        """
        Implementa método da superclasse
        """

    def _manter(self, no):
        """
        Altera método da superclasse
        """

    @abstractmethod
    def _iniciar_avaliador(self):
        """
        
        @returns: avaliador
        """
