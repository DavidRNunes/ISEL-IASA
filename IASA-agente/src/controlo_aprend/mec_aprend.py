from aprend_ref import AprendQ, MemoriaEsparsa, SelAccaoEGreedy
from mod import Estado


class MecAprend():
    """

    """

    _estados: Estado
    """ Estados ... """

    def __init__(self, accoes, alfa=0.5, gama=0.9, epsilon=0.01):
        """

        """
        self._mem_aprend = MemoriaEsparsa()
        self._sel_accao = SelAccaoEGreedy(self._mem_aprend, accoes, epsilon)
        self._aprend_ref = AprendQ(
            self._mem_aprend, self._sel_accao, alfa, gama)

    @property
    def estados(self):
        """
        Propriedade
        """
        return self._estados

    def aprender(self, s, a, r, sn):
        """

        """

    def selecionar_accao(self, s):
        """

        """

    def accao_sofrega(self, s):
        """

        """

    def q(self, s):
        """

        """
