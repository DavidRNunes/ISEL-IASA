from abc import ABC, abstractmethod


class ModeloPlan(ABC):
    """
    Interface
    """

    @abstractmethod
    def estado(self):
        """
        estado atual do agente
        """

    @abstractmethod
    def estados(self):
        """
        
        """

    @abstractmethod
    def operadores(self):
        """
        
        """