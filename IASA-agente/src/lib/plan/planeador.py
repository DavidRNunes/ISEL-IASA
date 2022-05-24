from abc import ABC, abstractmethod


class Planeador(ABC):
    """
    Interface abstrata do planeador

    Um planeador consiste num processo que permite planear o curso de
    accção do agente de forma a atingir todos os objetivos do modelo
    do mundo. O planeador recebe os objetivos e o modelo de planeamento
    e através de deliberação as acções são então escolhidas e organizadas
    delineando um plano de acção que visa a alcançar todos os objetivos
    da forma mais eficiente possível
    """

    @abstractmethod
    def planear(self, modelo_plan, objetivos):
        """
        Método abstrato que quando implementado permite delinar o plano
        de acção do agente para atingir o próximo objetivo
        """

    @abstractmethod
    def obter_accao(self, estado):
        """
        Método abstrato quando implementado permite obter o operador que
        permite a mudança de estado, ou seja, obter a acção que o agente
        efectua para um estado fornecido
        """

    @abstractmethod
    def plano_valido(self, estado):
        """
        Método abstrato que após a implementação permite verificar a
        validade do plano
        """

    @abstractmethod
    def terminar_plano(self):
        """
        Método abstrato que quando implementado permite terminar o plano
        quando executado o método
        """
