from cProfile import label
import math
from multiprocessing import Process,Pipe
import sys, threading
from sympy.ntheory import factorint ,primefactors
from datetime import timedelta
import socket 
from timeit import default_timer as timer
import matplotlib.pyplot as plt
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
import time
import math
def countTotalBits(num):
     
     # convert number into it's binary and
     # remove first two characters 0b.
     binary = bin(num)[2:]
     return len(binary)




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




def Encrypt(m, n, e):
    encint=ConvertToInt(m)
    c=PowMod(encint,e,n)
    return c

def is_square(x):
   #if x >= 0,
    if(x >= 0):
        sr = int(math.sqrt(x))
        # sqrt function returns floating value so we have to convert it into integer
        #return boolean T/F
        return ((sr*sr) == x)
    return 0
    



        
    



import socket
s = socket.socket()
print('Socket succesfully created')
port = 56789

s.bind(('', port))
print(f'socket binded to port{port}')
s.listen(5)
print('Socket is listening')
import time



x=[]
y=[]
z=[]
i=0

file1 = open("myfile2.txt","r+") 
file1.seek(0)
while True:
    
    c, addr = s.accept()
    n = c.recv(2048).decode()
    n = int(n)
    e = c.recv(2048).decode()
    e = int(e)
    y.append(countTotalBits(n))
    
    
    val=input('enter message : ')
    
    start = timer()
    ciphertext =str( Encrypt(val, n, e))
    end = timer()
    

    x.append(end-start)
   
    c.send(ciphertext.encode())
    plt.scatter(y, x, color= "green",
            marker= "o", s=30,label='Time to encrypt')
 
# x-axis label
    plt.xlabel('Key Size ---> n (in bits) ')
# frequency label
    plt.ylabel('Time in seconds')
# plot title
    plt.title('Relation bet size of n , time')
    plt.grid()
    plt.legend()
    plt.show()
 
# function to show the plot
   
    print('-------------------------------------------------------')
    print('Cracking the RSA.......')
    
    
    start2=timer()
    p,q=primefactors(n)
    d=InvertModulo(e,(p-1)*(q-1))
    end2=timer()
    print('p , q are : ',p,',',q)
    print('Private key (d) :', d)
    
    
    z.append((end2-start2))
    
    plt.scatter(y, z, color= "red",
            marker= "*", s=30,label='Time to break')
 
# x-axis label
    plt.xlabel('Key Size ---> n (in bits) ')
# frequency label
    plt.ylabel('Time in seconds')
# plot title
    plt.title('Relation bet size of n , time')

 
# function to show the plot
    plt.grid()
    plt.legend()
    plt.show()
    
    print('----------------------------------------------')
    print('Chosen Cipher attack CCA')
    
    r=int( file1.readline())
    print("r= "+str(r))
    Cdash=PowMod(PowMod(r,e,n)*PowMod(int(ciphertext),1,n),1,n)
    c.send(str(Cdash).encode())
    
    Y = c.recv(2048).decode()
    Y = int(Y)
    
    inverseR=InvertModulo(r,n)
    M=PowMod(PowMod(inverseR,1,n)*PowMod(Y,1,n),1,n)
    print('M : ',ConvertToStr(M))
    
    c.close()
   