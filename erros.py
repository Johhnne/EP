# -*- coding: utf-8 -*-
# Bibliotecas utilizadas
import numpy as np
import math

# Calcula o erro entre a matriz numérica e a exata
def erro(N,M,u,u_mod,letra):
    erro = np.subtract(u_mod,u)             # Subtração da matriz exata pela numérica
    erro = np.around(erro, decimals=6)      # Arredonda a matriz de erro definida pela subtração
    erro = np.absolute(erro)                # Módulo da matriz de erro

    # Mostra o valor máximo da última linha da matriz de erro
    print("Erro máximo da equação 11 para T = 1(letra " ,letra, "):" ,erro[M,:].max())

# Calculo o erro quadrático
def erro2(N,nf,uT,X,uk):
    deltaX = 1/N
    S1 = 0
    S2 = 0
    for i in range (N-1):
        S1 = [X[k]*uk[k,i] for k in range (nf)]
        S2 =(uT[i]-np.sum(S1))**2 + S2
    E = math.sqrt(deltaX*(S2))
    print("Erro quadrático:",round(E,5))
