import math

def b1(n):
    n=n+1
    return int((((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n)/math.sqrt(5))


if __name__=="__main__":
    n = int(input("К-во ступенек:"))
    print(b1(n))