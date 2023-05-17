def is_prime(x):
  #first cancels anything under 2
  if x < 2:
    print str(x) +" False"
    return False
  #now ranging up it checks
  else:
    #-1 as to not use the last number and above2
    for n in range(2,x-1):
      #modulo passes if while divisor
      if x % n == 0:
        return False
    else:
      return True
      print "True"


is_prime(9)
