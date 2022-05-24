from .fronteira import Fronteira


class FronteiraLIFO(Fronteira):
    """
    Classe que herda os métodos da classe fronteira e implementa o método
    de inserção de nós na lista

    A fronteira LIFO ou last-in-first-out consiste em adicionar nós em
    pilha, ou seja, uns seguidos dos anteriores, colocando sempre o nó mais
    recente no topo da fila, levando a que seja sempre o último a ter sido
    adicionado à lista de espera da fronteira a ser analisado de seguida

    @method inserir: implementação do método inserir da fronteira LIFO - nós
        são adicionados no fim da lista    
    """

    def inserir(self, no):
        """
        Método que permite inserir um nó na lista da fronteira, neste caso
        os nós são adicionados no fim da lista

        @param no: nó que se pretende adicionar à lista da fronteira
        """
        self._nos.append(no)
