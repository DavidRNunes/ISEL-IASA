from abc import ABC, abstractmethod


class Comportamento(ABC):
    """
    Interface abstrata que representa o módulo comportamental do agente

    O comportamento do agente relaciona os padrões de percepção com os
    padrões de acção, pelo que o método activar recebe a percepção atual
    do ambiente e retorna uma acção ou mais acções correspondentes a
    essa percepção que devem posteriormente ser processadas pelo agente

    @method activar: método abstrato que activa a reacção do comportamento
        à percepcção atual do ambiente
    """

    @abstractmethod
    def activar(self, percepcao):
        """
        Método abstrato que quando implementado activa a reacção perante
        o ambiente percepcionado, retornando a acção ou acções
        correspondentes.

        @param percepcao: estado atual do ambiente que rodeia o agente
        """
