#coupon paying bond
import numpy as np
np.random.seed(15)
#4 years till maturity
T = 4
#payment schedule
payment = np.ones(T*2)*30
payment[-1] = 1030

#Vasicek Model initial assumption
r_mean = 0.05
ki = 0.82
sigma = 0.12

#number of intervals and simulation path
n = 1000
path = 2000

r = np.zeros([path,n+1])
r[:,0] = 0.05

dt = T/float(n)
#brownian motion process
dw = np.sqrt(dt) * np.random.normal(0,1,[path,n])

#simulate interest rate
for i in range(path):
    for j in range(n):
       r[i,j+1] = r[i,j] + ki * (r_mean-r[i,j]) * dt + sigma * dw[i,j]

    #remove the initial interes rate value (0.05)
r_mod = np.delete(r,0,axis=1)

PV = np.zeros(T*2)

#create a dict for interest rate, store simulated interest rate maxtrix for different period and discount each payment back
int_rate = {}
for i in range(T*2):
    int_rate[i] = r_mod[:,0:((i+1)*n)/(T*2)]
    PV[i] = np.mean(np.exp(-dt*int_rate[i].sum(axis=1))*payment[i])

Present_Value = sum(PV)
print(Present_Value)
