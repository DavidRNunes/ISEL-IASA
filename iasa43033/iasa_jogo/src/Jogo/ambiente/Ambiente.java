package Jogo.ambiente;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Classe que representa um ambiente virtual dinâmico.
 * Esta classe é composta da classe Jogo, sendo definida pela mesma, e é caracterizada
 * pelos eventos que ocorrem no seu interior, ou seja, o ambiente virtual evolui ao
 * longo do tempo mediante os eventos que nele ocorrem e as interações que os agentes
 * nele inseridos têm com o mesmo, através da associação uni-direcional com a classe
 * Personagem.
 * 
 * @author David Nunes
 * @version %I%, %G%
 * @see Jogo
 * @see Personagem
 * @see Evento
 */

public class Ambiente {

    private Evento evento;
    private Scanner scanner = new Scanner(System.in);
    private Map<String, Evento> eventos;

    public Ambiente() {
        eventos = new HashMap<>();
        eventos.put("s", Evento.SILENCIO);
        eventos.put("r", Evento.RUIDO);
        eventos.put("a", Evento.ANIMAL);
        eventos.put("f", Evento.FUGA);
        eventos.put("p", Evento.FOTOGRAFIA);
        eventos.put("t", Evento.TERMINAR);
    }

    /**
     * Método que gera um novo evento de forma a alterar o estado do ambiente atual
     * e atualiza o mesmo. De momento faz uso dos métodos gerarEvento() e mostrar()
     * para o propósito.
     * 
     * @see #mostrar()
     * @see #gerarEvento()
     */
    public void evoluir() {
        evento = gerarEvento();
        mostrar();
    }

    /**
     * Método a implementar que atualiza o ambiente atual.
     */
    private void mostrar() {
        System.out.printf("Evento: %s\n", evento);
    }

    /**
     * Método a implementar que gera um novo evento.
     * "s" - silêncio; "r" - ruído; 
     * 
     * @return evento gerado
     */
    private Evento gerarEvento() {
        System.out.println("Evento? ");
        String comando = scanner.next();

        return eventos.get(comando);
    }

    /**
     * Método público getter que permite a outras classes obter o evento atual
     * do ambiente.
     * 
     * @return evento atual do ambiente
     */
    public Evento getEvento() {

        return evento;
    }
    
}
