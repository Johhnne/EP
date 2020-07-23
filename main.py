# -*- coding: utf-8 -*-
# Arquivos utilizados
import graficos
import loop_principal
import erros
import parte2

# Biblioteca utilizada
from matplotlib import pyplot as plt

# Biblioteca usada para o calculo do tempo de execução
import time

def main():

    ini = time.time()           # Função para obter o tempo de execução

    # Métodos de escolhas para determinar a situação a ser analisada
    escolha = int(input("\n\nDIGITE 1 PARA PARTE 1 OU 2 PARA PARTE 2: "))

    if escolha == 1:
    # Parte 1
        escolha1 = int(input("\n\nANÁLISE GRÁFICA E ERROS \n\n>DIGITE 1 PARA UMA ANÁLISE DA TAREFA 1 OU 2 PARA ANÁLISE DA TAREFA 2: "))

        if escolha1 == 1:           # Tarefa 1

            print("\n\n>CONDIÇÕES INICIAIS:")
            N = int(input("> N: "))
            lbd = float(input("> λ: "))

            escolha3 = int(input("\n\n>DIGITE 1 PARA LETRA 'A1', 2 PARA LETRA 'A2', 3 PARA LETRA 'B' OU 4 PARA LETRA 'C':"))

            if escolha3 == 1:       # Letra 'A1'

                # A função 'execucao' no arquivo 'loop_principal' executa método numérico dependendo da letra escolhida
                # e retorna a resolução representadas por matrizes 'u' e também as matrizes modelos determinadas pelo
                # método exato para servir de comparação, além dos vetores VX e VT que contém os valores de 'x' e de 't'
                # respectivamente, e o valor de M calculado com base no valor de N
                M, u_a1, u_a1_mod, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,0,escolha3,0)
                erros.erro(N,M,u_a1,u_a1_mod,"'A1'")                                        # Calcula o erro em relação ao modelo
                graficos.mapa_unico(u_a1,VX,VT,"Letra 'A1'")                                # Mostra o gráfico em mapa de calor para a solução numérica
                graficos.mapa_duplo(u_a1,u_a1_mod,VX,VT,"Letra A1","Modelo letra 'A1'")     # Mostra o gráfico em mapa de calor para a solução numérica (esquerda) e exata (direita)
        
            elif escolha3 == 2:     # Letra 'A2'

                M, u_a2, u_a2_mod, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,0,escolha3,0)
                erros.erro(N,M,u_a2,u_a2_mod,"'A2'")
                graficos.mapa_unico(u_a2,VX,VT,"Letra 'A2'")
                graficos.mapa_duplo(u_a2,u_a2_mod,VX,VT,"Letra A2","Modelo letra 'A2'")

            elif escolha3 == 3:     # Letra 'B'

                M, u_b,u_b_mod, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,0,escolha3,0)
                erros.erro(N,M,u_b,u_b_mod,"'B'")
                graficos.mapa_unico(u_b,VX,VT,"Letra 'B'")
                graficos.mapa_duplo(u_b,u_b_mod,VX,VT,"Letra 'B'","Modelo letra 'B'")

            elif escolha3 == 4:                   # Letra 'C'

                M, u_c, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,0,escolha3,0)         # No caso da letra 'C' não sabemos a solução exata
                graficos.mapa_unico(u_c,VX,VT,"Letra 'C'")

            # Exceção para número digitado além do especificado
            else:
                print("Número errado")

        elif escolha1 == 2:         # Tarefa 2
            # Condições iniciais
            print("\n\n>CONDIÇÕES INICIAIS:")
            N = int(input("> N: "))
            lbd = N

            escolha2 = int(input("\n\n>DIGITE 1 PARA MÉTODO EULER OU 2 PARA MÉTODO CRANK-NICOLSON: "))

            if escolha2 == 1:       # Método Euler

                escolha3 = int(input("\n\n>DIGITE 1 PARA LETRA 'A1', 2 PARA LETRA 'A2', 3 PARA LETRA 'B' OU 4 PARA LETRA 'C': "))

                if escolha3 == 1:   # Letra 'A1'

                    M, u_a1,u_a1_mod, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,escolha2,escolha3,0)
                    erros.erro(N,M,u_a1,u_a1_mod,"'A1'")
                    graficos.mapa_duplo(u_a1,u_a1_mod,VX,VT,"Letra A1 - método euler","Modelo letra A1")
                    graficos.mapa_unico(u_a1,VX,VT,"Letra A1 - método euler")

                elif escolha3 == 2: # Letra 'A2'

                    M, u_a2,u_a2_mod, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,escolha2,escolha3,0)
                    erros.erro(N,M,u_a2,u_a2_mod,"'A2'")
                    graficos.mapa_duplo(u_a2,u_a2_mod,VX,VT,"Letra A2 - método euler","Modelo letra A2")
                    graficos.mapa_unico(u_a2,VX,VT,"Letra A2 - método euler")

                elif escolha3 == 3: # Letra 'B'

                    M, u_b,u_b_mod, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,escolha2,escolha3,0)
                    erros.erro(N,M,u_b,u_b_mod,"'B'")
                    graficos.mapa_duplo(u_b,u_b_mod,VX,VT,"Letra B - método euler","Modelo letra B")
                    graficos.mapa_unico(u_b,VX,VT,"Letra B - método euler")

                elif escolha3 == 4: # Letra 'C'

                    M, u_c, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,escolha2,escolha3,0)
                    graficos.mapa_unico(u_c,VX,VT,"Letra C - método euler")

                else:
                    print("Número errado")

            elif escolha2 == 2:     # Método Crank-Nicolson

                escolha3 = int(input("\n\n>DIGITE 1 PARA LETRA 'A1', 2 PARA LETRA 'A2', 3 PARA LETRA 'B' OU 4 PARA LETRA 'C': "))

                if escolha3 == 1:   # Letra 'A1'
                    
                    M, u_a1,u_a1_mod, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,escolha2,escolha3,0)
                    erros.erro(N,M,u_a1,u_a1_mod,"'A1'")
                    graficos.mapa_duplo(u_a1,u_a1_mod,VX,VT,"Letra A1 - método crank-nicolson","Modelo letra A1")
                    graficos.mapa_unico(u_a1,VX,VT,"Letra A1 - método crank-nicolson")

                elif escolha3 == 2: # Letra 'A2'

                    M, u_a2,u_a2_mod, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,escolha2,escolha3,0)
                    erros.erro(N,M,u_a2,u_a2_mod,"'A2'")
                    graficos.mapa_duplo(u_a2,u_a2_mod,VX,VT,"Letra A2 - método crank-nicolson","Modelo letra A2")
                    graficos.mapa_unico(u_a2,VX,VT,"Letra A2 - método crank-nicolson")
                elif escolha3 == 3: # Letra 'B'

                    M, u_b,u_b_mod, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,escolha2,escolha3,0)
                    erros.erro(N,M,u_b,u_b_mod,"'B'")
                    graficos.mapa_duplo(u_b,u_b_mod,VX,VT,"Letra B - método crank-nicolson","Modelo letra B")
                    graficos.mapa_unico(u_b,VX,VT,"Letra B - método crank-nicolson")

                elif escolha3 == 4: # Letra 'C'

                    M, u_c, VX, VT = loop_principal.execucao(N,lbd,escolha,escolha1,escolha2,escolha3,0)
                    graficos.mapa_unico(u_c,VX,VT,"Letra C - método crank-nicolson")
                else:
                    print("Número errado")
            else:
                print("Número errado")
        else:
            print("Número errado")

    elif escolha == 2:
    # Parte 2
        escolha2 = int(input("\n\n>DIGITE 1 PARA LETRA 'A', 2 PARA LETRA 'B', 3 PARA LETRA 'C' OU 4 PARA LETRA 'D': "))
        # Excecução dos testes a partir do molde da Parte 1
        if escolha2 == 1:
            parte2.testes(128,escolha2)
        elif escolha2 == 2:
            parte2.testes(128,escolha2)
        else:
            # Condições iniciais
            N = int(input("> N: "))
            if escolha2 == 3:
                parte2.testes(N,escolha2)
            elif escolha2 == 4:
                parte2.testes(N,escolha2)
            else:
                print("Número errado")
    else:
        print("Número errado")

    fim = time.time()           # Função para obter o tempo de execução

    print("Tempo de execução desta análise:", round(fim-ini,2),"segundos")

if __name__ == "__main__":
    main()
