package Jogo.Ambiente;

/**
 * Enumerador que representa os vários eventos imutáveis possíveis de ocorrer num
 * ambiente, com o qual este enumerador se associa. Estes eventos podem ainda ser
 * percepcionados por um agente através da classe Percepcao.
 * 
 * @author David Nunes
 * @version %I%, %G%
 * @see Ambiente
 * @see Percepcao
 */

public enum Evento {
    
    SILENCIO,
    RUIDO,
    ANIMAL,
    FUGA,
    FOTOGRAFIA,
    TERMINAR

}
