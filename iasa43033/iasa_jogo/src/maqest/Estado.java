package maqest;

import java.util.HashMap;
import java.util.Map;

/**
 * Classe que representa um estado genérico de um agente. Esta classe permite
 * definir os vários estados de um agente bem como os estados para o qual este
 * transita perante diferentes eventos, para tal esta classe permite definir um
 * nome e é criado um HashMap<>() que faz corresponder a este estado os estados
 * sucessores do agente, ou seja, os estados para o qual o agente pode transitar,
 * e as acções a serem tomadas pelo agente no momento da transição para o novo
 * estado.
 * 
 * @author David Nunes
 * @version %I%, %G%
 * @see Map
 * @see HashMap
 * @see Transicao
 */

public class Estado<EV, AC> {

    private String nome;
    private Map<EV, Transicao<EV, AC>> transicoes;

    /**
     * Método construtor da classe Estado, recebe o nome a atribuir ao mesmo
     * e inicializa um HashMap<>() para este estado. Este HashMap deverá ser
     * populado com as transições de estado através do método transicao.
     * @param nome nome a atribuir ao estado
     * @see #transicao
     */
    public Estado(String nome) {
        this.nome = nome;
        transicoes = new HashMap<>();
    }

    /**
     * 
     * @param evento
     * @return
     */
    public Transicao<EV, AC> processar(EV evento) {
        return transicoes.get(evento);
    }

    /**
     * 
     * @param evento
     * @param estadoSucessor
     * @return
     */
    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /**
     * Método mais generalizado da transição que permite popular o HashMap criado com as
     * transições de estado correspondentes, ou seja, permite mapear ao estado atual do
     * agente definido uma transição composta por um evento ocorrido no ambiente, o estado 
     * para o qual o agente deverá transitar e a acção que o mesmo deve praticar durante
     * essa transição.
     * @param evento            evento que ocorreu no ambiente
     * @param estadoSucessor    estado para o qual o agente deverá transitar
     * @param accao             accção que o agente deve tomar durante a transição
     * @return                  a própria função
     */
    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor, AC accao) {
        transicoes.put(evento, new Transicao<EV, AC>(estadoSucessor, accao));
        return this;
    }

    /**
     * Método getter do nome do estado.
     * @return nome atribuído ao estado
     */
    public String getNome() {
        return nome;
    }

}
