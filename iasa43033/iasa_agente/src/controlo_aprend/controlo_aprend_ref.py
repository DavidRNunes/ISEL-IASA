from mod import Estado, EstadoAgente
from sae import Accao, Controlo, Direccao

from .mec_aprend import MecAprend


class ControloAprendRef(Controlo):
    """
    Classe que implementa o controlo do agente sob um mecanismo de
    aprendizagem por reforço
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
        self._s = None
        self._a = None
        accoes = [Accao(direccao) for direccao in Direccao]
        self._mec_aprend = MecAprend(accoes)

    def processar(self, percepcao):
        """

        """
        sn = EstadoAgente(percepcao.posicao)
        if self._s:
            r = self._gerar_reforco(percepcao)
            self._mec_aprend.aprender(self._s, self._a, r, sn)
        an = self._mec_aprend.selecionar_accao(sn)
        self._s = sn
        self._a = an

        self._mostrar()

        return an

    def _gerar_reforco(self, percepcao):
        """

        """
        r = -self._rmin  # reforço por efectuar uma acção
        if percepcao.recolha:
            r += self._rmax
        elif percepcao.colisao:
            r += -self._rmax
        return r

    def _mostrar(self):
        """

        """
        estados = self._mec_aprend.estados
        politica = {s: self._mec_aprend.accao_sofrega(s) for s in estados}
        valor = {s: self._mec_aprend.q(s, politica[s]) for s in estados}
        self.vista.limpar()
        self.vista.mostrar_valor(valor)
        self.vista.mostrar_politica(politica)
