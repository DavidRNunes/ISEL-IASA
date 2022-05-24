from mod import EstadoAgente, Problema


class ProblemaPlan(Problema):
    """
    Classe que implementa o problema de um planeador

    O problema do planeador consiste no estado que se pretende atingir
    e a percepção actual do mundo, através da qual são aplicados operadores
    até atingir o estado a que corresponde o objetivo

    @param modelo_plan: modelo do planeador actual - modelo actual do mundo
    @param estado_final: estado que se pretende que o agente atinja

    @method objectivo: verifica se o estado fornecido é o objetivo do problema
    """

    _estado_final: EstadoAgente
    """ Estado que se pretende atingir """

    def __init__(self, modelo_plan, estado_final):
        """
        Método construtor da classe, define o estado inicial do agente e os
        operadores possíveis em função do modelo do planeador e fornece esses
        dados para o construtor da superclasse

        @param modelo_plan: modelo actual do mundo
        @param estado_final: estado que se pretende atingir - objetivo
        """
        self._estado_final = estado_final
        self._estado_inicial = modelo_plan.estado()
        self._operadores = modelo_plan.operadores()

        super().__init__(self._estado_inicial, self._operadores)

    def objectivo(self, estado):
        """
        Método que permite verificar se o estado fornecido corresponde ao
        objetivo que se pretende atingir, verificando a igualdade entre
        o estado fornecido e o estado final definido pelo problema

        @param estado: estado que se pretende verificar
        @returns: True caso o estado seja o objetivo do problema, False em
            caso contrário
        """
        return estado.__eq__(self._estado_final)
