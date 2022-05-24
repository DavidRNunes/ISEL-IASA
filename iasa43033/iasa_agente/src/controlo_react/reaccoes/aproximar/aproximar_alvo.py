from ecr import Prioridade
from sae import Direccao

from .aproximar_dir import AproximarDir


class AproximarAlvo(Prioridade):
    """
    Classe que herda as propriedades da classe Prioridade, que por sua vez herda
    propriedades da classe ComportComp, implementando desta forma os comportamentos
    que permitem ao agente aproximar-se de um alvo numa das 4 direções possíveis.

    Esta classe recorre das propriedades da classe prioridade para efectuar a
    aproximação do agente ao alvo. Tal é garantido pois perante a percepção do ambiente
    é obtida a intensidade do estímulo traduzida pela distância entre o agente e o alvo,
    distância que se traduz na prioridade de execução do comportamento cuja direcção
    leva à aproximação do agente ao alvo devido ao método que seleciona a acção mais
    prioritária entre os comportamentos constituintes do comportamento AproximarAlvo
    """

    def __init__(self):
        """
        Método construtor da classe AproximarAlvo

        Implementa o método construtor da classe abstrata ComportComp
        fornecendo a lista de comportamentos que constituem o comportamento
        AproximarAlvo, que consistem nos comportamentos que permitem ao agente
        aproximar-se do alvo em função da direção que este se deve deslocar para
        atingir tal efeito, ou seja, é implementado o comportamento AproximarDir
        para cada uma das 4 direções que o agente se pode deslocar
        """
        super().__init__([
            AproximarDir(direccao) for direccao in list(Direccao)
        ])
