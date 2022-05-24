from ecr import Hierarquia
from sae import Direccao

from ..resposta.resposta_evitar import RespostaEvitar
from .evitar_dir import EvitarDir


class EvitarObst(Hierarquia):
    """
    Classe que herda as propriedades da classe Hierarquia, herdando por sua
    vez as propriedades da classe ComportComp, pelo que a classe EvitarObst
    se trata de um comportamento composto de comportamentos que evitam um
    obstáculo que se encontra no ambiente numa determinada direcção relativa
    ao agente

    A classe EvitarObst consiste então nos comportamentos EvitarDir para cada
    direcção do enumerador Direccao, sendo criado um comportamento EvitarDir
    para cada direcção em que se encontra um obstáculo próximo do agente,
    permitindo a este que os evite
    """

    def __init__(self):
        """
        Método construtor da classe EvitarObst

        Consiste na implementação do construtor da classe ComportComp sendo
        criada uma lista de comportamentos EvitarDir, um por cada direcção
        no enumerador Direccao, sendo fornecida a direcção do obstáculo mais
        próximo percepcionado pelo agente e a resposta correspondente a evitar
        esse mesmo obstáculo através da classe RespostaEvitar, da qual a
        classe EvitarObst depende
        """
        super().__init__([
            EvitarDir(direccao, RespostaEvitar(direccao)) for direccao in list(Direccao)
        ])
