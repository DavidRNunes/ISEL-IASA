package Jogo.Ambiente;

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
    }

    /**
     * Método a implementar que gera um novo evento.
     * 
     * @return evento gerado
     */
    private Evento gerarEvento() {
        return null;
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
