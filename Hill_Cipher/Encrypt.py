"""Program to encrypt a message using Hill_Cipher
Inputs: msg.txt, key.txt
Output: ciphertext.txt
Note: Messages of sizes indivisible by m will have a padding 'x' at the end
"""


import sys
def Encrypt(key,msg):
   # Reading the key from the file and creating a matrix
   KEY = []
   k = open(key,"r")
   lines = k.readlines()
   for l in lines:
       r = l.split()
       row=[]
       for i in r:
          
          row.append(int(i))
       KEY.append(row)
   
   #finding the value of m   
   order = len(KEY)
   k.close()
   # Reading the message in chunks of m and storing each chunk of length m in a matrix
   MSG =[]   
   m = open(msg,"r")
   
   while True:
        c=m.read(order)
        if not c:
           break
        else:
              ele = []
              #padding with x if last chunk has less than m characters
              if(len(c) % order > 0):
                  
                  c += 'x' * (order - (len(c) % order))
                  
                 
              for i in c:
                
                # mapping each character to a number between 0 to 25
                e = ord(i)-97
                ele.append(e)
              
                 
              MSG.append(ele)
   
   
   m.close()
   #Encrypting the message
   cipher=""
   #Performing a modulo multiplication of the key matrix and the message matrix 
   #and then converting the numbers back to characters
   for a in MSG:
      for b in zip(*KEY):
        
        cipher+=chr(sum(ea*eb for ea,eb in zip(a,b))%26+97) 
     
  
   #Writing the cipher to a file
   c=open("ciphertext.txt","w")
   c.write(cipher)
   c.close()

key=sys.argv[1]
msg=sys.argv[2]   
Encrypt(key,msg)