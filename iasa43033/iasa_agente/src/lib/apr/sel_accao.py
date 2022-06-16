from abc import ABC, abstractmethod


class SelAccao(ABC):
    """
    Interface que representa uma estratégia de selecção de acção

    Esta interface quando implementada permite selecionar uma acção
    através de uma estratégia, por exemplo uma estratégia sôfrega onde
    a acção selecionada é aquela que retorna o melhor valor Q(a), ou
    uma outra que pode selecionar a acção através de uma probabilidade,
    selecionando a melhor acção ou uma outra acção aleatória que permita
    ao agente explorar o mundo que o rodeia, evitando executar sempre a
    primeira acção que lhe proporcionou ganhos a curto prazo - estratégia
    que permite obter a melhor linha de acção no mundo

    @method seleccionar_accao: método que quando implementado seleciona
        a acção a executar pelo agente mediante uma estratégia
    """

    @abstractmethod
    def seleccionar_accao(self, s):
        """
        Método abstrato que quando implementado seleciona a acção a
        efectuar para o estado fornecido

        @param s: estado actual do agente
        """
