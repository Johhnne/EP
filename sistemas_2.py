# -*- coding: utf-8 -*-
# Arquivos utilizados
import math
import numpy as np
from matplotlib import pyplot as plt


# Construção da matriz A pelos produtos internos
def matrizA(uk,nf,N):
    A = np.zeros((nf,nf))
    for i in range (nf):
        for j in range (nf):
            produtoInterno = [uk[j,k]*uk[i,k] for k in range (N-1)]
            A[i,j] = np.sum(produtoInterno)
    return A

# Construção da matriz X pelos produtos internos
def matrizX(uT,uk,nf,N):
    B = np.zeros(nf)
    for i in range(nf):
        produtoInterno = [uT[k]*uk[i,k] for k in range (N-1)]
        B[i] = np.sum(produtoInterno)
    return B

# Decomposição de cholesky para Matriz A
def decomposicao(A):
    M, M = np.shape(A)
    L = np.zeros((M,M))
    D = np.zeros((M,M))
    for j in range(M):
        for i in range (M):
            L[i,i] = 1
            if j == 0:
                D[j,j] = A[j,j]
                L[i,j] = A[i,j]/D[j,j]
            else:
                if i > j:
                    S1 = 0
                    for k in range (j):
                        S1 = L[i,k]*L[j,k]*D[k,k] + S1
                    L[i,j] = (A[i,j]-S1)/D[j,j]
                else:
                    S2 = 0
                    for k in range (j):
                        S2 = (L[j,k]**2)*D[k,k] + S2
                    D[j,j] = A[j,j] - S2
    Lt = np.transpose(L)
    return L,D,Lt

# Resolução do sistema LDLt*x = b por loop
# Essa resolução se divide em resolução de 3 sistemas menores
def loop_resolucao(L,D,B,nf):
    X = np.zeros(nf)
    Y = np.zeros(nf)
    Z = np.zeros(nf)

    # Resolução do sistema L*Y = b
    for i in range (nf):
        if i == 0:
            Y[i] = B[i]/L[i,i]
        else:
            S = [Y[k]*L[i,k] for k in range (i)]
            Y[i] = B[i]-np.sum(S)
    
    # Resolução do sistema D*Z = Y
    for i in range (nf):
        Z[i] = Y[i]/D[i,i]

    # Resolução do sistema Lt*X = Z
    i = nf-1
    while i >= 0:
        if i == nf-1:
            X[i] = Z[i]
        else:
            S = [X[k]*L[k,i] for k in range (i+1,nf)]
            X[i] = (Z[i]-np.sum(S))
        i = i - 1
    return X

# Método recursivo para resolver o sistema LDLt*x = b
'''
def resolucao(L,D,Lt,B,nf):
    Y = np.zeros(nf)
    X = np.zeros(nf)
    i = nf-1
    j = 0
    
    def recursiva_Y(Y,i):
        if i == 0:
            Y[i] = B[i]/L[i,i]
            return Y[i]
        else:
            S = [recursiva_Y(Y,k)*L[i,k] for k in range (i)]
            Y[i] = (B[i]-np.sum(S))/L[i,i]
            return Y[i]

    def recursiva_X(Y,X,j):
        if j == nf-1:
            X[j] = Y[j]/(L[j,j]*D[j,j])
            return X[j]
        else:
            S = 0
            k = nf-1
            while k > j:
                S = recursiva_X(Y,X,k)*Lt[j,k] + S
                k = k - 1
            X[j] = ((Y[j]/D[j,j])-S)/Lt[j,j]
            return X[j]
    
    recursiva_Y(Y,i)
    recursiva_X(Y,X,j)
    return X
'''
