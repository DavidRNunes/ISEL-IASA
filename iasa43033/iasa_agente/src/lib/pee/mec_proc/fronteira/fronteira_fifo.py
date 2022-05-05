from pee.mec_proc.fronteira.fronteira import Fronteira


class FronteiraFIFO(Fronteira):
    """
    Classe que herda os métodos da classe fronteira e implementa o método
    de inserção de nós na lista

    A fronteira FIFO ou first-in-first-out consiste em obter o primeiro nó que
    foi adicionado à lista, correspondente ao nó mais antigo a ter sido
    adicionado. Tal é assegurado colocando sempre os nós na primeira posição
    da lista, levando a que os nós mais antigos fiquem sempre nas posições mais
    próximas do fim da lista

    @method inserir: implementação do método inserir da fronteira FIFO - nós
        são adicionados no início da lista  
    """

    def inserir(self, no):
        """
        Método que permite inserir um nó na lista da fronteira, neste caso
        os nós são adicionados no início da lista
        
        @param no: nó que se pretende adicionar à lista da fronteira
        """
        self._nos.insert(0, no)