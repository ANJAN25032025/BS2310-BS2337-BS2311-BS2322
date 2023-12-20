import math
def predictor(b,c,r):
    b = int(b)
    c = int(c)
    r = int(r)
    if c == 0:
        print("WE WILL ASK THE PREDICTOR PREDICT THE SKI AT THE FIRST DAY")
    elif r >= b:
        print("WE WILL BUY THE SKI AT THE FIRST DAY")
    elif b < c:
        print("WE WILL BUY THE SKI AT",round(b/r)," th DAY")
    else:
        o = 1 + (math.sqrt(((c+1)**2)+4*c*(b-1))+c-1)/(2*b)
        t = (1 - c + math.sqrt(((c+1)**2)+4*b*c))/2
        if c >= o*b:
            print("WE WILL BUY THE SKI AT",round(b/r)," th DAY")
        else:
            print("WE WILL ASK THE PREDICTOR AT ",round(t),"th DAY")
        
b = input("ENTER THE COST OF THE SKI:")
c = input("ENTER THE COST OF THE PREDICTOR:")
r = input("ENTER THE COST OF THE RENT:")
predictor(b,c,r)
