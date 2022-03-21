package maqest;

/**
 * Classe transitória entre estados que guarda os valores do estado seguinte
 * e da acção a tomar pelo agente. Representa o estado transitório entre dois
 * estados, sendo utilizado pela classe de Estado para definir as transições
 * de cada estado, recorrendo a um HashMap.
 * 
 * @author David Nunes
 * @version %I%, %G%
 * @see Estado
 */

public class Transicao<EV, AC> {

    private Estado<EV, AC> estadoSucessor;
    private AC accao;

    /**
     * Método construtor da classe, recebe o estado sucessor e a acção à qual
     * deve ser associada a transição
     * @param estadoSucessor
     * @param accao
     */
    public Transicao(Estado<EV, AC> estadoSucessor, AC accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    /**
     * Método que permite obter o estado que se sucede ao estado atual, ou
     * seja, o estado para o qual o agente vai transitar.
     * 
     * @return estado seguinte do agente
     */
    public Estado<EV, AC> getEstadoSucessor() {
        return estadoSucessor;
    }

    /**
     * Método que permite obter a acção de transição para a transição
     * definida.
     * 
     * @return acção a praticar pelo agente
     */
    public AC getAccao() {
        return accao;
    }
    
}
