from abc import ABC, abstractmethod

from mod import Estado, Operador


class ModeloPDM(ABC):
    """
    Interface abstrata representante do modelo de processos de decisão de
    Markov

    Define a estrutura da representação do mundo sob a forma de um processo
    de decisão de Markov, recorrendo às funções que permitem representar o
    conjunto de estados no mundo, as acções que o agente pode praticar, a
    probabilidade de transitar para um determinado estado por meio de uma
    dada acção e a recompensa obtida em função da transição de estado
    efectuada
    """

    @abstractmethod
    def S(self):
        """
        Método abstrato que representa o conjunto de estados do mundo

        @returns: lista de estados do mundo
        """

    @abstractmethod
    def A(self, s):
        """
        Método abstrato que representa o conjunto de acções possíveis
        no estado s fornecido

        @param s: estado actual pertencente ao conjunto de estados em S
        @returns: lista de operadores do modelo do mundo
        """

    @abstractmethod
    def T(self, s, a):
        """
        Método abstrato que representa a probabilidade de transição do
        estado s fornecido para um estado seguinte s' através da acção
        a também ela fornecida

        @param s: estado actual pertencente ao conjunto de estados em S
        @param a: acção que se pretende aplicar ao estado s
        @returns: lista de tuplos das transições contendo a probabilidade
            da transição e o estado seguinte
        """

    @abstractmethod
    def R(self, s, a, sn):
        """
        Método abstrato que representa a recompensa esperada para a
        transição do estado s para sn por meio da acção a, todos eles
        fornecidos ao método

        @param s: estado actual pertencente ao conjunto de estados em S
        @param a: acção que se pretende aplicar ao estado s
        @param sn: estado sucessor após se aplicar a acção a ao estado s
        @returns: o valor da recompensa em double
        """
