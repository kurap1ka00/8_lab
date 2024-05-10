def a2(n):
  S = (len(n)+1)*(len(n)+2)/2
  s=0
  for i in n:
    s+=int(i)
  return int(S-s)

if __name__=="__main__":
    
  n = input("arr:").split()

  print(a2(n))