package Jogo.personagem;

import Jogo.ambiente.Evento;

/**
 * Classe que simula a percepção de um agente.
 * Esta classe obtém um evento e permite a outras classes obter o
 * evento atual que foi observado. É através desta classe que se simula
 * a capacidade do agente observar o ambiente que o rodeia e reter essa
 * informação de forma que a mesma seja posteriormente processada para
 * ser tomada uma acção sobre ela.
 * 
 * @author David Nunes
 * @version %I%, %G%
 * @see Controlo
 * @see Evento
 */

public class Percepcao {

    private Evento evento;

    /**
     * Método construtor da classe Percepcao. Recebe um evento da classe
     * Evento e atuliza o valor do evento na classe Percepcao. O evento
     * recebido corresponde ao estado atual do ambiente que está a ser
     * percepcionado pelo agente.
     * 
     * @param evento estado atual do ambiente a ser observado
     */
    public Percepcao(Evento evento) {
        this.evento = evento;
    }

    /**
     * Método público getter que permite a outras classes obter o valor
     * atual do evento percepcionado.
     * 
     * @return valor atual de evento
     */
    public Evento getEvento() {
        return evento;
    }

}
