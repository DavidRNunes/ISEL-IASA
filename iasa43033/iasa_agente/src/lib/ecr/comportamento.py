from abc import ABC, abstractmethod

"""
Interface abstrata que engloba reacções e outros comportamentos.
O comportamento relaciona padrões de percepção com padrões de acção,
pelo que o método abstrato activar tem como atributo a percepção do
exterior.
"""
class Comportamento(ABC):
    """
    Método abstrato que recebe como atributo a percepção do exterior
    e é implementado na classe reacção de forma a relacionar esta
    percepção com a sua ação correspondente
    """
    @abstractmethod
    def activar(self, percepcao):
        """Activar"""
