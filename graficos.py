# -*- coding: utf-8 -*-
# Bibliotecas utilizadas
import numpy as np
from matplotlib import pyplot as plt

# Função para criação de um mapa de calor utilizando uma matriz e escalas definidas pelos vetores VX e VT
def mapa_unico(u,VX,VT,titulo):
    fig, quadro = plt.subplots(1,1)                     # Define as divisões da figura que será mostrada     

    # Montagem do mapa através das matrizes e vetores definidos anteriormente, 
    # da coloração definida por 'cmap' e dos valores máximo e mínimo da matriz                                                   
    a = quadro.pcolormesh(VX,VT,u,cmap = "coolwarm", vmin=u.min(),vmax=u.max())

    quadro.set_title(titulo)                            # Define o título do gráfico
    quadro.set_xlabel("Posição")                        # Define a nomenclatura do eixo 'x'
    quadro.set_ylabel("Tempo")                          # Define a nomenclatura do eixo 'y'    
    quadro.set_yticks(np.arange(0,1.1,0.1))             # Define os índices do eixo 'y' de 0.1 em 0.1
    fig.colorbar(a, ax=quadro,label = "Temperatura")    # Faz a barra de cores localizada a direita do gráfico
    plt.show()                                          # Mostra o resultado 

# Função para criação de dois mapas de calor utilizando duas matrizes de iguais dimensões e escalas definidas pelos vetores VX e VT
def mapa_duplo(u,u_mod,VX,VT,titulo1,titulo2):

    # Além de dividir a figura em dois quadros, define uma distância padrão entre eles
    fig, quadro = plt.subplots(1,2,gridspec_kw = dict(wspace = 0.6))

    a = quadro[0].pcolormesh(VX,VT,u,cmap = "coolwarm" ,vmin=u.min(),vmax=u.max())
    quadro[0].set_title(titulo1)
    quadro[0].set_xlabel("Posição")
    quadro[0].set_ylabel("Tempo")
    quadro[0].set_yticks(np.arange(0,1.1,0.1))
    fig.colorbar(a, ax=quadro[0],label = "Temperatura")

    b = quadro[1].pcolormesh(VX,VT,u_mod,cmap = "coolwarm",vmin=u.min(),vmax=u.max())
    quadro[1].set_title(titulo2)
    quadro[1].set_xlabel("Posição")
    quadro[1].set_ylabel("Tempo")
    quadro[1].set_yticks(np.arange(0,1.1,0.1))
    fig.colorbar(b, ax=quadro[1],label = "Temperatura")
    plt.show()

# Função para criação de gráfico simples
def linha(u,N,titulo):
    fig, ax = plt.subplots(constrained_layout=True)
    ax.plot(u,"r",label = "uT")
    ax.set_xlabel('Posição na matriz')
    ax.set_ylabel('Temperatura[°C]')
    ax.set_title(titulo)
    ax.legend()

    # Escala de x para posição na matriz e o inverso
    def x2p(x):
        return x/N
    def p2x(x):
        return x*N

    # Cria um eixo secundário com as escalas definidas anteriormente
    secax = ax.secondary_xaxis('top', functions = (x2p,p2x))
    secax.set_xlabel('Posição na barra(x)')
    secax.set_xticks(np.arange(0,1.1,0.1))
    plt.show()
