# -*- coding: utf-8 -*-
# Biblioteca utilizada
import numpy as np

# Resolução do sistema LDLt*x = b, com L e D definidos por vetores VL e VD
# A resolução se divide em duas partes:
# A primeira calcula a relação dos termos de b para calcular o cada "u"
def B(N,b,VL,B):
    for k in range (N-1):
        if k == 0:
            B[k] = b[k]
        else:
            B[k] = b[k]-VL[k-1]*(B[k-1])
    return B

# A segunda calcula o cada linha de "u" a partir dos valores da relação dos 
# termos de b, e dos "u's" anteriores, começando pelo último até o primeiro
def resolucao(N,k,u,B,VL,VD):
    i = N-1
    while i >= 0:
        if i == N-1:
            u[k+1,i] = B[i-1]/VD[i-1]
        elif i > 0:
            u[k+1,i] = (B[i-1]/VD[i-1])-u[k+1,i+1]*VL[i-1]
        i = i - 1
    return u
    
#############################################################################
# Optou-se pelo uso de loop ao invés do método recursivo por ser mais rápido,
# porém, para efeito de comparação, o método recursivo encontra-se comentado
# abaixo, sendo que para seu uso, pode-se remover o sinal de comentário da 
# função e da sua chamada nas linhas 120, 124, 128, 132 e 137 do arquivo 
# loop_principal.py, na função "excecucao", e comentar o método anterior na 
# mesma função
#############################################################################

'''
# A função recursiva é utilizada para resolver o sistema LDLt*x = b,
# de modo que a multiplicação é feita de forma direta
def recursiva_u(i,k,N,u,b,VL,VD):
    def recursivaLDLt_b(i,VL,b):
        # Para calcular o valor da parte definida como LDLt_b no 
        # sistema, que seriam as multiplicações onde não há u[k+1]
        if i == 0:
            # Primeiro valor de b[i] para o sistema
            return b[i]
        else:
            # Utilizando a mesma lógica da função abaixo, porém 
            # para o termo anterior das multiplicações envolvendo
            # 'b' e o vetor da matriz 'L'
            LDLt_b = b[i] - VL[i-1]*recursivaLDLt_b(i-1,VL,b)
            return LDLt_b
    if i == N-1:
        # Último valor de u[k+1,i] para o sistema
        u[k+1,i] = recursivaLDLt_b(i-1,VL,b)/VD[i-1]
        return u[k+1,i]
    else:
        
        # Essa equação define a relação de multiplicações do sistema,
        # sendo que a variável u[k+1,i+1] é necessária para definir a
        # u[k+1,i], portanto a função percorre todos os valores de u[k+1,i]
        # até o i = N-1, onde o u[k+1,i] não depende do próximo
        u[k+1,i] = recursivaLDLt_b(i-1,VL,b)/VD[i-1] - recursiva_u(i+1,k,N,u,b,VL,VD)*VL[i-1]
        return u[k+1,i]
'''
