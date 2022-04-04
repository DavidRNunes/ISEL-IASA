from ecr.comportComp import ComportComp

"""
Classe que implementa a classe abstrata ComportComp correspondente aos
comportamentos compostos, implementando o tipo de comportamento mediante
a selecção de acção, ou seja, perante comportamentos compostos estes podem
ser abordados de várias formas diferentes dependendo da selecção da acção
pretendida, nomeadamente hierarquia, prioridade ou fusão. Neste caso a
classe implementa hierarquia, que se traduz numa supressão das reacções
que se encontram mais abaixo na hierarquia, sendo executada a que se encontra
no topo da hierarquia.
"""
class Hierarquia(ComportComp):

    """
    Método que retorna a acção mais prioritária da hierarquia fixa.
    Por convenção admite-se que o utilizador da Hierarquia organiza
    a prioridade dos comportamentos compostos por ordem numérica
    crescente, ou seja, o primeiro comportamento da lista é o mais
    prioritário. Esta conveção leva a que as acções recebidas na classe
    hierarquia já vêm previamente ordenadas por prioridade, fazendo
    da lista recebida a acção prioritária a primeira entrada da lista
    recebida, pelo que retornamos a mesma.
    @args accoes - lista de acções correspondentes aos comportamentos
    @returns accoes[0] - acção prioritária da hierarquia
    """
    def seleccionar_accao(self, accoes):
        if accoes:
            return accoes[0]