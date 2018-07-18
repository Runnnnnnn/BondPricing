import numpy as np
#set seed
np.random.seed(15)
#number of paths
m = 1000
#number of intervals
N = 10000
#bond maturity
T=0.5
#delta t
t = T/float(N)

#initial interest rate is 5%
r = np.zeros([m,N])
r[:,0] = 0.05

#assumption for vasicek model
sigma = 0.12
k = 0.82
r_mean = 0.05

#simulate browian motion process
dw = np.zeros((m,N))
dw = np.sqrt(t) * np.random.normal(0,1,[m,N])

#Vasicek model
#simulate interest rate
for i in range(m):
    for j in range(N-1):
        r[i,j+1] = r[i,j] + k*(r_mean - r[i,j])*t + sigma * dw[i,j]

#Using Euler's method of integral estimation, the discount factor can be transformed as following:
discount_factor = np.exp(-r[:,1:N].sum(axis=1) * t)

bond_price = np.mean(discount_factor*1000)
print(bond_price)
