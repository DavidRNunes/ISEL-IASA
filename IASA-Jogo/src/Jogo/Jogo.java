package Jogo;

import Jogo.Ambiente.Ambiente;
import Jogo.Ambiente.Evento;
import Jogo.Personagem.Personagem;

/**
 * Classe executável pai que cria as restantes classes que compõem o jogo a
 * desenvolver,
 * composta ainda pelo loop de jogo.
 * O jogo consiste num abiente onde uma personagem interage com eventos através
 * de ações, tendo por objetivo registar a presença de animais recorrendo a
 * fotografias.
 * 
 * @author David Nunes
 * @version %I%, %G%
 * @see Ambiente
 * @see Personagem
 */

public class Jogo {

    private static Ambiente ambiente;
    private static Personagem personagem;

    /**
     * Ponto de entrada no jogo - main method. Cria um novo ambiente e uma nova
     * personagem inserida nesse ambiente e de seguida executa o método executar().
     * 
     * @param args Não utilizado
     * @see #executar()
     */
    public static void main(String[] args) {
        ambiente = new Ambiente();
        personagem = new Personagem(ambiente);

        executar();
    }

    /**
     * Loop de execução do jogo. Faz a personagem executar o seu próprio método
     * executar() e de seguida manda o ambiente executar o seu método evoluir()
     * que irá reagir às alterações provocadas pelo agente personagem. Este loop
     * de jogo só termina quando o ambiente chega ao estado de TERMINAR.
     * 
     * @see Personagem#executar()
     * @see Ambiente#evoluir()
     * @see Evento
     */
    private static void executar() {

        do {
            personagem.executar();
            ambiente.evoluir();
        } while (ambiente.getEvento() != Evento.TERMINAR);

    }

}
