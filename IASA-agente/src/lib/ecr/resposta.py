"""
Classe que representa a resposta que o agente deve ter a um determinado
estímulo. Esta resposta traduz-se numa acção que o agente irá fazer, perante
o que foi percepcionado no ambiente.
"""
class Resposta:
    """
    Método construtor da classe Resposta, recebe a acção a praticar perante
    a resposta atual.
    """
    def __init__(self, accao):
        self._accao = accao

    """
    Método que recebe a percepção e intensidade do estímulo e lhe faz
    corresponder uma prioridade, que se traduz em estímulos mais intensos
    terem uma resposta prioritária. Retorna a propria acção em função da
    sua intensidade.
    """
    def activar(self, percepcao, intensidade):
        self._accao.prioridade = intensidade

        return self._accao