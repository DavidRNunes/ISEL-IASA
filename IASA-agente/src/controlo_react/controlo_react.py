from ecr import Comportamento
from sae import Controlo


class ControloReact(Controlo):
    """
    Classe específica da classe abstrata Controlo implementando-a, consiste no
    controlo reactivo do agente, ou seja, controla o agente sob forma de uma
    arquitectura reactiva.

    A arquitectura reactiva consiste numa arquitectura simples de acção-reacção
    onde o agente deteta um estímulo através da sua percepção do ambiente que o
    rodeia e é activada uma resposta ao estímulo em função da intensidade do
    mesmo, sendo desencadeada uma acção por parte do agente. Esta classe recebe
    um comportamento único, ou um comportamento composto, permitindo processar
    tanto uma situação como outra - perante o estado atual do ambiente esta
    classe processa a informação e obtém uma resposta única para o agente atuar
    sobre o que foi percepcionado.

    @param comportamento: comportamento que pretendemos que o agente empregue
        perante o ambiente que o rodeia

    @method processar: método que processa a percepção do ambiente em função
        do comportamento fornecido ao agente e retorna a acção que o agente
        deve efectuar
    """

    def __init__(self, comportamento):
        """
        Método construtor da classe

        @param comportamento: comportamento a ter perante a percepção atual
            do ambiente
        """
        self._comportamento = comportamento
        self.mostrar_per_dir = True             # True ativa o debugger do simulador

    def processar(self, percepcao):
        """
        Método que processa o comportamento perante o ambiente percepcionado

        É activado o comportamento para a atual percepção do ambiente,
        criando o estímulo que corresponde à percepção actual sendo retornada
        a resposta a esse estímulo sob forma de acção a praticar pelo agente.

        @param percepcao: estado atual do ambiente que rodeia o agente
        @returns: a acção correspondente ao comportamento activado
        """
        return self._comportamento.activar(percepcao)
