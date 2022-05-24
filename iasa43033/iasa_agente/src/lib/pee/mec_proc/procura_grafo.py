from abc import ABC

from .mecanismo_procura import MecanismoProcura
from .no import No


class ProcuraGrafo(MecanismoProcura, ABC):
    """
    Classe abstrata que implementa as bases para os métodos de procura por
    grafos

    Um algoritmo que verifique por redundância dos caminhos a expandir é
    denominado de um mecanismo de procura por grafos, uma vez que guarda
    em memória os estados que já foram previamente explorados. Desta forma
    evita-se explorar os mesmos estados várias vezes, evitando redundância.
    Cada um dos estados atingido é guardado num dicionário que permite
    posteriormente verificar se o estado já foi explorado de forma a ignorar
    o mesmo e evitando a necessidade de expandir o nó

    @method resolver: método que cria o dicionário de memória de estados explorados
    @method _memorizar: método que permite memorizar o nó no dicionário e
        adicionar o mesmo à fronteira
    @method _manter: método que verifica se um dado nó tem um estado previamente
        explorado
    """

    def resolver(self, problema):
        """
        Método que cria o dicionário com o nó inicial e recorre à superclasse
        para efectuar o algoritmo de resolução da procura

        @param problema: estado inicial do agente, operadores e objetivos
        @returns: solução do problema ou None caso não haja solução, recorrendo
            à superclasse
        """
        self._explorados = {}

        return super().resolver(problema)

    def _memorizar(self, no):
        """
        Método que permite adicionar nós à fronteira de exploração e ao
        dicionário de estados explorados

        É feita uma verificação se o nó em causa deve ser memorizado na
        fronteira de exploração que consiste em verificar se o estado do
        nó já foi explorado previamente

        @param no: nó que se pretende memorizar
        """
        if self._manter(no):
            self._explorados.update({no.estado: no})
            self._fronteira.inserir(no)

    def _manter(self, no):
        """
        Método que verifica se o estado do nó fornecido corresponde a um
        estado que tenha sido explorado anteriormente

        @returns: True caso o nó deva ser mantido, ou seja, caso ainda não
            tenha sido explorado, ou False caso já tenha sido explorado
            anteriormente e deva ser ignorado
        """
        for estado_explorado in self._explorados.keys():
            if no.estado == estado_explorado:
                return False

        return True
