from ecr.resposta import Resposta
from sae import Accao


class RespostaMover(Resposta):
    """
    Especialização da classe Resposta que implementa a resposta a um
    estímulo traduzindo-se num movimento do agente numa determinada
    direcção.

    É definida uma resposta específica a um estímulo que informa o agente
    da direcção para onde este se deve mover, sendo invocado o construtor
    da classe geral fornecendo à acção o argumento de direcção
    """

    def __init__(self, direccao):
        """
        Método construtor da classe

        Invoca o construtor da superclasse Resposta e envia para a mesma
        a acção com o argumento de direcção

        @param direccao: direcção para onde o agente se deve mover
        """
        super().__init__(Accao(direccao))
