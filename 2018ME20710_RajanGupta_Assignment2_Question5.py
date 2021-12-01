import numpy as np
import math
from scipy.optimize import minimize

### Minimize x1**2 + exp(x2**2 + 2*(x3**2)) + (4*x3) ###
######## Objective function : minimize(P1) 
def Objectionfunction(x):
    x1,x2,x3 = x[0],x[1],x[2]
    return (x1*x1) + math.exp((x2**2) + (2*(x3**2))) + (4*x3)

#### Subjected to folowing constraints ############
######### x1-x2 + 10x3 <=-2 ######
def ineq_constraint(x):
    x1,x2,x3 = x[0],x[1],x[2]
    return -x1 + x2 - (10*x3) -2

######### -x2+x3=1 #############
def sum_constraint(x):
    x1,x2,x3 = x[0],x[1],x[2]
    return 1+x2-x3

##### For method = Sequential Least SQuares Programming (SLSQP)
##### As solution can depend on initial guess, I tried to test on a range of inputs as initial guess
##### and as I sweeped over valid i,j,k in [-500,500] at gap of 1, I got best initial guess as 
##### [-335, -2, -1] which gave minimum value as 4.964561098668265

Initial_guess = [-335,-2,-1]
ranges = [[-np.inf,np.inf],[-np.inf,np.inf],[-np.inf,np.inf]]      ## Bounds on x1,x2,x3 (Unbounded)
constr = [{'type':'ineq','fun':ineq_constraint},{'type':'eq','fun':sum_constraint}]   ## constraints
answer = minimize(Objectionfunction,Initial_guess,method='SLSQP',bounds=ranges,constraints = constr)

print("The minimum value of Objective function is :", answer.fun)
print("And the value of x = [x1,x2,x3] for it is [",answer.x[0],",",answer.x[1],",",answer.x[2],"]")