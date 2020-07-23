# -*- coding: utf-8 -*-
# Bibliotecas utilizadas
import math
import numpy as np
from matplotlib import pyplot as plt

# Arquivos utilizados
import vetores
import euler
import crank_nicolson
import tarefa1
import tarefa2

# Função principal que recebe os valores de N e Lambda, 
# além das escolhas do usuário para definir a análise
def execucao(N,lbd,escolha,escolha1,escolha2,escolha3,p):
    # Definição do delta T e delta X com base no enunciado
    if escolha1 == 1:
        deltaX = 1/N                       
        deltaT = lbd*(deltaX)**2  
    else:
        deltaT = deltaX = 1/N
    M = int(round(1/deltaT))    # Calculado a partir do N

    # Criação das matrizes que serão usadas:
    # Matrizes da função u(t,x)
    u_a1 = np.zeros((M+1,N+1))    
    u_a1_mod = np.zeros((M+1,N+1))   
    u_a2 = np.zeros((M+1,N+1))    
    u_a2_mod = np.zeros((M+1,N+1))    
    u_b = np.zeros((M+1,N+1))        
    u_b_mod = np.zeros((M+1,N+1))     
    u_c = np.zeros((M+1,N+1))

    u_p =  np.zeros((M+1,N+1))      

    # Vetores dos valores de "t" e "x"
    VT = np.zeros(M+1)
    VX = np.zeros(N+1)

    # Listas da matriz "b" definidas na equação 29 do enunciado
    b_a1 = np.zeros(N-1)
    b_a2 = np.zeros(N-1)
    b_b = np.zeros(N-1)
    b_c = np.zeros(N-1)

    b_p = np.zeros(N-1)

    # Matriz para resolução do sistema LDLt*x = b
    B = np.zeros(N-1)

    # Criação dos vetores referentes à matriz A
    if (escolha2 == 2 or escolha == 2):
        VA1,VA2 = vetores.vetores_A(N,lbd/2)
    else:
        VA1,VA2 = vetores.vetores_A(N,lbd)
    
    # Decomposição da matriz A
    VD,VL = vetores.decomposicao_cholesky(VA1,VA2,N)

    for k in range (M+1):
        for i in range(N+1):

            # Definição dos vetores de "t" e "x"
            VT[k] = k*deltaT
            VX[i] = i*deltaX

            # Definição das matrizes que representam as soluçẽos exatas
            u_a1_mod[k,i] = 10*VT[k]*(VX[i]**2)*(VX[i]-1)
            u_a2_mod[k,i] = (1+math.sin(10*VT[k]))*(VX[i]**2)*((1-VX[i])**2)
            u_b_mod[k,i] = math.exp((VT[k])-(VX[i]))*math.cos(5*(VX[i])*(VT[k]))

            # Execução dos loops com base nas escolhas definidas
            if escolha == 1:
                if escolha1 == 1:           # Tarefa 1    
                    if escolha3 == 1:
                        tarefa1.a1(k,i,M,N,deltaT,deltaX,u_a1)
                    elif escolha3 == 2:
                        tarefa1.a2(k,i,M,N,deltaT,deltaX,u_a2)
                    elif escolha3 == 3:
                        tarefa1.b(k,i,M,N,deltaT,deltaX,u_b)
                    else:
                        tarefa1.c(k,i,M,N,deltaT,deltaX,u_c)
                else:                       # Tarefa 2
                # As funções da tarefa 2 retornam as fronteiras de u(t,x) 
                # para a solução numérica e as matrizes "b"

                    if escolha2 == 1:           # Euler
                        if escolha3 == 1:
                            euler.a1(N,M,lbd,k,i,deltaT,deltaX,u_a1,b_a1)
                        elif escolha3 == 2:
                            euler.a2(N,M,lbd,k,i,deltaT,deltaX,u_a2,b_a2)
                        elif escolha3 == 3: 
                            euler.b(N,M,lbd,k,i,deltaT,deltaX,u_b,b_b)
                        else:
                            euler.c(N,M,lbd,k,i,deltaT,deltaX,u_c,b_c)
                    else: 
                  # Crank-Nicolson
                        if escolha3 == 1:
                            crank_nicolson.a1(N,M,lbd/2,k,i,deltaT,deltaX,u_a1,b_a1)
                        if escolha3 == 2:
                            crank_nicolson.a2(N,M,lbd/2,k,i,deltaT,deltaX,u_a2,b_a2)
                        elif escolha3 == 3: 
                            crank_nicolson.b(N,M,lbd/2,k,i,deltaT,deltaX,u_b,b_b)
                        else:
                            crank_nicolson.c(N,M,lbd/2,k,i,deltaT,deltaX,u_c,b_c)
            else:
            # Parte 2
                crank_nicolson.parte2(N,M,lbd/2,k,i,deltaT,deltaX,u_p,b_p,p)

        if k < M and (escolha1 == 2 or escolha == 2):
            # Funções recursivas para chegar na solução numérica final 
            # usando as matrizes "b"
            i = 1
            if escolha3 == 1:
                #tarefa2.recursiva_u(i,k,N,u_a1,b_a1,VL,VD)             # Solução LDLt*x = b pelo método recursivo
                tarefa2.B(N,b_a1,VL,B)                                  # Solução LDLt*x = b por loop simples
                tarefa2.resolucao(N,k,u_a1,B,VL,VD)
            elif escolha3 == 2:
                #tarefa2.recursiva_u(i,k,N,u_a2,b_a2,VL,VD)
                tarefa2.B(N,b_a2,VL,B)
                tarefa2.resolucao(N,k,u_a2,B,VL,VD)
            elif escolha3 == 3:
                #tarefa2.recursiva_u(i,k,N,u_b,b_b,VL,VD)
                tarefa2.B(N,b_b,VL,B)
                tarefa2.resolucao(N,k,u_b,B,VL,VD)
            elif escolha3 == 4:
                #tarefa2.recursiva_u(i,k,N,u_c,b_c,VL,VD)
                tarefa2.B(N,b_c,VL,B)
                tarefa2.resolucao(N,k,u_c,B,VL,VD)
            elif escolha == 2:
                # Parte 2
                #tarefa2.recursiva_u(i,k,N,u_p,b_p,VL,VD)       
                tarefa2.B(N,b_p,VL,B)
                tarefa2.resolucao(N,k,u_p,B,VL,VD)

    # Retorno de cada letra
    if escolha3 == 1:
        return M, u_a1, u_a1_mod, VX, VT
    elif escolha3 == 2:
        return M, u_a2, u_a2_mod, VX, VT
    elif escolha3 == 3:
        return M, u_b, u_b_mod, VX, VT
    elif escolha3 == 4:
        return M, u_c, VX, VT
    elif escolha == 2:
        return M, u_p, VX, VT
