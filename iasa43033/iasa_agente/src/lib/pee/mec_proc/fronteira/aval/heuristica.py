from abc import ABC, abstractmethod


class Heuristica(ABC):
    """
    Interface abstrata que define a função heuristíca, h

    A função heuristíca h representa uma estimativa do custo do
    percurso desde o nó n até ao objetivo

    @method h: método que define a função h
    """

    @abstractmethod
    def h(self, estado):
        """
        Método que define a função h independente do custo do
        caminho até ao estado fornecido, dependendo apenas do
        estado e do objetivo

        @param estado: estado que se pretende estimar o custo desde
            ele prórprio até ao objetivo
        @returns: valor estimado do custo desde o estado até ao
            objetivo, em double
        """
