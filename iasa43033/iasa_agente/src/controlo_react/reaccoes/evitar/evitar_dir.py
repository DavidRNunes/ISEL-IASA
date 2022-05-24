from ecr import Reaccao

from ..resposta.resposta_evitar import RespostaEvitar
from .estimulo_obst import EstimuloObst


class EvitarDir(Reaccao):
    """
    Classe que herda as propriedade de uma Reaccao, sendo implementada por
    um estímulo e uma resposta

    Esta classe consiste na reacção do agente perante um obstáculo na sua
    proximidade permitindo uma resposta correspondente a evitar chocar com
    o obstáculo em causa

    @param direccao: direcção em que se encontra o obstáculo percepcionado
    @param resposta: reposta que o agente deve activar perante o estímulo
        detectado pelo mesmo
    """

    def __init__(self, direccao, resposta):
        """
        Classe construtora da classe EvitarDir

        Implementa o construtor da classe Reaccao fornecendo o estímulo
        percepcionado correspondente à percepção de um obstáculo na proximidade
        do agente através da classe EstimuloObst, da qual a classe depende, e
        uma resposta a esse mesmo estímulo
        """
        super().__init__(EstimuloObst(direccao), resposta)
