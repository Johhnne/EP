# -*- coding: utf-8 -*-
# Bibliotecas utilizadas
import random
import math
import numpy as np
from matplotlib import pyplot as plt
import sys

# Arquivos utilizados
import loop_principal
import erros
import sistemas_2
import graficos
import barraDeProgresso

def testes(N,escolha2):
    lbd = N

    # Separação de cada teste
    if escolha2 == 1:
        uT, uk, nf = teste_a(N,lbd,escolha2)
    elif escolha2 == 2:
        uT, uk, nf = teste_b(N,lbd,escolha2)
    elif escolha2 == 3:
        uT, uk, nf = teste_c(N,lbd,escolha2)
    elif escolha2 == 4:
        uT, uk, nf = teste_d(N,lbd,escolha2)

    # Matrizes A e B da equação 40 do enunciado definida como A*X = B
    A = sistemas_2.matrizA(uk,nf,N)
    B = sistemas_2.matrizX(uT,uk,nf,N)

    # Decomposição da matriz A em LDLt
    L,D,Lt = sistemas_2.decomposicao(A)

    # Resolução do sistema, obtendo as intensidades "ak"
    X = sistemas_2.loop_resolucao(L,D,B,nf)
    
    # Mostra cada "ak"
    k = 0
    for a in X:
        print(f"a{k+1} =",round(a,5))
        k = k + 1

    # Define e mostra o erro quadrático
    erros.erro2(N,nf,uT,X,uk)

    # Calculo do uT final
    uTf = np.zeros(N-1)
    for i in range (N-1):
        for j in range (nf):
            uTf[i] = X[j]*uk[j,i] + uTf[i]
    
    if escolha2 == 3:
        graficos.linha(uTf,N,"Solução")
    elif escolha2 == 4:
        graficos.linha(uT,N,"uT recebido")
        graficos.linha(uTf,N,"Solução")


def teste_a(N,lbd,escolha2):
    nf = 1
    uk = np.zeros((nf,N-1))

    # Posição da forçante pontual
    p = 0.35          

    # Usando o método de Crank-Nicolson para chegar no uk
    M, u_p, VX, VT = loop_principal.execucao(N,lbd,2,0,escolha2,0,p)
    uk[:] = u_p[N,1:N]
    uT = 7*uk[0,:]
    return uT, uk, nf

def teste_b(N,lbd,escolha2):
    nf = 4
    uk = np.zeros((nf,N-1))
    uT = np.zeros(N-1)

    # Posição das forçantes pontuais
    P = np.array([0.15, 0.3, 0.7, 0.8])

    S = 0
    for p in P:
        M, u_p, VX, VT = loop_principal.execucao(N,lbd,2,0,escolha2,0,p)
        uk[S] = u_p[N,1:N]
        S = S + 1

    uT = 2.3*uk[0,:]+3.7*uk[1,:]+0.3*uk[2,:]+4.2*uk[3,:]
    return uT, uk, nf

def teste_c(N,lbd,escolha2):
    nf = 10

    # Matriz para armazenar os valores do arquivo teste.txt
    U = np.zeros(2059)

    # Leitura e armazenamento dos valores do arquivo teste.txt
    f = open("teste.txt","r")
    i = 0
    for line in f:
        for element in line.split():
            U[i] = element
            i = i+1

    # Barra de Progresso para auxiliar a utilização
    #########################################
    barraDeProgresso.printBarra(0, nf, prefixo = 'Progress:', suffixo = 'Complete', comprimento = 50)
    #########################################

    uk = np.zeros((nf,N-1))

    # Posição das forçantes pontuais
    P = U[0:10]


    S = 0
    for p in P:
        M, u_p, VX, VT = loop_principal.execucao(N,lbd,2,0,escolha2,0,p)
        uk[S] = u_p[N,1:N]
        ####################################
        barraDeProgresso.printBarra(S + 1, nf, prefixo = 'Progress:', suffixo = 'Complete', comprimento = 50)
        ####################################
        S = S + 1

    # Armazenamento dos valores de uT na matriz uT de acordo com o N 
    j = 2048/N
    uT = np.zeros(N-1)
    for k in range (N-1):
        uT[k] = U[int(10+(k+1)*j)]
    return uT, uk, nf

def teste_d(N,lbd,escolha2):
    nf = 10

    # Matriz para armazenar os valores do arquivo teste.txt
    U = np.zeros(2059)

    # Leitura e armazenamento dos valores do arquivo teste.txt
    f = open("teste.txt","r")
    i = 0
    for line in f:
        for element in line.split():
            U[i] = element
            i = i+1

    uk = np.zeros((nf,N-1))

    # Posição das forçantes pontuais
    P = U[0:10]

    # Barra de Progresso para auxiliar a utilização
    #########################################
    barraDeProgresso.printBarra(0, nf, prefixo = 'Progress:', suffixo = 'Complete', comprimento = 50)
    #########################################

    # Criação das matrizes de temperatura para chegar no uk usando o método de Crank-Nicolson
    S = 0
    for p in P:
        M, u_p, VX, VT = loop_principal.execucao(N,lbd,2,0,escolha2,0,p)
        uk[S] = u_p[N,1:N]
        ####################################
        barraDeProgresso.printBarra(S + 1, nf, prefixo = 'Progress:', suffixo = 'Complete', comprimento = 50)
        ####################################
        S = S + 1

    # Armazenamento dos valores de uT na matriz uT de acordo com o N
    # e um ruído definido por um número aleatório conforme o enunciado
    j = 2048/N
    uT = np.zeros(N-1)
    for k in range (N-1):
        uT[k] = (1+(2*(random.random()-0.5))*0.01)*U[int(10+(k+1)*j)]
    return uT, uk, nf
