from mod.operador import Operador
from teste.plan_traj.mod_prob.estado_localidade import EstadoLocalidade


class OperadorLigacao(Operador):
    """
    
    """
    
    _custo: int
    _estado_origem: EstadoLocalidade
    _estado_destino: EstadoLocalidade

    def __init__(self, origem, destino, custo):
        """
        
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
        else:
            return None

    def custo(self, estado, estado_suc):
        """
        Método que retorna o custo da operação, como neste caso
        a implementação só necessita de obter o custo das operações
        não necessitamos de usar os parâmetros fornecidos, retornando
        apenas o custo da operação

        @returns: custo da operação
        """
        return self._custo