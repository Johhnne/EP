# -*- coding: utf-8 -*-
# Bibliotecas utilizadas
import math
import numpy as np

# Letra 'A1'
def a1(k,i,M,N,deltaT,deltaX,u_a1):
    i = i + 1                   # Como as fronteiras são nulas, não é preciso passar por i = 0
    t = k*deltaT                # Cálculo das variávies 't' e 'x'
    x = i*deltaX
    if i < N and k < M:         # Exclusão da fronteira i = N e do k = M pois a equação calcula o 'u' para k+1 
        fXT = 10*(x**2)*(x-1)-60*x*t+20*t   # f(t,x) conforme o enunciado

        # Equação 11 do enunciado
        u_a1[k+1,i] = u_a1[k,i]+deltaT*(((u_a1[k,i-1] - 2*u_a1[k,i] + u_a1[k,i+1])/((deltaX)**2))+fXT)
    return u_a1                 # Retorno da matriz da solução numérica

# Letra 'A2'
def a2(k,i,M,N,deltaT,deltaX,u_a2):
    i = i + 1                   # Como as fronteiras são nulas, não é preciso passar por i = 0
    if i < N+1:                 # A partir da linha anterior o valor de i pode alcançar N+1 
        t = k*deltaT            # Cálculo das variávies 't' e 'x'
        x = i*deltaX 
        if k == 0:              # Condição inicial
            u_a2[k,i] = (1+math.sin(10*t))*(x**2)*((1-x)**2)
        elif i < N and k < M+1: # Exclusão da fronteira i = N e do k = M pois a equação calcula o 'u' para k+1 
            k = k - 1           # Para que a equação 11 inclua a fronteira definida em k = 0
            t = k*deltaT        # Mudança no valor de 't' pela alteração do valor de 'k'

            # f(t,x) conforme o enunciado
            fXT = 10*math.cos(10*t)*(x**2)*((1-x)**2)-(1+math.sin(10*t))*(12*(x**2)-12*x+2)

            # Equação 11 do enunciado
            u_a2[k+1,i] = u_a2[k,i]+deltaT*(((u_a2[k,i-1] - 2*u_a2[k,i] + u_a2[k,i+1])/((deltaX)**2))+fXT)
    return u_a2

# Letra 'B'
def b(k,i,M,N,deltaT,deltaX,u_b):
    t = k*deltaT                # Cálculo das variávies 't' e 'x'
    x = i*deltaX
    if i == N:                  # Condição de fronteira
        u_b[k,i] = math.exp(t-x)*math.cos(5*x*t)
    elif i == 0 or k == 0:      # Condição inicial e parte da fronteira
        u_b[k,i] = math.exp(t-x)*math.cos(5*x*t)
    elif i < N and k < M+1:     # Exclusão da fronteira i = N e do k = M pois a equação calcula o 'u' para k+1
        k = k-1                 # Para que a equação 11 inclua a fronteira definida em k = 0
        t = k*deltaT            # Mudança no valor de 't' pela alteração do valor de 'k'

        # f(t,x) conforme o enunciado
        fXT = math.exp(t-x)*(25*(t**2)*math.cos(5*t*x)-(10*t+5*x)*math.sin(5*t*x))

        # Equação 11 do enunciado
        u_b[k+1,i] = u_b[k,i]+deltaT*(((u_b[k,i-1] - 2*u_b[k,i] + u_b[k,i+1])/((deltaX)**2))+fXT)
    return u_b                  # Retorno da matriz da solução numérica

# Letra 'C'
def c(k,i,M,N,deltaT,deltaX,u_c):
    i = i + 1                   # Como as fronteiras são nulas, não é preciso passar por i = 0
    if i < N and k < M:         # Exclusão da fronteira i = N e do k = M pois a equação calcula o 'u' para k+1 
        t = k*deltaT            # Cálculo das variávies 't' e 'x'
        x = i*deltaX

        # 'r', 'h' e 'p' definidos pelo enunciado
        r = 10000*(1-2*t**2)
        h = deltaX
        p = 0.25

        # Condições conforme  especificado
        if p-h/2 <= x <= p+h/2:     
            g = 1/h
        else:
            g = 0

        # f(t,x) conforme o enunciado
        fXT = r*g

        # Equação 11 do enunciado
        u_c[k+1,i] = u_c[k,i]+deltaT*(((u_c[k,i-1] - 2*u_c[k,i] + u_c[k,i+1])/((deltaX)**2))+fXT)

        return u_c              # Retorno da matriz da solução numérica
