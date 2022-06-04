import string
import sys, threading
import socket

from sympy import true
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)



#############################################################

def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]
#print(ConvertToStr(ConvertToInt('Number Theory')))

def GCD(a, b):
  if b == 0:
    return a
  return GCD(b, a % b)

def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

# this is an R2L recursive implementation that works for large integers
def PowMod(a, n, mod): 
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod

def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n # we don't want -ve integers
    return b



def Decrypt(c, p, q, e):
    t=(p-1)*(q-1)
    d=InvertModulo(e,t)
    n=p*q
    m=PowMod(c,d,n)
    m=ConvertToStr(m)
    return m


#ciphertext = Encrypt("attack", modulo, exponent)

#print(message)



#################################################################
# Create a socket object


import socket
file1 = open("myfile.txt","r+") 
i=0
file1.seek(0)
while True :
  
  s = socket.socket()
  port = 56789
  s.connect(('127.0.0.1', port))

  
  p=int(file1.readline())
  print("p= "+str(p))
  q=int(file1.readline())
  print("q= "+str( q))
  n=p*q
  print("First part of public key is %d"%n)
  a=(p-1)*(q-1)
  print("Euler Totient function is %d\n"%a)
  e=int(file1.readline())
  print("e= "+str( e))
  print("Public key is n=%d , e=%d\n"%(n,e))

  s.send(str.encode(str(n)))
  s.send(str.encode(str(e)))
  m=int((s.recv(2048)).decode('utf-8'))
  print("Recieved encrypted message is %d"%m)

  decmsg=Decrypt(m, p, q, e)
  print('Decrypted message : '+decmsg)

  print('----------------------------------')

  cdash=int((s.recv(2048)).decode('utf-8'))
  Y=Decrypt(cdash, p, q, e)
  Y=ConvertToInt(Y)
  s.send(str.encode(str(Y)))
  
  s.close()

