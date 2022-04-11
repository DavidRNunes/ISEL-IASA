from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.explorar.explorar import Explorar
from controlo_react.reaccoes.recolher import Recolher
from sae import Controlo
from sae import Simulador

"""
Ambiente de teste dos controlos reactivos, fornece-se o comportamento
e pode-se testar o mesmo.

No caso de se pretender testar o comportamento explorativo do agente
recorremos ao comportamento explorar, que leva o agente a mover-se
de forma aleatória no ambiente que o rodeia, chocando com as paredes
(que podemos observar visualmente quando a cor do agente muda para
vermelho) e recolhendo alvos que aleatóriamente passe por cima.

No caso de se pretender testar o comportamento composto Recolher,
constituído pelos comportamentos AproximarAlvo, EvitarObst e Explorar,
podemos observar que o agente se desloca de uma forma muito menos
aleatória, uma vez que quando detecta um alvo o agente se desloca
directamente em direcção ao alvo, recolhendo-o e avaliando em todos
os momentos a proximidade de obstáculos, tanto que o agente com este
comportamento activo não choca com as paredes. O movimento do agente
torna-se errático como no comportamento explorativo apenas quando não
detecta nenhum alvo (situações que já tenha recolhido todos os alvos
presentes numa área e tenha de se deslocar para detectar outro alvo).
"""
# Ativação
explorar = Explorar()
recolher = Recolher()
controlo = ControloReact(recolher)
Simulador(1, controlo).executar()
