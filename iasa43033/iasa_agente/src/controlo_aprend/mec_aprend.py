from apr import AprendQ, MemoriaEsparsa, SelAccaoEGreedy
from mod import Estado


class MecAprend():
    """
    Classe que permite controlar o mecanismo de aprendizagem

    Esta classe permite iniciar as várias classes do mecanismo de
    aprendizagem de forma a facilitar a intercção do controlo de
    aprendizagem por reforço

    """

    _estados: Estado
    """ Estados ... """

    def __init__(self, accoes, alfa=0.5, gama=0.9, epsilon=0.01):
        """

        """
        self._accoes = accoes
        self._alfa = alfa
        self._gama = gama
        self._epsilon = epsilon
        self._mem_aprend = MemoriaEsparsa()
        self._sel_accao = SelAccaoEGreedy(self._mem_aprend, accoes, epsilon)
        self._aprend_ref = AprendQ(
            self._mem_aprend, self._sel_accao, alfa, gama)

    @property
    def estados(self):
        """
        Propriedade
        """
        return self._mem_aprend.obter_estados()

    def aprender(self, s, a, r, sn):
        """

        """
        self._aprend_ref.aprender(s, a, r, sn)

    def selecionar_accao(self, s):
        """

        """
        return self._sel_accao.seleccionar_accao(s)

    def accao_sofrega(self, s):
        """

        """
        return self._sel_accao.accao_sofrega(s)

    def q(self, s, a):
        """

        """
        return self._mem_aprend.q(s, a)
