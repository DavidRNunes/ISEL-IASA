from mod.estado import Estado


class EstadoLocalidade(Estado):
    """
    
    """

    _localidade: str

    def __init__(self, localidade):
        """
        Método construtor do estado da localidade
        """
        self._localidade = localidade
        

    def id_valor(self):
        """
        
        """
        return hash(self._localidade)

    @property
    def localidade(self):
        """
        Propriedade que permite obter o nome da localidade correspondente ao
        estado
        """
        return self._localidade