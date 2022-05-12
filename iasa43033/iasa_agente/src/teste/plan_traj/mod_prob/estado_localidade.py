from mod.estado import Estado


class EstadoLocalidade(Estado):
    """
    Classe que implementa a classe abstrata Estado permitindo criar estados
    da classe de estados que compõe o problema do planeador de trajetos

    Um estado consiste no nome da localidade fornecido em formato string
    ao qual é atribuído um identificador único ficando assim criado o
    estado correspondente à localidade fornecida

    @param localidade: nome da localidade ao qual corresponde o estado

    @method id_valor: método que permite definir o identificador único do
        estado criado
    """

    _localidade: str

    def __init__(self, localidade):
        """
        Método construtor do estado da localidade

        @param localidade: nome da localidade, em string, ao qual este
            estado corresponde
        """
        self._localidade = localidade
        

    def id_valor(self):
        """
        Método que implementa o método abstrato da classe Estado
        permitindo definir o ID único para este estado

        @returns: identificador do estado em formato int
        """
        return hash(self._localidade)

    @property
    def localidade(self):
        """
        Propriedade que permite obter o nome da localidade correspondente ao
        estado
        """
        return self._localidade