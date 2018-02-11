
import numpy
import sys

# function to compute gcd
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def GenerateRandomMatrix(m):
   #Generating a random matrix using numpy
   max=numpy.random.randint(2,26)
   Key = numpy.random.randint(0,max,size=(m,m))
   #Finding the determinant of that matrix  
   Det = int(round(numpy.linalg.det(Key)))
   return Key,Det
 
def KeyGen(m):
       Key,Det = GenerateRandomMatrix(m)
       
       # Checking for invertibility of the matrix
       # Determinant needs to be non zero and invertible in mod 26
       
       count = 0
       while (Det==0 or gcd(Det,26)!=1):
          Key,Det = GenerateRandomMatrix(m)
          count+=1
          
          print("Trying to find an invertible key..."+ str(count)+" attempt! ")
          
       
       print("Found a suitable key!")
       #Formatting matrix for file
       K=""
       for i in Key:
          for j in i:
               
               K+=str(j)+" "
          K+="\n"
          
       f = open("key.txt","w")
       f.write(K)
       f.close()

m=int(sys.argv[1])
KeyGen(m)
