from abc import ABC, abstractmethod


class MemoriaAprend(ABC):
    """
    Interface abstrata representativa da memória do algoritmo

    Quando implementada esta classe permite que o agente tenha
    memória do mundo, nomeadamente dos valores de estado-acção
    de cada posição que já visitou no passado
    """

    @abstractmethod
    def q(self, s, a):
        """
        Método abstrato que representa um valor de num estado
        realizar uma dada acção, retornando o valor de no estado
        s realizar a acção a - equivalente a uma recompensa imediata

        @param s: estado observado do qual se pretende obter o valor
        @param a: acção realizada pelo agente no estado s
        """

    @abstractmethod
    def actualizar(self, s, a, q):
        """
        Método abstrato que permite actualizar a memória do algoritmo
        para um determinado estado mediante a acção praticada e o valor
        de utilidade obtido por essa acção

        @param s: estado observado actual
        @param a: acção realizada
        @param q: valor estado-acção obtido
        """

    @abstractmethod
    def obter_estados(self):
        """
        Método abstrato que permite obter a lista de estados conhecidos
        pelo agente - estados que se encontram em memória
        """
