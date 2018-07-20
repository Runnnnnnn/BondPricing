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
r = np.zeros([m,N+1])
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
    for j in range(N):
        r[i,j+1] = r[i,j] + k*(r_mean - r[i,j])*t + sigma * dw[i,j]

#Using Euler's method of integral estimation, the discount factor can be transformed as following:
discount_factor = np.exp(-r[:,1:N+1].sum(axis=1) * t)

#bond face value
FV = 1000 
bond_price = np.mean(discount_factor*FV)
print(bond_price)

####################################################################################
#To avoid column miscount, apply drop function to drop the "first" column -> Column 0

#drop the column with initial interest rate assumption 0.05
r_new = np.delete(r,0,axis=1)
discount_factor_2 = np.exp(-r_new.sum(axis=1) * t)

bond_price_2 = np.mean(discount_factor_2*FV)
print(bond_price_2)
#As the methodology does not change
#bond_price = bond_price_2 


