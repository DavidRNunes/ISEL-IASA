from .sel_accao import SelAccao


class SelAccaoEGreedy(SelAccao):
    """

    """

    _epsilon: float
    """ Epsilon é... """

    def __init__(self, mem_aprend, accoes, epsilon):
        """

        """
        self._mem_aprend = mem_aprend
        self._accoes = accoes
        self._epsilon = epsilon

    def seleccionar_accao(self, s):
        """
        super
        """

    def accao_sofrega(self, s):
        """

        """

    def explorar(self):
        """

        """
