from .modelo_pdm import ModeloPDM


class PDM(ModeloPDM):
    """
    
    """

    _gama: float
    _delta_max: int

    def __init__(self, modelo, gama, delta_max):
        """
        
        """
        self._modelo = modelo
        self._gama = gama
        self._delta_max = delta_max

    def utilidade(self):
        """
        
        """

    def util_accao(self, s, a, U):
        """
        
        """

    def politica(self, U):
        """
        
        """

    def resolver(self):
        """
        
        """