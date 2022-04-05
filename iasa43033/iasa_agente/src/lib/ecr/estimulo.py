from abc import ABC, abstractmethod


class Estimulo(ABC):
    """
    Interface abstrata que representa o estímulo detetado pelo sensor do agente.

    Define o método abstrato detectar que tem como atributo a percepção do
    ambiente por parte do sensor do agente.
    """

    @abstractmethod
    def detectar(self, percepcao):
        """
        Método abstrato que deteta uma percepção do exterior

        Uma percepção do ambiente obtida pelo sensor do agente é
        traduzida num float que permite obter a intensidade do estímulo,
        permitindo assim detectar se a percepção activou um estímulo.

        @param percepcao: estado atual do ambiente que rodeia o agente
            percepcionado pelo sensor do mesmo
        """
