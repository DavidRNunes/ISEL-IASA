package Jogo.Personagem;

/**
 * Classe que simula a componente de controlo de um agente. É nesta componente
 * que o agente processa a informação recebida pelos sensores (percepcionada),
 * raciocinando qual a acção adequada para as condições atuais do ambiente onde
 * se encontra. É nesta classe que o agente se torna verdadeiramente inteligente,
 * uma vez que é aqui que com o conhecimento que o agente dispõe é tomada uma
 * decisão considerada maximizadora do valor esperado da medida de desempenho
 * (neste caso, o objetivo ou finalidade). A classe Controlo faz com que o agente
 * em causa aplique uma arquitectura do modelo deliberativo, uma vez que entre
 * a percepção do ambientee a acção sobre o mesmo existe um momento de deliberação
 * sobre a acção a tomar.
 * 
 * @author David Nunes
 * @version %I%, %G%
 * @see Personagem
 * @see Percepcao
 * @see Accao
 */

public class Controlo {

    /**
     * Método que recebe a informação dos sensores do agente, que obtiveram
     * informações sobre o ambiente no qual este se insere, e processa essa
     * mesma informação, retornando a acção considerada ótima.
     * 
     * @param percepcao informações percepcionadas pelos sensores do agente
     * @return acção ótima a tomar
     */
    public Accao processar(Percepcao percepcao) {
        return null;
    }
    
}
