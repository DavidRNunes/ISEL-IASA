from mod import Operador

from .estado_localidade import EstadoLocalidade


class OperadorLigacao(Operador):
    """
    Classe que implementa a interface Operador permitindo criar os
    operadores entre dois estados

    Através desta classe são criados os operadores do modelo do
    problema de planeamento de trajetos, sendo fornecido o estado
    inicial (localidade inicial) e o estado de destino (localidade
    destino) e o custo da operação. Estes dados são guardados localmente
    associando os estados a um custo criando assim o operador entre
    estes estados

    @param origem: localidade inicial do operador
    @param destino: localidade final do operador
    @param custo: custo da operação

    @method aplicar: verifica se o estado fornecido é o estado inicial
        do nó retornando o destino em caso afirmativo
    @method custo: retorna o custo da operação entre os dois nós fornecidos
    """

    _custo: int
    _estado_origem: EstadoLocalidade
    _estado_destino: EstadoLocalidade

    def __init__(self, origem, destino, custo):
        """
        Método construtor do operador de ligação

        @param origem: string da localidade inicial, passada para a classe
            EstadoLocalidade para ser guardada sob a forma de um estado
        @param destino: string da localidade de destino, passada para a
            classe EstadoLocalidade sendo guardada sob a forma de estado
        @param custo: custo da operação entre os estados
        """
        self._estado_origem = EstadoLocalidade(origem)
        self._estado_destino = EstadoLocalidade(destino)
        self._custo = custo

    def aplicar(self, estado):
        """
        Método que verifica se o estado fornecido corresponde ao
        estado inicial do nó de forma a poder ser aplicado o
        operador

        @param estado: estado que se pretende aplicar o operador
        @returns: estado de destino caso este operador possa ser
            aplicado a este estado
        """
        if estado.__eq__(self._estado_origem):
            return self._estado_destino

    def custo(self, estado, estado_suc):
        """
        Método que retorna o custo da operação, como neste caso
        a implementação só necessita de obter o custo das operações
        não necessitamos de usar os parâmetros fornecidos, retornando
        apenas o custo da operação

        @returns: custo da operação
        """
        return self._custo
