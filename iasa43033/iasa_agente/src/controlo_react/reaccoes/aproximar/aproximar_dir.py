from controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao


class AproximarDir(Reaccao):
    """
    Classe que implementa a Reaccao correspondente à aproximação do agente em
    direcção a um alvo que se situe perto do mesmo

    Nesta classe é fornecida uma das 4 direcções do enumerador Direccao sendo
    implementada a classe Reaccao fornecendo o estímulo correspondente ao alvo
    mais próximo na direcção fornecida (em função da distância), e a resposta
    a esse estímulo, nomeadamente, o movimento em direcção ao alvo

    @param direccao: direcção do movimento do agente
    """

    def __init__(self, direccao):
        """
        Método construtor da classe AproximarDir

        Fornece ao construtor da classe Reaccao o estímulo correspondente
        ao alvo mais próximo do agente e a resposta correspondente a mover
        em direcção a esse mesmo alvo através das classes EstimuloAlvo e
        RespostaMover, respetivamente

        @param direccao: direcção em que o agente se move
        """
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))
