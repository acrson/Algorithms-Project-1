"""
COMPLETED (still need debugging while methods are incomplete):
    - main
    - user type
    - public menu (outline)
    - owner menu (outline)
    * as far as I know, it may not be fully completed until we fin code and start debugs

to-do (as far as Sera knows):
    - public user: options 1, 2
    - owner: options 1, 2, 3, 4
    - Check if all exits and menu thingies work properly,, some might depend
      on if methods are completed so we can see what it looks like fully functioned
    * I'M STILL DEBUGGING PLEASE BE CAREFUL ToT

OTHER NOTES:
    - if u want to change the formatting of methods or anything, feel free to!!!
        this current outline is just for Sera's reference


"""
import random
import math

# OWNER content****************************************************************************************************************************

# Owner option 1 - decrypt received message, show list of received messages to choose from
# Decrypt message
def decryptMsg(cyphered_message, d, n):#THIS FUNCTION
    # d = findPrivateKey()
    # Decrypt message C character by character by converting each int back to the ASCII equivalent
    message = "" # Empty string
    for i in cyphered_message: # Loop through each char of the cyphered message.
        i = pow(i, d, n) # Decrpyt, return to char. Uses fast modular exponentiation with built in python function
        message += chr(i)
    print("The decyphered message is: ", message)
    return message


# Owner option 2 - digitally sign a message
# Generate digital signature
def genDigSig(message, d, n): #THIS FUNCTION
    signature = [] # Empty string
    message = message.upper() # Capitalize all of the message
    
    for i in message: # For each character in the message string,
        i = ord(i) # Convert current char of message to ASCII integer
        i = pow(i, d, n) # Encrypt char using private key d
        signature.append(i) # Add current encrypted char to signature string
    
    return signature



# Owner option 3 - show the keys #THIS FUNCTION
def showKeys(e, d):
    # show both the public and private keys
    print("Public Key:  ", e) #does this refer to just e or (e, n)?
    print("Private Key: ", d)



# Owner option 4 - generate new set of keys
# Generate keys

#Checks if number is a pseudo prime number using Fermat's test
def is_pseudoPrime(num, k = 5):
    if num <= 1:
        return False
    for _ in range(k):
        a = random.randrange(2,num)
        if pow(a, num-1, num) != 1:
            return False
    return True

#Generates a pseudo prime number
def gen_pseudoPrime(bit_length):
    while True:
        num = random.randrange(2**(bit_length-1), 2**bit_length)
        if is_pseudoPrime(num):
            return num
        
#Generates a public key (e)
def findPublicKey(phi):
    e = random.randint(2,phi)
    while math.gcd(e,phi) != 1:
        e = random.randint(2,phi)
    return e

#Find the extended gcd
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

