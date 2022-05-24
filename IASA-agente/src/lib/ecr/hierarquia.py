from ecr import ComportComp


class Hierarquia(ComportComp):
    """
    Classe que implementa a classe abstrata ComportComp correspondente aos
    comportamentos compostos implementando a selecção de acção sob forma de
    hierarquia

    A hierarquia consiste na supressão e substituição das acções fornecidas
    pelas várias reacções inseridas no comportamento que se encontram nos
    níveis inferiores de uma hierarquia fixa predefinida em função da acção
    que se encontra no topo da hierarquia, sendo esta a acção selecionada
    para ser executada pelo agente

    @method seleccionar_accao: método que retorna a acção que se encontra
        no topo da hierarquia
    """

    def seleccionar_accao(self, accoes):
        """
        Método que retorna a acção que se encontra no topo da hierarquia

        Por convenção admite-se que o utilizador da hierarquia organiza
        previamente a prioridade dos comportamentos compostos por ordem
        numérica crescente, fornecendo os comportamentos já ordenados para
        a lista, sendo o primeiro comportamento fornecido aquele que se
        encontra no topo da mesma. Esta convenção leva a que o método a
        implementar apenas necessite de retornar a primeira entrada da
        lista, uma vez que esta é acção prioritária e aquela que deve ser
        executada pelo agente

        @param accoes: lista de acções
        @returns: a acção que se encontra no topo da hierarquia
        """
        if accoes:
            return accoes[0]
