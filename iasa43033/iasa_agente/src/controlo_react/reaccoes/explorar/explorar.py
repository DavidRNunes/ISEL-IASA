from random import choice

from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.comportamento import Comportamento
from sae.ambiente.direccao import Direccao


class Explorar(Comportamento):
    """
    Classe que realiza a classe Comportamento, implementando os seus métodos
    para criar um comportamento que consiste na deslocação aleatória do agente
    em uma unidade no espaço que o rodeia

    É selecionada uma direcção aleatóriamente por entre as direções disponíveis
    no enumerador Direccao, recorrendo ao método choice da classe Random do
    Python, sendo esta fornecida à classe RespostaMover que, em conjunto com a
    percepcção do ambiente atual, retorna a acção de mover o agente uma unidade
    na direcção escolhida

    @method activar: método que recebe a percepção do ambiente e permite
        a deslocação do mesmo na direcção selecionada
    """

    def activar(self, percepcao):
        """
        Método que ativa a exploração do agente

        Este método recebe a percepção do ambiente que rodeia o agente e
        permite que o mesmo se desloque aleatóriamente uma unidade na
        direcção selecionada

        @param percepcao: estado atual do ambiente que rodeia o agente
        @returns: a acção a praticar pelo agente constituída por uma
            direcção e intensidade, traduzindo-se numa deslocação no
            ambiente em que se encontra
        """
        direccao = choice(list(Direccao))
        resposta = RespostaMover(direccao)
        return resposta.activar(percepcao)
