from mod import Estado

from .memoria_aprend import MemoriaAprend


class MemoriaEsparsa(MemoriaAprend):
    """

    """

    _valor_omissao: float
    """ Valor omisao é... """
    _memoria: None
    """ Memória é... """
    _estados: Estado
    """ Estados ... necessário(?) """

    def __init__(self, valor_omissao=0.0):
        """

        """
        self._valor_omissao = valor_omissao

    @property
    def memoria(self):
        """
        Propriedade
        """
        return self._memoria

    def q(self, s, a):
        """
        super
        """

    def actualizar(self, s, a, q):
        """
        super
        """

    def obter_estados(self):
        """
        super
        self._estados (?)
        """
