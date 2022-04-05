from controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao


class AproximarDir(Reaccao):
    """
    Classe que implementa a classe Reaccao e indica a direcção para o qual o
    agente se deve tentar mover
    """

    def __init__(self, direccao):
        """
        Método construtor da classe AproximarDir

        Fornece ao construtor da classe Reaccao o estímulo, correspondente
        ao alvo e a resposta correspondente a mover em direcção ao alvo

        @param direccao: direcção para onde pretendemos que o agente tente
            mover-se
        """
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))
