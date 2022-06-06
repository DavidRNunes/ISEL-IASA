from abc import ABC, abstractmethod


class AprendRef(ABC):
    """

    """

    def __init__(self, mem_aprend, sel_accao):
        """

        """
        self._mem_aprend = mem_aprend
        self._sel_accao = sel_accao

    @abstractmethod
    def aprender(self, s, a, r, sn):
        """

        """
