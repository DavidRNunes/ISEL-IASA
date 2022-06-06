from mod import Estado
from sae import Accao, Controlo

from .mec_aprend import MecAprend


class ControloAprendRef(Controlo):
    """

    """

    _rmax: float
    """ Rmax é ... """
    _rmin: float
    """ Rmin é ... """
    _s: Estado
    """ S é ... """
    _a: Accao
    """ A é ... """

    def __init__(self):
        """

        """
        self._rmax = 100.0
        self._rmin = 1.0

    def processar(self, percepcao):
        """
        self._mec_aprend = MecAprend(accoes) -> here (?)
        """

    def _gerar_reforco(self, percepcao):
        """

        """

    def _mostrar(self):
        """

        """
