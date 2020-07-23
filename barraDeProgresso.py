# -*- coding: utf-8 -*-
import sys

# Cria uma barra de progresso que aumenta em direção a 100% com as iterações "i"
def printBarra (i, total, prefixo = '', suffixo = '', decimais = 1, comprimento = 100, preenchimento = '█'):
    porcentagem = ("{0:." + str(decimais) + "f}").format(100 * (i / float(total)))
    partePreenchida = int(comprimento * i // total)
    barra = preenchimento * partePreenchida + '-' * (comprimento - partePreenchida)
    print('\r%s |%s| %s%% %s' % (prefixo, barra, porcentagem, suffixo), end = '\r')
    if i == total: 
        print()
