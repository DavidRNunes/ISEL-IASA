from abc import ABC, abstractmethod
from estado import Estado


class Operador(ABC):
    """
    
    """

    @abstractmethod
    def aplicar(self, estado):
        """
        
        @returns: estado
        """

    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        
        @returns: double
        """