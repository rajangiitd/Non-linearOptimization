import numpy as np

def f(x):
    x1,x2= x[0][0],x[1][0]
    return 5*(x1**4) + 4*(x2**4) - 6*(x1**2) +5*(x2**2) + (2*x1*x2) + (15*x1) -(7*x2) -13

def delF(x):
    x1,x2= x[0][0],x[1][0]
    ans = np.array([ 20*(x1**3) - 12*x1 +2*x2 +15  ,  24*(x2**3) + 10*x2 + 2*x1 -7 ] ).T
    return ans

def delsqF(x):
    x1,x2= x[0][0],x[1][0]
    ans =  np.array([ [ 60*(x1**2)-12, 2],[2, 72*(x2**2)+10]  ]).T
    return ans

Initial_guess = np.reshape(np.array([1,1]).T , (-1,1))

x= Initial_guess
val = delF(x)
print("Initial guess: [", x[0][0],",",x[1][0] , "] and initial value of f(x1,x2) = ", f(x))

iteration_count=0
########### While first order necessary condition is false, update the x #############
# The following while condition is equivalent to while( abs(val[0])>10**(-10) and abs(val[1])>10**(-10)):
# i.e. (10**-10) is tolerance level
while(np.linalg.norm(val)>10**(-10)):
    iteration_count+=1
    update = np.reshape(np.matmul( np.linalg.inv(delsqF(x)), val ),(-1,1))
    x = x - update       #### update
    val = delF(x)
    print("For iteration = ",iteration_count)
    print("Value of x: [",x[0][0],",",x[1][0],"] and value of f(x1,fx2) = ",f(x))
###############      Verification                       ###############################
print("\nVerification\n\nFirst Order Necessary Condition(F.O.N.C.)")
print("delf(x) = ",val)
print("We can see that both the values in delf(x) have become close to 0")
print("i.e. We can say that F.O.N.C. is satisfied.\n")
print("Second order necessary condition\n")
print("del_square_f(x) (Let = A) =\n", delsqF(x))
A = delsqF(x)
print("As A is (2 cross 2) and A[0][1]==A[1][0] is ",A[0][1]==A[1][0],"-> A is symmetric matrix")
print("and as A[0][0]>0 is ",A[0][0]>0," i.e. positive and ")
print("Also, determinant of A = ", (A[0][0]*A[1][1])- (A[1][0]*A[0][1])," which is also positive"  )
print("Hence from the sylvester's criteria, we can say that the matrix A is positve definite.\n")
## sylvester's criteria : If A is symmetric and A[1:i][1:i] are all having postiive determinant
## then matrix is positive definite. It is a "if and only if" type statement.
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Also, the eigenvalues of matrix A are",eigenvalues)
print("As we can see that as eigenvalues are non-negative, we can say that")
print("The matrix A is p.s.d.")
print("Hence\n We can claim that we have found a minimum at x=[", x[0][0],",",x[1][0] , "] where f(x)=",f(x))