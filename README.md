# Project-LinearSystems

Projeto para analisar a deformação de uma viga sujeita a uma carga distribuída W e uma tração T.

Os objetivos do projeto são:
1. Implementar rotinas para soluçãoao eficiente de sistemas triangulares (superior e inferior) com matrizes banda;
2. Utilizar essas rotinas em conjunto com a rotina fornecida para cálculo da fatoração
A = LU para obter uma rotina para resolver sistemas lineares com matrizes banda;
3. Resolver os sistemas lineares para o modelo da viga utilizando diversos
valores do parâmetro de discretização n e analise da variação do tempo computacional
conforme esse parâmetro aumenta;
4. Comparar o obtido no item anterior com o tempo de computação de rotinas que não
se aproveitam da estrutra de bandas do sistema;
5. Fixe um valor (grande) de n e resolver o sistema para diversos valores de parãmetros
w. Aproveitar da fatoração A = LU não mudar de um caso para outro;
6. Fazer gráficos dos resultados e comparar as deformações obtidas para distintas cargas
e trações;
7. Escrever um relatório descrevendo cuidadosa e extensivamente os resultados obtidos.
