package maqest;

/**
 * Classe de uma máquina de estados finitos genérica que recebe um estado atual
 * e retorna o estado futuro da entidade, ou seja, é fornecido o estado em que
 * se encontra um agente e, quando ocorre uma transformação do sistema, através
 * de um evento, esse evento é fornecido à máquina de estados que o processa de
 * acordo com as transições mapeadas para esse evento. A classe MaquinaEstados é
 * uma classe composta por Estados, que transitam mediante as transições
 * definidas na classe Transicao.
 * 
 * @author David Nunes
 * @version %I%, %G%
 * @see Estado
 * @see Transicao
 */

public class MaquinaEstados<EV, AC> {

    private Estado<EV, AC> estado;

    /**
     * Método contrutor da máquina de estados, recebe e define o estado atual
     * da máquina de estados.
     * 
     * @param estado estado inicial da máquina de estados
     */
    public MaquinaEstados(Estado<EV, AC> estado) {
        this.estado = estado;
    }

    /**
     * Método que processa o evento ocorrido e retorna a acção a tomar pelo
     * agente. Este método faz uso da classe Transicao para guardar os valores
     * obtidos pelo método processar() da classe Estado, ou seja, para o estado
     * atual do agente e perante o evento que se dá devolve a acção a tomar.
     * @param evento    evento ocorrido a processar
     * @return          null caso não haja uma transição de estado ou quando
     *                  não há ação a tomar; acção a tomar pelo agente
     */
    public AC processar(EV evento) {
        Transicao<EV, AC> transicao = estado.processar(evento);
        if (transicao != null) {
            estado = transicao.getEstadoSucessor();

            return transicao.getAccao();
        }

        return null;
    }

    /**
     * Método getter que permite a outras classes obter o estado atual
     * da máquina de estados.
     * 
     * @return estado atual da máquina de estados
     */
    public Estado<EV, AC> getEstado() {
        return estado;
    }
    
}
