package Jogo.Personagem;

import Jogo.Ambiente.Evento;
import maqest.Estado;
import maqest.MaquinaEstados;

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

    private MaquinaEstados<Evento, Accao> maqEst;

    /**
     * Método construtor da classe, define os estados em que o personagem se pode
     * encontrar e, para cada estado, define os seus estados transitórios recorrendo
     * a uma máquina de estados. A máquina de estados irá controlar as transições que
     * ocorrem durante o loop de jogo, alterando o estado atual do personagem para os
     * estados aqui definidos.
     */
    public Controlo() {
        Estado<Evento, Accao> procura  = new Estado<>("Procura");
        Estado<Evento, Accao> inspeccao  = new Estado<>("Inspeccao");
        Estado<Evento, Accao> observacao  = new Estado<>("Observacao");
        Estado<Evento, Accao> registo  = new Estado<>("Registo");

        procura
            .transicao(Evento.RUIDO, inspeccao, Accao.APROXIMAR)
            .transicao(Evento.SILENCIO, procura, Accao.PROCURAR)
            .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR);

        inspeccao
            .transicao(Evento.RUIDO, inspeccao, Accao.PROCURAR)
            .transicao(Evento.SILENCIO, procura)
            .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR);

        observacao
            .transicao(Evento.FUGA, inspeccao)
            .transicao(Evento.ANIMAL, registo, Accao.OBSERVAR);

        registo
            .transicao(Evento.FUGA, procura)
            .transicao(Evento.FOTOGRAFIA, procura)
            .transicao(Evento.ANIMAL, registo, Accao.FOTOGRAFAR);

        maqEst = new MaquinaEstados<>(procura);
    }

    /**
     * Método que recebe a informação dos sensores do agente, que obtiveram
     * informações sobre o ambiente no qual este se insere, e processa essa
     * mesma informação, retornando a acção considerada ótima.
     * 
     * @param percepcao informações percepcionadas pelos sensores do agente
     * @return acção ótima a tomar
     */
    public Accao processar(Percepcao percepcao) {
        Evento evento = percepcao.getEvento();
        Accao accao = maqEst.processar(evento);
        mostrar();

        return accao;
    }

    /**
     * Método que imprime para a consola o estado actual do agente
     */
    private void mostrar() {
        System.out.printf("Estado: %s\n", getEstado().getNome());
    }

    /**
     * Método que pede à máquina de estados o estado atual do agente
     * 
     * @return estado atual do agente
     */
    public Estado<Evento, Accao> getEstado() {
        return maqEst.getEstado();
    }
    
}
