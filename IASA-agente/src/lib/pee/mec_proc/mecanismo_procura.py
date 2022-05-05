from abc import ABC, abstractmethod
from pee.mec_proc.no import No
from pee.solucao import Solucao
from mod.estado import Estado
from mod.operador import Operador
from mod.problema.problema import Problema
from pee.mec_proc.fronteira.fronteira import Fronteira


class MecanismoProcura(ABC):
    """
    Classe abstrata que define um mecanismo de procura 
    
    Mecanismo de procura é um algoritmo que recebe um problema e percorre
    um espaço de estados até encontrar uma solução ou uma indicação de 
    falha (inexistência de solução). A forma como o espaço de estados é 
    percorrido é a única diferença entre os vários mecanismos de procura,
    traduzindo-se em algoritmos de diferente complexidade computacional.

    @method resolver: implementa o algoritmo de resolução do problema
    @method _expandir: expande o nó fornecido através dos seus operadores
        retornando a lista de nós filho a adicionar à fronteira
    @method _iniciar_fronteira: inicia a fronteira vazia do mecanismo
    @method _memorizar: adiciona o nó fornecido à fronteira
    """

    _fronteira: Fronteira

    def __init__(self):
        """
        Método construtor da classe inicia a fronteira do problema
        como uma lista vazia
        """
        self._iniciar_fronteira()
    
    def resolver(self, problema):
        """
        Implementa o algoritmo de resolução base de todos os mecanismos
        de procura

        Establece o nó inicial como sendo o estado inicial do problema e
        associa-lhe os operadores da transformação de estado. Este nó é
        inserido na fronteira de exploração e de seguida é analisada a 
        fronteira até que esta fique vazia ou retorne a solução do problema
        após percorrer todos os estados do espaço de estados - remove-se os
        nós em estudo da fronteira e avaliando se são a solução pretendida
        caso contrário adicionam-se os nós-filho à fronteira e repete-se
        o ciclo de exploração.

        @param problema: estado inicial do agente, operadores e objetivos
        @returns: solução do problema ou None caso não haja solução
        """
        no = No(problema.estado_inicial, problema.operadores)
        self._fronteira.inserir(no)
        while not self._fronteira.vazia():
            no = self._fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)
            for noSuc in self._expandir(problema, no):
                self._memorizar(noSuc)
        return None

    def _expandir(self, problema, no):
        """
        Método que expande a fronteira de exploração através dos operadores
        do nó actual

        Percorre os operadores do nó actual e retorna os novos nós gerados,
        denominados de nós-filho ou nós sucessores, associados ao estado
        resultante de cada operador

        @param problema: estado inicial do agente, operadores e objetivos
        @param no: nó que se pretende expandir (nó em estudo)
        @returns: lista de nós filho do nó fornecido - nós a adicionar à
            fronteira de exploração do espaço de estados
        """
        for operador in problema.operadores:
            estado_suc = operador.aplicar(no.estado)
            if estado_suc:
                yield No(estado_suc, operador, no)
    
    @abstractmethod
    def _iniciar_fronteira(self):
        """
        Método abstrato que inicia a fronteira associada ao mecanismo em
        causa
        
        @returns: fronteira do mecanismo vazia
        """

    @abstractmethod
    def _memorizar(self, no):
        """
        Método que permite adicionar nós à fronteira de exploração em
        diferentes locais tendo em conta o tipo de fronteira

        @param no: nó que se pretende memorizar (adicionar à fronteira)
        """