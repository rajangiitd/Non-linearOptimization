import numpy as np

# f(x)
def f(x):
    x1,x2= x[0][0],x[1][0]
    return 8*(x1**4) + 3*(x2**2) - (6*x1*x2)+ (2*x2)

# del f(x)
def delF(x):
    x1,x2= x[0][0],x[1][0]
    ans = np.array([ 32*(x1**3) - (6*x2) , (6*x2) - (6*x1) +2   ] ).T
    return ans

# delsquare f(x)
def delsqF(x):
    x1,x2= x[0][0],x[1][0]
    ans =  np.array([ [ 96*(x1**2), -6],[-6, 6]  ]).T
    return ans

def BacktrackingLineSearch( xk, pk):
    alphak = 1
    mu = 0.2
    # Armijo condition
    while( f(xk + alphak*pk )> f(xk) + mu*alphak*np.matmul(pk.T,-pk)):
        alphak= alphak/2
    return alphak

### After plotting 3-D graph of function, I saw that the function minimizes
### somewhere between x1,x2 belongs to (-1.5,0.1), (-1.5,0.1)
### Then I noticed that the algorithm is very sensitive to initial guess
### After few iterations, alphak tends to become approx 10^-17 
### for initial guess = (0.5,0.5), after converging f(x) comes = -0.2500
### for initial guess = (0,0) after converfing f(x) comes = -3.95e-322 (approx 0)
### for initial guess = (-0.5,-0.5), after converging f(x) comes = -1.2500
### for initial guess = (-1,-1), after converging f(x) comes = -1.5953
### for initial guess = (0,-1), after converging f(x) comes = -1.54149
### And so on
### Hence after looping x1,x2 from [-1.5,1] at 0.001 gaps
### Best initial guess came out to be [0.462,0.462]
### This give f(x) = -1.608794911641696 after the algorithm converges.

i,j= 0.462,0.462
Initial_guess = np.reshape(np.array([i,j]).T , (-1,1))
x= Initial_guess
val = delF(x)
print("Initial guess: [", x[0][0],",",x[1][0] , "] and initial value of f(x1,x2) = ", f(x))

iter_count =0
# The following while condition is similar to the condition used in code
# while(abs(val[0])>10**(-6) and abs(val[1])>10**(-6) ): i.e. (10**-6) is tolerance level
while(np.linalg.norm(val)>10**(-6)):    
    iter_count+=1
    print("After iteration:",iter_count)
    alpha = BacktrackingLineSearch(x,-delF(x))
    x = x - np.reshape((alpha*delF(x)) ,(-1,1))
    print("At x = [", x[0][0],",",x[1][0] , "] and the value of f(x1,x2) = ", f(x))
    val = delF(x)
    if(alpha< 10**-13):
        break     ### the value of alpha has diminished so much that update doesn't make any valuable change

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