# -*- coding: utf-8 -*-
# Biblioteca utilizada
import numpy as np

# Transformação da matriz A em vetores
def vetores_A(N,lbd):
    VA1 = np.zeros(N-1)
    VA2 = np.zeros(N-2)
    for i in range (N-1):
        VA1[i] = 1 + 2*lbd
        if i < N-2:
            VA2[i] = -lbd
    return VA1,VA2

# Decomposição LDLt*x = b em vetores
def decomposicao_cholesky(VA1,VA2,N):
    VL = np.zeros(N-2)
    VD = np.zeros(N-1)
    for j in range(N-1):
        if j == 0:
            VD[j] = VA1[j]
        else:
            VL[j-1] = VA2[j-1]/VD[j-1]
            VD[j] = VA1[j] - (VL[j-1]**2)*VD[j-1]
    return VD,VL
