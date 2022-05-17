from mod.estado import Estado
from mod.problema.problema import Problema


class ProblemaPlan(Problema):
    """
    
    """

    _estado_final: Estado

    def __init__(self, modelo_plan, estado_final):
        """
        
        """
        self._estado_final = estado_final
        self._estado_inicial = modelo_plan.estado()
        self._operadores = modelo_plan.operadores()
        super().__init__(self._estado_final, self._operadores)


    def objectivo(self, estado):
        """
        
        """
        return estado.__eq__(self._estado_final)