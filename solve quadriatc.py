## solve quadratic
try: ## no letters

    A = float(input("What is your A varible? ")) ## get ^2 value
    if A == 0: ## check for values that dont work
        print("cannot put 0 into quadratic")
    #print(A) testing

    B = float(input("What is your B varible? "))## x value
    if B == 0: ## check for values that dont work
        print("cannot put 0 into quadratic")
    #print(B) testing

    C = float(input("What is your C varible? ")) ## get constant value
    if C == 0: ## check for values that dont work
        print("cannot put 0 into quadratic")
    #print(C) testing

except ValueError:  ## no letters
    print("Please use real numbers for your varibles. ")
    exit()

d4AC = float(B ** 2.0 - 4.0 * (A * C)) ## defines discrim
## i also forgot why theres a d there but its there now
if d4AC < 0:
    print("no real solutions")
else: 
    sqrt_d4AC = d4AC ** 0.5 ## 1/2 can get weird w order of ops - use 0.5

    dPlus = (-B + sqrt_d4AC) / (2 * A) 
    dMinus = (-B - sqrt_d4AC) / (2 * A) ## this is only here bc i cant do plus or minus in python

    print(dPlus)

    print(dMinus)