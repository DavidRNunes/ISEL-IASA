package Jogo.Personagem;

import Jogo.Ambiente.Ambiente;
import Jogo.Ambiente.Evento;

/**
 * Personagem é a classe representante de um agente inteligente que interage com um 
 * jogador humano. Considera-se um agente algo que seja capaz de percepcionar o seu
 * ambiente através de sensores e actuar sobre esse mesmo ambiente através de 
 * actuadores. No nosso caso tratamos um agente inteligente pois este processa a 
 * informação que obtém e actua sobre a mesma racionalmente - actua no sentido de 
 * conseguir o melhor resultado possível perante os objetivos pretendidos. Neste 
 * sentido, a classe Personagem faz parte da classe Jogo (agregação) e percepciona
 * o ambiente que a rodeia através da classe Ambiente (associação) e interage com o
 * mesmo recorrendo à classe Controlo (composição de Personagem).
 * 
 * @author David Nunes
 * @version %I%, %G%
 * @see Jogo
 * @see Ambiente
 * @see Percepcao
 * @see Controlo
 */

public class Personagem {

    private Controlo controlo = new Controlo();
    private Ambiente ambiente;

    /**
     * Método construtor da classe Personagem.
     * Recebe o ambiente no qual o agente se encontra inserido e atualiza o valor
     * global da classe.
     * 
     * @param ambiente ambiente no qual o agente se insere
     */
    public Personagem(Ambiente ambiente) {
        this.ambiente = ambiente;
    }

    /**
     * Método que atualiza o agente.
     * O agente percepciona o ambiente no qual se insere recorrendo ao método
     * percepcionar() e de seguida processa a informação obtida através do método
     * processar() da classe Controlo, que lhe irá devolver uma acção de acordo com
     * o objetivo pretendido. Por último o agente actua sobre essa acção através do
     * método actuar().
     * 
     * @see Percepcao
     * @see Accao
     * @see Controlo#processar(Percepcao)
     * @see #actuar(Accao)
     */
    public void executar() {
        Percepcao percepcao = percepcionar();
        Accao accao = controlo.processar(percepcao);
        actuar(accao);
    }

    /**
     * Método que recebe a acção que o agente deve executar e executa-a.
     * 
     * @param accao acção a executar
     */
    private void actuar(Accao accao) {
        if (accao != null) {
            System.out.printf("Accao: %s\n", accao);
        }
    }

    /**
     * Método que permite ao agente observar o ambiente onde se encontra inserido e
     * obter informações relativas ao mesmo. Neste caso é obtido o evento atual do
     * ambiente e é devolvido esse mesmo valor.
     * 
     * @return percepção obtida do ambiente (evento atual de ambiente)
     * @see Percepcao
     */
    private Percepcao percepcionar() {
        Evento evento = ambiente.getEvento();
        Percepcao percepcao = new Percepcao(evento);

        return percepcao;
    }

}
