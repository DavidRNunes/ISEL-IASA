from ecr.comportComp import ComportComp

"""
Classe que implementa a classe abstrata ComportComp correspondente aos
comportamentos compostos, implementando o tipo de comportamento mediante
a selecção de acção, ou seja, perante comportamentos compostos estes podem
ser abordados de várias formas diferentes dependendo da selecção da acção
pretendida, nomeadamente hierarquia, prioridade ou fusão. Neste caso a
classe implementa a Prioridade, onde as respostas são selecionadas de
acordo com uma prioridade associada que varia ao longo do tempo. Esta
prioridade é definida nas próprias acções, sendo, por exemplo, a distância
que o agente se encontra de um enimigo. A classe percorre a lista de acções
e retorna a acção com maior prioridade para ser executada.
"""
class Prioridade(ComportComp):

    """
    Método que permite percorrer a lista de acções dos comportamentos
    e seleciona a acção com maior prioridade, que, na implementação
    deste jogo corresponde à variável prioridade, cujo valor é um int
    superior a 0. O parâmetro key define qual o parâmetro a que o max
    se aplica, sendo o max a função que permite obter o maior int na lista
    """
    def seleccionar_accao(self, accoes):
        if accoes:
            return max(accoes, key=lambda accao: accao.prioridade)