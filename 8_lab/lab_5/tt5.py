import math
def a5(n):
    return int((((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n)/math.sqrt(5))

if __name__=="__main__":
    n=int(input("n="))

    print(a5(n ))

