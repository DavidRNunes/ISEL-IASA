from abc import ABC, abstractmethod


class MemoriaAprend(ABC):
    """
    Interface
    """

    @abstractmethod
    def q(self, s, a):
        """

        """

    @abstractmethod
    def actualizar(self, s, a, q):
        """

        """

    @abstractmethod
    def obter_estados(self):
        """

        """
