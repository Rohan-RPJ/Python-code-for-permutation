'''TO FIND ALL POSSIBLE STRINGS FROM A GIVEN STRING
   AUTHOR : ROHAN P. JAIN
   DATE : 28-1-19
   BELOW IS THE LINK FOR THIS CODE ON REPL.IT CODING PLATFORM
   https://repl.it/@Rohan_PP/Permutation-of-a-string'''

n=input("Enter length of string\n")
j = 0

def noOfpermutations(n):
  l=1
  for x in range(2,n+1):
    l=(l+1)*x
  return l

nop=noOfpermutations(n)
p = ['0']*nop

def perms(s):
  global p,j
 
  #print "s=",s
  if len(s) is 1:
    if s not in p:
      p[j]=s
      j+=1
      #print "j=",j
      if j>nop:
        return 0
  else:
    perms(s[1:])
    if s not in p:
      p[j]=s
      j+=1
      #print "j=",j
      if j>nop:
        return 0
    s = s[1:] + s[0]
    if s not in p:
      perms(s)

def main():
  global p
  s=raw_input("Enter a string with non-repeated characters\n")
  #print noOfpermutations(len(s))
  perms(s)
  print "All combination possibilities\n"
 
  #for i in p:
  #  print i

  if '0' in p:
    k=p.index('0')
    #print k
    i=0
    while i<n:
      for string in p:
        if string is '0':
          break
        if string.find(s[i]) is -1:
          if s[i]+string not in p:
            p[k]=s[i]+string
            #print p[k]
            k+=1
      i+=1
      if i is n:
        if '0' in p:
          i=0

  #print i
  p = sorted(p)

  for i in p:
    print i

  print "Number of permutations =",nop
main()
