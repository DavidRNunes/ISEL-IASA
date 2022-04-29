from pee import FronteiraFIFO
from pee import ProcuraGrafo


class ProcuraLarg(ProcuraGrafo):
    """
    
    """

    def _iniciar_fronteira(self):
        """
        Implementa o método da superclasse
        """
        self._fronteira = FronteiraFIFO()

        return self._fronteira