import math
def asking_predictor(u,v,c,b):
    u = int(u)
    v = int(v)
    c = int(c)
    b = int(b)
    if u >= b:
        if  b >= v and  (b + math.sqrt(b*b - v*v)) >= u:
            f = (math.sqrt(v*v + (u-b)**2)-(u-b))/2
        else:
            f = b /(1 + ((u*u)/(v*v)))
    else:
        if   b >= v and u >= (b + math.sqrt(b*b - v*v)):
            f = (math.sqrt(v*v + (b-u)**2)-(b - u))/2
        else:
            f = u - (b/(1 + ((v*v)/(u*u))))


    if c > f:
        print("Don't ask the predictor")
    else:
        print("Ask the predictor")


u = input("ENTER THE MEAN:")
v = input("ENTER THE VARIANCE:")
c = input("ENTER THE COST OF THE PREDICTOR:")
b = input("ENTER THE COST OF A SKI:")
asking_predictor(u,v,c,b)
