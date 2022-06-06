from .aprend_ref import AprendRef


class AprendQ(AprendRef):
    """
    
    """

    _alfa: float
    """ Alfa é... """
    _gama: float
    """ Gama é... """

    def __init__(self, mem_aprend, sel_accao, alfa, gama):
        self._alfa = alfa
        self._gama = gama
        super().__init__(mem_aprend, sel_accao)

    def aprender(self, s, a, r, sn):
        """
        super
        """
