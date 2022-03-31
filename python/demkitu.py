n=str(input("nhap n : "))
i=0
print(n[i])
def demkitu(n,i):
  if (n[i]==None):
    return i
  else:
    return demkitu(n,i+1)
print("so ki tu la ",demkitu(n,i))
