from scipy.special import hyp1f1 
from numpy import sqrt, exp, pi, dot 
def boys(n,t):
    return hyp1f1(n+0.5, n+1.5, -t)/(2.*n+1.)
def Vij(i,j,k,l,m,n,alpha,beta,A,B,C):
    p = alpha + beta
    q = alpha * beta
    AB = A-B
    rAB = dot(AB, AB)
    P = (alpha*A+beta*B)/p 
    PC = P-C 
    pRPC = p*dot(PC,PC) 
    Ax,Ay,Az = A[0], A[1], A[2] 
    Bx,By,Bz = B[0], B[1], B[2] 
    Cx,Cy,Cz = C[0], C[1], C[2] 
    if (i,j,k,l,m,n) == (0, 0, 0, 0, 0, 0):
          return 2*pi*exp(-q*rAB/p)*boys(0, pRPC)/p
    if (i,j,k,l,m,n) == (0, 0, 0, 1, 0, 0):
          return 2*pi*(-alpha*(-Ax + Bx)*boys(0, pRPC)/p + (Cx + (-Ax*alpha - Bx*beta)/p)*boys(1, pRPC))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (0, 0, 0, 0, 1, 0):
          return 2*pi*(-alpha*(-Ay + By)*boys(0, pRPC)/p + (Cy + (-Ay*alpha - By*beta)/p)*boys(1, pRPC))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (0, 0, 0, 0, 0, 1):
          return 2*pi*(-alpha*(-Az + Bz)*boys(0, pRPC)/p + (Cz + (-Az*alpha - Bz*beta)/p)*boys(1, pRPC))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (1, 0, 0, 0, 0, 0):
          return 2*pi*(-beta*(Ax - Bx)*boys(0, pRPC)/p + (Cx + (-Ax*alpha - Bx*beta)/p)*boys(1, pRPC))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (1, 0, 0, 1, 0, 0):
          return pi*(-2*alpha*(-Ax + Bx)*(-beta*(Ax - Bx)*boys(0, pRPC)/p + (Cx + (-Ax*alpha - Bx*beta)/p)*boys(1, pRPC))/p - 2*beta*(Ax - Bx)*(Cx + (-Ax*alpha - Bx*beta)/p)*boys(1, pRPC)/p + 2*(Cx + (-Ax*alpha - Bx*beta)/p)**2*boys(2, pRPC) + boys(0, pRPC)/p - boys(1, pRPC)/p)*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (1, 0, 0, 0, 1, 0):
          return 2*pi*(-alpha*(-Ay + By)*(-beta*(Ax - Bx)*boys(0, pRPC)/p + (Cx + (-Ax*alpha - Bx*beta)/p)*boys(1, pRPC))/p + (Cy + (-Ay*alpha - By*beta)/p)*(-beta*(Ax - Bx)*boys(1, pRPC)/p + (Cx + (-Ax*alpha - Bx*beta)/p)*boys(2, pRPC)))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (1, 0, 0, 0, 0, 1):
          return 2*pi*(-alpha*(-Az + Bz)*(-beta*(Ax - Bx)*boys(0, pRPC)/p + (Cx + (-Ax*alpha - Bx*beta)/p)*boys(1, pRPC))/p + (Cz + (-Az*alpha - Bz*beta)/p)*(-beta*(Ax - Bx)*boys(1, pRPC)/p + (Cx + (-Ax*alpha - Bx*beta)/p)*boys(2, pRPC)))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (0, 1, 0, 0, 0, 0):
          return 2*pi*(-beta*(Ay - By)*boys(0, pRPC)/p + (Cy + (-Ay*alpha - By*beta)/p)*boys(1, pRPC))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (0, 1, 0, 1, 0, 0):
          return 2*pi*(-alpha*(-Ax + Bx)*(-beta*(Ay - By)*boys(0, pRPC)/p + (Cy + (-Ay*alpha - By*beta)/p)*boys(1, pRPC))/p + (Cx + (-Ax*alpha - Bx*beta)/p)*(-beta*(Ay - By)*boys(1, pRPC)/p + (Cy + (-Ay*alpha - By*beta)/p)*boys(2, pRPC)))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (0, 1, 0, 0, 1, 0):
          return pi*(-2*alpha*(-Ay + By)*(-beta*(Ay - By)*boys(0, pRPC)/p + (Cy + (-Ay*alpha - By*beta)/p)*boys(1, pRPC))/p - 2*beta*(Ay - By)*(Cy + (-Ay*alpha - By*beta)/p)*boys(1, pRPC)/p + 2*(Cy + (-Ay*alpha - By*beta)/p)**2*boys(2, pRPC) + boys(0, pRPC)/p - boys(1, pRPC)/p)*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (0, 1, 0, 0, 0, 1):
          return 2*pi*(-alpha*(-Az + Bz)*(-beta*(Ay - By)*boys(0, pRPC)/p + (Cy + (-Ay*alpha - By*beta)/p)*boys(1, pRPC))/p + (Cz + (-Az*alpha - Bz*beta)/p)*(-beta*(Ay - By)*boys(1, pRPC)/p + (Cy + (-Ay*alpha - By*beta)/p)*boys(2, pRPC)))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (0, 0, 1, 0, 0, 0):
          return 2*pi*(-beta*(Az - Bz)*boys(0, pRPC)/p + (Cz + (-Az*alpha - Bz*beta)/p)*boys(1, pRPC))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (0, 0, 1, 1, 0, 0):
          return 2*pi*(-alpha*(-Ax + Bx)*(-beta*(Az - Bz)*boys(0, pRPC)/p + (Cz + (-Az*alpha - Bz*beta)/p)*boys(1, pRPC))/p + (Cx + (-Ax*alpha - Bx*beta)/p)*(-beta*(Az - Bz)*boys(1, pRPC)/p + (Cz + (-Az*alpha - Bz*beta)/p)*boys(2, pRPC)))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (0, 0, 1, 0, 1, 0):
          return 2*pi*(-alpha*(-Ay + By)*(-beta*(Az - Bz)*boys(0, pRPC)/p + (Cz + (-Az*alpha - Bz*beta)/p)*boys(1, pRPC))/p + (Cy + (-Ay*alpha - By*beta)/p)*(-beta*(Az - Bz)*boys(1, pRPC)/p + (Cz + (-Az*alpha - Bz*beta)/p)*boys(2, pRPC)))*exp(-q*rAB/p)/p
    if (i,j,k,l,m,n) == (0, 0, 1, 0, 0, 1):
          return pi*(-2*alpha*(-Az + Bz)*(-beta*(Az - Bz)*boys(0, pRPC)/p + (Cz + (-Az*alpha - Bz*beta)/p)*boys(1, pRPC))/p - 2*beta*(Az - Bz)*(Cz + (-Az*alpha - Bz*beta)/p)*boys(1, pRPC)/p + 2*(Cz + (-Az*alpha - Bz*beta)/p)**2*boys(2, pRPC) + boys(0, pRPC)/p - boys(1, pRPC)/p)*exp(-q*rAB/p)/p
