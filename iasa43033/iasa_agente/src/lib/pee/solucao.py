class Solucao:
    """
    
    """

    __dimensao = None
    """ Dimensão da solução (int) """
    __custo = None
    """ Custo da solução (double) """

    def __init__(self, no_final):
        """
        criar o percurso do nó solução pelos antecessores até ao início
        """
        self._percurso = None

    @property
    def dimensao(self):
        """
        dimensão do percurso
        """

    @property
    def custo(self):
        """
        custo da solução
        """

    def remover_passo(self):
        """
        
        @returns: PassoSolucao
        """

    def __iter__(self):
        """
        
        @returns: iterador de nós
        """
        return iter(self._percurso)
    
    def __getitem__(self, key):
        """
        
        @returns: nó
        """
        return self._percurso[key]