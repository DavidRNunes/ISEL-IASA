from sae import Accao

from ecr.resposta import Resposta

"""
Classe especifica da classe Resposta que a implementa enviando para
a mesma a direcção para onde o agente se deve mover. É criada uma
acção correspondente ao movimento do agente e é fornecida a direcção
para onde este se deve mover, estes argumentos são então implementados
no construtor da superclasse, associando assim à acção criada o
argumento de direcção.
"""
class RespostaMover(Resposta):
    
    """
    Método contrutor da classe RespostaMover que recebe a direcção
    para onde o agente se deve mover e invoca o construtor da 
    superclasse pai Resposta e envia para a mesma a acção com o
    argumento direcção.
    """
    def __init__(self, direccao):
        super().__init__(Accao(direccao))