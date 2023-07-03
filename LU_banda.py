#Codigo que se beneficia da estrutura das bandas

import numpy as np
import time

def LU_banda ( A, p, n ):
    U = np.array(A)
    L = np.eye( n )
    for j in range( n - 1 ):
        v = min( n, j + p + 1 )
        for i in range( j + 1, v ):
            L[ i, j ] = U[ i, j ] / U[ j, j ]
            U[ i, j : v ] = U[ i, j : v ] - L[ i, j ] * U[ j, j : v ]
    return ( L, U )

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

#inicializando as matrizes A e b
(A,b) = modelo(n,w,T)

start_time=time.time()

(L,U) = LU_banda ( A,1,n-2)

#resolvendo os sistemas triangulares
y=[0 for _ in range (n-2)]
for i in range (n-2):
    soma=b[i]
    for j in range (i-1,-1,-1):
        soma-=L[i][j]*y[j]
    y[i]=soma/L[i][i]
    

x=[0 for _ in range (n-2)]
for i in range (n-3,-1,-1):
    soma=y[i]
    for j in range (i+1,n-2):
        soma-=U[i][j]*x[j]   
    x[i]=soma/U[i][i]


print('Vetor Resposta:',x)

end_time=time.time()

execution_time = end_time - start_time
print("Tempo de execução:", execution_time)