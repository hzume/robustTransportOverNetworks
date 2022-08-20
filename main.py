import numpy as np
from scipy import linalg

class Graph(np.ndarray):
    def __new__(cls, n, edges):
        ret = np.zeros((n, n))
        for e in edges:
            ret[int(e[0]-1)][int(e[1]-1)] = np.exp(-e[2])
        return ret
    
n = 9
N = 3

edges = np.loadtxt("matrix_b.txt")
A = Graph(n, edges)
w, vl, vr = linalg.eig(A, left=True)

idx = 0
max_eig = -np.inf
for i, eig in enumerate(w):
    if np.isreal(eig):
        eig = np.real(eig)
        if max_eig < eig:
            idx = i
            max_eig = eig

u = np.real_if_close(vl[:, idx])
v = np.real_if_close(vr[:, idx])
inner_prod = u@v
u /= np.sqrt(inner_prod)
v /= np.sqrt(inner_prod)
nu = u*v

R = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        R[i][j] = v[j]*A[i][j] / (max_eig*v[i])

Rn = np.linalg.matrix_power(R, N)

delta_1 = np.ones((n)) * 1e-10
delta_1[0] = 1
delta_n = np.ones(n) * 1e-10
delta_n[-1] = 1

phi_n = np.ones((n))

def C(phi_h_0):
    phi_0 = Rn@phi_n
    phi_h_0 = delta_1 / phi_0
    phi_h_n = Rn.T@phi_h_0
    return delta_n / phi_h_n

new_phi = C(phi_n)
while (abs(phi_n[0] - new_phi[0]) > 1e-10):
    phi_n = new_phi
    new_phi = C(phi_n)


phi = [phi_n]
for _ in range(N):
    phi.append(R@phi[-1])
phi.reverse()

pi = []
for i in range(N):
    pi.append(np.diag(1/phi[i])@R@np.diag(phi[i+1]))

P = [delta_1]
for i in range(N):
    P.append(pi[i].T@P[-1])
P = np.array(P)
P = np.round(P, 4)
print(P)