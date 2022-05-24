from ..estado import Estado


class EstadoAgente(Estado):
    """
    Classe que implementa a classe abstrata Estado permitindo criar estados
    para as diferentes posições do agente no mundo

    O estado do agente no mundo consiste na posição que este ocupa, sendo
    posição um tuplo de valores correspondente às coordenadas do agente

    @param posicao: tuplo de coordenadas da posição atual do agente

    @method id_valor: método que permite definir o identificador único do
        estado criado
    """

    def __init__(self, posicao):
        """
        Método construtor da classe EstadoAgente, guarda a posição
        fornecida criando o estado para essa posição

        @param posicao: tuplo da posição actual do agente no mundo
        """
        self._posicao = posicao

    @property
    def posicao(self):
        """
        Propriedade que permite obter a posição do agente para o estado
        definido
        """
        return self._posicao

    def id_valor(self):
        """
        Método que implementa o método abstrato da classe Estado
        permitindo definir o ID único para este estado

        @returns: identificador do estado em formato int
        """
        return hash(self._posicao)
