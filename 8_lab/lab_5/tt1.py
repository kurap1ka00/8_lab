



def a1(w1,w2):
  strr=''
  for i in range(0,len(w1)):
    if(w1[:len(w1)-1-i] in w2):
      strr=w1[:len(w1)-1-i]
      break
  return strr

if __name__=="__main__":
  words = input("w:").split()

  s=''
  s = a1(words[0],words[1])
  for i in words:
    if(s in i):
      continue
    else:
      s = a1(s,i)


  print(s)
    
      
