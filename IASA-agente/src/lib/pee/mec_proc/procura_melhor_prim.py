from abc import ABC, abstractmethod
from pee.mec_proc.procura_grafo import ProcuraGrafo


class ProcuraMelhorPrim(ProcuraGrafo, ABC):
    """
    
    """

    def iniciar_fronteira(self):
        """
        Implementa método da superclasse
        """

    def manter(self, no):
        """
        Altera método da superclasse
        """

    @abstractmethod
    def iniciar_avaliador(self):
        """
        
        @returns: avaliador
        """
