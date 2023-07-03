#Codigo que nao se beneficia da estrutura das bandas

import numpy as np
import time

def modelo ( n, w, T, L = 1.2e2 , E = 2.9e7 , I = 1.21e2 ):
    a = T / ( E * I )
    b = w / ( 2 * E * I )
    h = L / ( n - 1 )
    A = np.zeros( ( n - 2, n - 2 ) )
    v = -( h**2 * a + 2 )
    A[ range( 0, n - 3 ), range( 1, n - 2 ) ] = 1.0
    A[ range( 0, n - 2 ), range( 0, n - 2 ) ] = v
    A[ range( 1, n - 2 ), range( 0, n - 3 ) ] = 1.0
    X = np.linspace( h, ( n - 2 ) * h, n - 2 )
    bh_3 = b * ( h ** 3 )
    f = np.linspace( bh_3 , ( n - 2 ) * bh_3 , n - 2 ) * ( L - X )
    return ( A, f )

n=int(input("Digite n:"))
w=float(input("Digite w:"))
T=float(input("Digite T:"))

#inicializando as matrizes A, b,U,L e P
(A,b) = modelo(n,w,T)
n=n-2
U = np.array(A)
L = np.zeros( (n,n) )
P=np.eye(n)
start_time=time.time()

for i in range (n-1):
    mx=-999999999
    index=i
    #Encontrando o maximo elemento da coluna
    for j in range (i,n):
        mx=max(mx,U[j][i])
        if(mx==U[j][i]):
            index=j
    #Swap linha do maximo elemento com a linha i
    b_temp=b[i]
    b[i]=b[index]
    b[index]=b_temp
    for j in range(n):
        guardar_valor=U[i][j]
        U[i][j]=U[index][j]
        U[index][j]=guardar_valor
        guardar_valor=L[i][j]
        L[i][j]=L[index][j]
        L[index][j]=guardar_valor
        guardar_valor=P[i][j]
        P[i][j]=P[index][j]
        P[index][j]=guardar_valor
    #Subtraindo a linha i de cada linha posterior
    for j in range(i+1,n):
        L[j][i]=(U[j][i])/(U[i][i])
        for k in range (i,n):
            U[j][k]-=L[j][i]*U[i][k]
for i in range (n):
    L[i][i]=1

#resolvendo os sistemas triangulares
y=[0 for _ in range (n)]
for i in range (n):
    soma=b[i]
    for j in range (i-1,-1,-1):
        soma-=L[i][j]*y[j]
    y[i]=soma/L[i][i]
    
x=[0 for _ in range (n)]
for i in range (n-1,-1,-1):
    soma=y[i]
    for j in range (i+1,n):
        soma-=U[i][j]*x[j]
    x[i]=soma/U[i][i]

print('Vetor Resposta:',x)

end_time=time.time()
execution_time = end_time - start_time
print("Tempo de execução:", execution_time)









            

    
    


        

