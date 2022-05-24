from abc import ABC, abstractmethod

from mod import Estado, Operador
from .transicao import Transicao


class ModeloPDM(ABC):
    """
    
    """

    @abstractmethod
    def S(self):
        """
        
        """

    @abstractmethod
    def A(self, s):
        """
        
        """

    @abstractmethod
    def T(self, s, a):
        """
        
        """

    @abstractmethod
    def R(self, s, a, sn):
        """
        
        """