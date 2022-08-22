
# tabuleiro-L
Em um tabuleiro quadrado dividido em $2^(2n)$ quadrados (com tamanhos iguais entre si), cada posição (i.e., cada quadrado da divisão) pode ser determinada por uma tupla de comprimento $n$, onde cada elemento é um inteiro $0$, $1$, $2$ ou $3$, denotando sucessivamente em quais quadrantes do tabuleiro o quadrado se encontra: convencionando que $0$ denota o quadrante superior esquerdo, $1$ o superior direito, $2$ o inferior esquerdo e $3$ o inferior direito.

* o primeiro número da posição denota em qual quadrante do tabuleiro inteiro o quadrado em questão se encontra,
* o segundo número da posição denota em qual sub-quadrante deste primeiro quadrante o quadrado em questão se encontra,

e assim sucessivamente. No tabuleiro de tamanho $n=1$, a única posição existente é a tupla vazia ( ).

Também podemos determinar onde se localiza no tabuleiro uma peça de 3 quadrados em formato “L”, como na figura abaixo, usando um conjunto contendo as posições dos 3 quadrados do tabuleiro cobertos pela peça.

![image info](./1.png)

