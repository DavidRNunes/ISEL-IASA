from abc import abstractmethod
from no import No
from pee import Solucao
from mod import Estado
from mod import Operador
from mod.problema import Problema


class MecanismoProcura:
    """
    
    """

    def __init__(self):
        """
        
        """
    
    def resolver(self, problema):
        """
        
        @returns: solução
        """

    def expandir(self, no):
        """
        
        @returns: lista de nós
        """
    
    @abstractmethod
    def iniciar_fronteira(self):
        """
        
        @returns: fronteira
        """

    @abstractmethod
    def memorizar(self, no):
        """
        
        """