#Find the modular inverse
def findPrivateKey(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m


#owner menu!!!!!!!!!!
def owner(choice2, message, cyphered_message, e, n, phi):
    d = findPrivateKey(e, phi) # Find the private key
    signature = []
    
    boolsub2 = False 
    while (boolsub2 == False):
       if (choice2[0] == '1'):
           # Decrypt recieved msg
           message = decryptMsg(cyphered_message, d, n)
           return message, signature, e, n, phi 
           break
            
       elif (choice2[0] == '2'):
           # digitally sign msg
           
           if (message == ""):
               print("\nNo message to sign.")
               break
           
           else:
               signature = genDigSig(message, d, n)
               print("Digital signature sent.\n")
               return message, signature, e, n, phi 
               break
           
       elif (choice2[0] == '3'):
           # show keys
           showKeys(e, d)
           
           break
           
       elif (choice2[0] == '4'):
           # Generate new keys
           p = gen_pseudoPrime(22)
           q = gen_pseudoPrime(22)
           n = p * q
           phi = (p - 1) * (q - 1)
           e = findPublicKey(phi)
           d = findPrivateKey(e, phi)
           
           print("\nNew keys generated.\n")
           return message, signature, e, n, phi 
           
           break
          
       elif (choice2[0] == '5'):
           # Exit menu
           print("\nBye for now!\n")

           boolsub2 = True   
           break
    
       else:
           choice2 = input("Invalid choice made. Please enter one of the available options: ")
           
    return message, signature, e, n, phi 


# PUBLIC content********************************************************************************************************************

#public option 1
def sendEncryptedMsg(e, n): #THIS FUNCTION
    # Encrypt message M character by character by converting each char to its ASCII equivalent
    message = input("Type your message: ")
    message = message.upper()
    cyphered_message = [] # empty list
    for i in message:
        i = ord(i) # converts char to int relative to ASCII
        i = pow(i, e, n) # encrypt, return to char. Uses fast modular exponentiation with built in python function
        cyphered_message.append(i)
    print("The cyphered message is: ", cyphered_message)
    return message, cyphered_message



# public option 2 - show list of options to authenticate, if none say none
def authenticateDigSig(message, signature, e, n):
    sig_message = "" # Empty string
    authentic = False # Initialize boolean value to false by default
    
    for i in signature: # For each character in the signature string,
        i = chr(pow(i, e, n)) # Decrypt char using public key e
        sig_message += i # Add current decrypted char to sig_message string
    
    # If message and sig_message are identical, we know the signature is authentic.
    if message == sig_message: 
        authentic = True
    
    return authentic



#public user menu!!!!!!
def publicUser(choice2, e, n, phi, message, signature):
    repeat2 = False
    authentic = False
    cyphered_message = ""
    
    while (repeat2 == False):
       if (choice2[0] == '1'):
           
           # calls for Pub:send encrypt
           message, cyphered_message = sendEncryptedMsg(e, n)
           
           print("Message encrypted and sent.")
           #return message, cyphered_message
           
           break
               
       elif (choice2[0] == '2'):
           # authenticate digital sig.
           
           # calls Pub:authenticate
           authentic = authenticateDigSig(message, signature, e, n)
           
           if authentic:
               print("Signature is valid.")
           else:
               print("Signature is invalid.")
           
           break
           
          
       elif (choice2[0] == '3'):
           # Exit menu
           repeat2 = True  
           break
    
       else:
           choice2 = input("Invalid choice made. Please enter one of the available options: ")
       
    return message, cyphered_message
            
   
               
# USER TYPE content********************************************************************************************************************
def usertype(choice1, e, n, phi, message, cyphered_message, signature):
    repeat1 = False
    choice2 = ['']
    while (repeat1 == False):
       if (choice1[0] == '1'):
           # Public User
           print("\nAs a public user, what would you like to do?")
           print("      1. Send an encrypted message")
           print("      2. Authenticate a digital signature")
           print("      3. Exit")
           choice2[0] = input("Enter you choice: ")
           
           # calls for public user menu
           if (choice2[0] == '3'):
               repeat1 = True
               break
           
           #else:
           message, cyphered_message = publicUser(choice2, e, n, phi, message, signature)
           
          
               
       elif (choice1[0] == '2'):
           # Owner of key
           print("\nAs the Owner of the Keys, what would you like to do?")
           print("      1. Decrypt a received message")
           print("      2. Digitally sign a message")
           print("      3. Show keys")
           print("      4. Generate new set of key")
           print("      5. Exit")
           choice2[0] = input("Enter you choice: ")
           
           if (choice2[0] == '5'):
               repeat1 = True
               break
           
           # calls for owner menu
           message, signature, e, n, phi = owner(choice2, message, cyphered_message, e, n, phi)
          
       elif (choice1[0] == '3'):
           # Exit program
           repeat1 = True   
           break
    
       else:
           choice1 = input("Invalid choice made. Please enter one of the available options: ")
           
    return message, cyphered_message, signature, e, n, phi
    
# MAIN content************************************************************************************************************************************
def main():

   repeat = True
   choice1 = ['']
   
   # Variable declaration
   p = gen_pseudoPrime(22)
   q = gen_pseudoPrime(22)
   n = p * q
   phi = (p - 1) * (q - 1)
   e = findPublicKey(phi)
   message = ""
   cyphered_message = ""
   signature = ""
   
   print("\nRSA keys have been generated.")
   
   while(repeat == True):
       print("\nPlease select your user type:")
       print("      1. A public user")
       print("      2. Owner of keys")
       print("      3. Exit program")
       choice1[0] = input("Enter your choice: ")
       
       #calls  user type
       message, cyphered_message, signature, e, n, phi = usertype(choice1, e, n, phi, message, cyphered_message, signature)
       
       #print("public key: ", e)

       
       if choice1[0] == '3':  # Check if exit was chosen
           #repeat = False
           break
 
# call main function
if __name__ == "__main__":
    main()
















