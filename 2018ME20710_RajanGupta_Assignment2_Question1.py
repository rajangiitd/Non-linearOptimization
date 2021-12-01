import math

########### Given function #############
def f(x):
    return (math.sin(x) - (3*x*math.exp(-(x**3)))) 

########### Derivative of given function ##############
def df(x):
    return (math.cos(x) -3*math.exp(-x**3)*(1- (3*x**3)) )

########### Root finding function via newton root finding method ########
def find_root(initial_guess):
    if( f(initial_guess)==0):
        return initial_guess
    else:
        iter_count=0
        current_guess = initial_guess
        ########################### while loop for update###########################
        while ( abs(f(current_guess))>=(10**-12)):
            iter_count+=1
            denominator = df(current_guess)
            if( abs(denominator)< 10**(-9)):
                print("--f'(x) has gone very close to zero for the value",current_guess,"i.e. Poor initial guess--")
                return current_guess
            
            current_guess =  current_guess - (f(current_guess)/denominator)  #### update
            if(iter_count>1000):
                print("More than 1000 iterations done. Initial guess do not seem to work!")
                return current_guess
        return current_guess

Initial_guesses = [-8,-1,0,1,3,7,10,13,20,22,40,101,300,1001,1600,4500,9000,21000]

for guess in Initial_guesses:
    ##### Using try-except for error-handling purpose
    try:
        value = find_root(guess)
        print("Finding root with Initial guess = ",guess)
        print("Value(root) found = ",value,"where the function value is", f(value),"\n")
    except:
        print("Whle finding root with Initial guess = ",guess," Some problem have occured") 
        ###  Intial guesses like -10 are not recommended, 
        ###  As the e^(-x**3) value in function becomes e^(1000)
        ### which cause computation(overflow) problem