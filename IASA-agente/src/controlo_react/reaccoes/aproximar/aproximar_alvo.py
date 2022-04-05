from controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao


class AproximarAlvo(Prioridade):
    """
    Classe que implementa a classe Prioridade e define os comportamentos compostos
    contidos nela prórpria, correspondentes aos comportamentos de AproximarDir para
    cada direcção disponível no enumerador de Direcções

    Esta classe manda o agente avançar em direcção a um alvo quando o mesmo é detetado
    """
    
    def __init__(self):
        """
        Método construtor da classe AproximarAlvo

        Implementa o método construtor da classe abstrata ComportComp
        fornecendo a lista de comportamentos que constituem o comportamento
        AproximarDir, que consistem na aproximação numa determinada direção
        contida no enumerador Direccao
        """
        super().__init__([
            AproximarDir(direccao) for direccao in list(Direccao)
        ])
