import numpy as np
from scipy.optimize import minimize

### Score to maximize P(x1,x2,x3)= -(x1^2 -2x1 +4(x2)^2 - 0.03(x3)^2 + 0.04x3)                       ###
### Maximizing it is equivalent to minimize P1(x1,x2,x3)= +(x1^2 -2x1 +4(x2)^2 - 0.03(x3)^2 + 0.04x3)###
### Maximum score will be equal to negative of minimum value of P1(x1,x2,x3)                         ###

######## Objective function : minimize(P1) 
def Objectionfunction(x):
    x1,x2,x3 = x[0],x[1],x[2]
    return (x1*x1) - (2*x1) + (4*x2*x2) - (0.03*x3*x3) + (0.04*x3)

######### x1+x2+x3 is exactly equal to 2
def sum_constraint(x):
    x1,x2,x3 = x[0],x[1],x[2]
    return 2-x1-x2-x3

##### As the answer can depend on initial guess, 
##### For method = Sequential Least SQuares Programming (SLSQP)
##### I checked for i,j,k belongs to [0,2] at 0.001 gaps
##### and found the best initial guess to be [0,0,0.3] which give min_value = -0.9901030927835053
##### Although the initial guess = [0,0,0] gave the min_value = -0.9901030927835052 
##### and both results have negligible difference which may even be due to floating-point errors
##### Scipy have 1 more constrained optimizer as trust-constr

Initial_guess = [0,0,0]
ranges = [[0,2],[0,2],[0,2]]                       ## Bounds on x1,x2,x3
con1 = [{'type':'eq','fun':sum_constraint}]        ## equality constraint
answer = minimize(Objectionfunction,Initial_guess,method='SLSQP',bounds=ranges,constraints = con1)
print("The minimum value of Objective function is :", answer.fun)
print("The value of x = [x1,x2,x3] for it is [",answer.x[0],",",answer.x[1],",",answer.x[2],"]")
print("Also the sum(x1+x2+x3) found by SLSQP optimizer = ",answer.x[0]+answer.x[1]+answer.x[2],"\n")
print("Hence the maximum score or max(P(x1,x2,x3)) is ", -answer.fun)