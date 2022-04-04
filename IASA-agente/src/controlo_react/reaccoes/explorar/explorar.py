from random import choice
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.comportamento import Comportamento
from sae.ambiente.direccao import Direccao

"""
Classe que realiza o método activar do comportamento do agente correspondente
a andar numa direção aleatória das direcções disponíveis no enumerador Direccao. 
Esta classe cria uma lista das direcções possíveis e da mesma escolhe uma direção
aleatoriamente recorrendo ao método choice da classe random do python.
Esta direcção é fornecida à classe RespostaMover em conjunto com a
percepção atual e é retornada a acção correspondente, neste caso, mover
uma unidade na direção escolhida.
"""
class Explorar(Comportamento):

    """
    Método que recebe a percepção atual do ambiente que rodeia o agente
    e escolhe uma direção aleatória para mover o agente. Este método
    permite mover o agente aleatoriamente pelo ambiente em que este se
    encontra, selecionando uma direcção aleatória e para a mesma activando
    a resposta correspondente - avançar uma unidade nessa direcção.
    """    
    def activar(self, percepcao):
        direccao = choice(list(Direccao))
        resposta = RespostaMover(direccao)
        return resposta.activar(percepcao)