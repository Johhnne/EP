# EP Parte 1 e 2, disciplina MAP3121 Poli-USP 2020/1

O enunciado está disponível no arquivo enunciado.pdf.

Versão do interpretador: Python3.8.2.

Para utilizar o programa são necessárias as seguintes bibliotecas:
	matplotlib
	numpy
	
Todos os arquivos precisam estar na mesma pasta e não podem ter seus nomes alterados.

Para a excecução será pedido um valor de N e de lambda, após essa definição o usuário decidirá a letra a ser analisada, e obterá como retorno um erro máximo relativo à última linha da matriz que representa a solução numérica. Além disso o programa mostrará dois gráficos, à esquerda para a solução numérica e à direita para a solução exata, e depois mais um gráfico somente para a solução numérica, com exceção da letra 'C' que possui apenas solução numérica.

A escolha do lambda de ser menor ou igual a 0.5 no caso da tarefa 1, e igual ao valor de N para a tarefa 2.

Tabém será retornado o tempo necessário para análise em função do N,lambda e métodos escolhidos.

Para o excecução dos testes da Parte 2 o usuário deve digitar "2" e o teste a ser excecutado, de acordo com as instruções do terminal. 
Apenas nos testes "c" e "d" será possível escolher o valor do "N" a ser utilizado. Nos demais testes o valor de "N" é 128 por padrão.

No caso dos testes "a" e "b", o programa imprime as intensidades (ak) e o erro quadrático. Já o teste "c", além das intensidades (ak) e 
do erro quadrático, inclui também o gráfico da solução uT encontrada. Além disso o teste "d" também inclui o gráfico do uT recebido no arquivo teste.txt.

Para auxiliar a estimativa do tempo de excecução, devido a demora dos testes "c" e "d", o programa mostra uma barra de progresso.

Por fim o arquivo a ser excecutado será apenas o “main.py”.
