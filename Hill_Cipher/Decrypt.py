"""
Program to decrypt a message encrypted by Hill Cipher
Inputs: ciphertext.txt, key.txt
Output: output.txt
Note: Messages of sizes indivisible by m will have a padding 'x' at the end
"""
import numpy
import sys

# Extended Euclidean algorithm for calculating modulo inverse of a number
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

# function to calculate modulo inverse    
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m

# function to compute the minor of a matrix
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

# function to compute adjoint of a matrix
def getMatrixInverse(m):

    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1], -1*m[0][1]],
                [-1*m[1][0], m[0][0]]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * int(round(numpy.linalg.det(minor)))%26)
        cofactors.append(cofactorRow)
    #Transpose of cofactor matrix    
    cofactors = list(map(list,zip(*cofactors)))
    return cofactors

# function to perform decrryption    
def Decrypt(key,ciphertext):
   # Reading key from the file and creating a key matrix
   KEY = []
   k = open(key,"r")
   lines = k.readlines()
   for l in lines:
       r = l.split()
       row=[]
       for i in r:
          row.append(int(i))
       KEY.append(row)
   k.close()
   #Calculating the determinant using numpy 
   Dete = int(round(numpy.linalg.det(KEY)))
   #Getting the adjoint
   Adjoint = getMatrixInverse(KEY)
  
   #Finding the modulo inverse of the determinant
   Determinant = modinv(Dete,26)
   
   #Computing m
   order = len(KEY)
   
   #Creating a cipher matrix by reading the file ciphertext.txt in chunks
   CIPHER =[]   
   m = open(ciphertext,"r")
   
   while True:
        c=m.read(order)
        if not c:
           break
        else:
              ele = []
              
              for i in c:
                e = ord(i)-97
                ele.append(e)
              
                 
              CIPHER.append(ele)
   m.close()
   #Decrypting the cipher text by multiplying Cipher matrix and Key inverse modulo 26
   #and then converting the elements from the resulting matrix to characters   
   output=""
   
   for a in CIPHER:
      for b in zip(*Adjoint):
        
        output+=chr((sum(ea*eb for ea,eb in zip(a,b))*int(Determinant))%26+97) 
         
  
 
   
   #Writing the decrypted text to a file
   c=open("output.txt","w")
   c.write(output)
   c.close()

key = sys.argv[1]
ciphertext = sys.argv[2]   
Decrypt(key,ciphertext)