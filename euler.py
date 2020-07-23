# -*- coding: utf-8 -*-
# Bibliotecas utilizadas
import math
import numpy as np

def a1(N,M,lbd,k,i,deltaT,deltaX,u_a1,b_a1):
    t = (k+1)*deltaT                        # 't' e 'x' base na equação 29
    x = i*deltaX
    if 0 < i < N:                           # Condições para a matriz 'b'

        # f(t,x) conforme o enunciado
        fXT = 10*(x**2)*(x-1)-60*x*t+20*t

        # Termos definidos na matriz 'b'
        b_a1[i-1] = u_a1[k,i] + deltaT*(fXT)
    return b_a1, u_a1

def a2(N,M,lbd,k,i,deltaT,deltaX,u_a2,b_a2):
    t = (k+1)*deltaT            # 't' e 'x' base na equação 29
    x = i*deltaX

    if k == 0:                  # Condições iniciais
        u_a2[k,i] = (x**2)*((1-x)**2)
    if 0 < i < N:               # Condições para a matriz 'b'

        # f(t,x) conforme o enunciado
        fXT = 10*math.cos(10*t)*(x**2)*((1-x)**2)-(1+math.sin(10*t))*(12*(x**2)-12*x+2)

        # Termos definidos na matriz 'b'
        b_a2[i-1] = u_a2[k,i] + deltaT*(fXT)
    return b_a2, u_a2

def b(N,M,lbd,k,i,deltaT,deltaX,u_b,b_b):
    t = (k+1)*deltaT            # 't' e 'x' base na equação 29
    x = i*deltaX

    # f(t,x) conforme o enunciado
    fXT = math.exp(t-x)*(25*(t**2)*math.cos(5*t*x)-(10*t+5*x)*math.sin(5*t*x))

    # g1 e g2 para 't' de k e para 't' de k+1
    g1 = math.exp(t)
    g2 = math.exp(t-1)*math.cos(5*t)
    g1k = math.exp(k*deltaT)
    g2k = math.exp((k*deltaT)-1)*math.cos(5*(k*deltaT))

    # Condições de fronteira
    if i == 0:
        u_b[k,i] = g1k
    elif i == N:
        u_b[k,i] = g2k


    elif k == 0:                # Condição inicial
        u_b[k,i] = math.exp(-x)

    # Fronteiras internas para matriz 'b'
    if i == 1:                            
        b_b[i-1] = u_b[k,i] + deltaT*(fXT) + lbd*g1
    elif i == N-1:
        b_b[i-1] = u_b[k,i] + deltaT*(fXT) + lbd*g2

    # Parte interna da matriz 'b'
    elif 1 < i < N-1:
        b_b[i-1] = u_b[k,i] + deltaT*(fXT)
    return b_b, u_b

def c(N,M,lbd,k,i,deltaT,deltaX,u_c,b_c):
    t = (k+1)*deltaT            # 't' e 'x' base na equação 29
    x = i*deltaX

    # 'r', 'h' e 'p' definidos pelo enunciado
    r = 10000*(1-2*t**2)
    h = deltaX
    p = 0.25

    # Condições conforme especificado
    if p-h/2 <= x <= p+h/2:
        g = 1/h
    else:
        g = 0

    # f(t,x) conforme o enunciado
    fXT = r*g

    if 0 < i < N:
        # Termos definidos na matriz 'b'
        b_c[i-1] = u_c[k,i] + deltaT*(fXT)
    return b_c, u_c
