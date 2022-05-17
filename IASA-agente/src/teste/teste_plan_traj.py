from teste.plan_traj.ligacao import Ligacao
from teste.plan_traj.planeador_trajeto import PlaneadorTrajeto

"""
Implementação do modelo do problema de planeamento de trajetos

É criada a lista de ligações entre localidades tal como no fornecida
no enunciado e é dada uma localidade inicial e um objetivo final à
escolha. Perante o mecanismo de procura definido no planeador (classe
PlaneadorTrajeto) é obtida uma solução encontrada por esse mecanismo
sendo depois imprimida para a consola recorrendo ao método mostrar_trajeto
da classe do planeador.
"""

ligacoes = [
    Ligacao("Loc-0", "Loc-1", 5),
    Ligacao("Loc-0", "Loc-2", 25),
    Ligacao("Loc-1", "Loc-3", 12),
    Ligacao("Loc-1", "Loc-6", 5),
    Ligacao("Loc-2", "Loc-4", 30),
    Ligacao("Loc-3", "Loc-2", 10),
    Ligacao("Loc-3", "Loc-5", 5),
    Ligacao("Loc-4", "Loc-3", 2),
    Ligacao("Loc-5", "Loc-6", 8),
    Ligacao("Loc-5", "Loc-4", 10),
    Ligacao("Loc-6", "Loc-3", 15)
]

"""
Aplicação de teste complementar
"""
ligacoes_complementar = [
    Ligacao("Loc-0", "Loc-1", 5),
    Ligacao("Loc-0", "Loc-2", 25),
    Ligacao("Loc-0", "Loc-7", 7),
    Ligacao("Loc-1", "Loc-3", 12),
    Ligacao("Loc-1", "Loc-6", 5),
    Ligacao("Loc-2", "Loc-7", 5),
    Ligacao("Loc-2", "Loc-8", 15),
    Ligacao("Loc-2", "Loc-4", 30),
    Ligacao("Loc-3", "Loc-2", 10),
    Ligacao("Loc-3", "Loc-5", 5),
    Ligacao("Loc-4", "Loc-3", 2),
    Ligacao("Loc-5", "Loc-6", 8),
    Ligacao("Loc-5", "Loc-9", 1),
    Ligacao("Loc-5", "Loc-4", 10),
    Ligacao("Loc-6", "Loc-3", 15),
    Ligacao("Loc-7", "Loc-8", 8),
    Ligacao("Loc-8", "Loc-4", 25),
    Ligacao("Loc-9", "Loc-6", 2),
    Ligacao("Loc-9", "Loc-10", 2),
    Ligacao("Loc-10", "Loc-4", 2)
]


loc_inicial = "Loc-0"
loc_final = "Loc-3"
planeador = PlaneadorTrajeto()
solucao = planeador.planear(ligacoes, loc_inicial, loc_final)
planeador.mostrar_trajecto(solucao)

