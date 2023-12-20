

import math
def asking_predictor(b,t,n,m,p,l,c,h):
    b = int(b)
    t = int(t)
    n = int(n)
    m = int(m)
    p = int(p)
    l = int(l)
    c = int(c)
    h = float(h)
    if t >= m:
        if p == 0 and l == 0:
            print("We will ask the predictor at the first day and for whole length") 
        elif n*c >= (b + n*h*c) :
            print("We will buy the bahncard at the first day and we have no need to ask the predictor")
        elif b < p:
            print("We will buy the bahncard at",round((b + n*h*c)/n*c),"th day and we have no need to ask the predictor")
        else:
            o = 1 + (math.sqrt(((p + l +1)**2)+4*(p+l)*(b+n*h*c-1))+p+l-1)/(2*(b+n*h*c))
            t = (1 - p + l + math.sqrt(((p+l+1)**2)+4*(b+n*h*c)*(p + l)))/2
            if p + l >= o*(b+n*h*c):
                print("WE WILL BUY THE SKI AT",round((b+n*h*c)/(n*c))," th DAY")
            else:
                print("WE WILL ASK THE PREDICTOR AT ",round(t),"th DAY and for only one time")

    if t < m:
        if b + h*c < c + p:
            print("We will always buy the bahncard at the day of request and there is no necessary of the predictor")
        else:
            i = 1
            while i < n-1:
                if i*c < b + i*c*h and (i + 1)*c >= b + (i +1)*c*h:
                    if  (i + 1)*c - (b + (i +1)*c*h) >= p + t*l :
                        print("Go to the predictor at the day of request and ask him to predict for the time interval of validity of the card and we have to go to the predictor for "
                              ,round(m/t),"time")
                    else:
                        print("No need to go predictor and use randomized algorithm to determine 2 - h approximation")
                i += 1
                

b = input("ENTER THE COST OF THE BAHNCARD:")
t = input("ENTER THE VALIDITY OF THR CARD:")
n = input("ENTER THE NUMBER OF TRAVEL REQUEST:")
m = input("ENTER THE LENGTH OF INTERVAL:")
p = input("ENTER THE COST OF PREDICTION PER TIME:")
l = input("ENTER THE COST OF PREDICTION PER INTERVAL:")
c = input("ENTER THE COST OF TICKETS:")
h = input("ENTER THE DISCOUNT RATE(This value is between 0 and 1):")            
asking_predictor(b,t,n,m,p,l,c,h)
