
from random import choice
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae import Accao
from sae import Direccao


class RespostaEvitar(RespostaMover):
    """
    Classe que permite ao agente evitar os obstáculos que o rodeiam
    """

    def __init__(self, dir_inicial = Direccao.ESTE):
        """"""
        self._dir_inicial = dir_inicial
        self._direccoes = list(Direccao)
        self._accao = Accao(dir_inicial)
        super().__init__(self._accao)

    def activar(self, percepcao, intensidade):
        if percepcao.contacto_obst(self._dir_inicial):
            self._accao.direccao = self.direccao_livre(percepcao)
            return super().activar(percepcao, intensidade)
        else:
            return super().activar(percepcao, intensidade)

    def direccao_livre(self, percepcao):
        dir_livres = [direccao for direccao in self._direccoes
                        if not percepcao.contacto_obst(direccao)]

        return choice(list(dir_livres))