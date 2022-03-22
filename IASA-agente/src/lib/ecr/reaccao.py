"""
Classe que representa uma associação estímulo-resposta baseada na arquitectura
reativa. Perante uma percepção de algo exterior esta activa um estímulo que,
perante a sua intensidade, ativa uma resposta que se irá traduzir numa acção.
Estas interações representam então uma reacção de um agente, traduzidas nesta
classe. Reacção herda da classe Comportamento o método activar, uma vez que 
um conjunto de reacções relacionadas pode ser agrupada num módulo comportamental,
que nos permite assim ter no seu interior comportamentos, que por sua vez podem
ter reacções e/ou outros comportamentos que por sua vez dispõem da mesma regra
estrutural.
"""
from .comportamento import Comportamento

class Reaccao(Comportamento):
    """
    Método construtor da classe Reaccao, recebe como argumentos um
    estimulo e uma resposta e guarda os mesmos para variáveis internas.
    """
    def __init__(self, estimulo, resposta):
        self._estimulo = estimulo
        self._resposta = resposta

    """
    Método que activa a detecção de um estímulo, ou seja, perante a percepção
    exterior detetada guarda o valor da intensidade do estímulo correspondente
    que, se for superior a 0 (ou seja, se existe um estímulo), ativa a resposta
    correspondente a esse estímulo.
    @args percepcao - o ambiente exterior percepcionado, que se traduz num estímulo
    @returns accao - a resposta ao estímulo detetado, emm função da sua intensidade
    """
    def activar(self, percepcao):
        intensidade = self._estimulo.detectar(percepcao)

        if intensidade > 0:
            accao = self._resposta.activar(percepcao, intensidade)

            return accao