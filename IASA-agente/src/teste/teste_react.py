from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.explorar.explorar import Explorar
from sae import Controlo
from sae import Simulador

"""
Ambiente de teste dos controlos reactivos, fornece-se o comportamento
e pode-se testar o mesmo. Neste caso forneceu-se o comportamento
explorar e verificou-se que o agente explorava o campo de jogo aleatoriamente
"""
# Ativação
explorar = Explorar()
controlo = ControloReact(explorar)
Simulador(1, controlo).executar()
