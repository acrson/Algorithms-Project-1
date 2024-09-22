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
    message = '' # Empty string
    for i in cyphered_message: # Loop through each char of the cyphered message.
        i = ord(i) # Convert to ASCII
        i = chr(pow(i, d, n)) # Decrpyt, return to char. Uses fast modular exponentiation with built in python function
        message += i
    print('The decyphered message is: ', message)



# Owner option 2 - digitally sign a message
# Generate digital signature
def genDigSig(message, d, n): #THIS FUNCTION
    signature = '' # Empty string
    message = message.upper() # Capitalize all of the message
    
    for i in message: # For each character in the message string,
        i = ord(i) # Convert current char of message to ASCII integer
        i = chr(pow(i, d, n)) # Encrypt char using private key d
        signature += i # Add current encrypted char to signature string
    
    return signature



# Owner option 3 - show the keys #THIS FUNCTION
def showKeys(e, d):
    # show both the public and private keys
    print('Public Key:  ', e) #does this refer to just e or (e, n)?
    print('Private Key: ', d)



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
def modinv(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m


#owner menu!!!!!!!!!!
def owner(choice2):
    boolsub2 = False
    while (boolsub2 == False):
       if (choice2[0] == '1'):
           # Decrypt recieved msg
           print("hi")
            
       elif (choice2[0] == '2'):
           # digitally sign msg
           print("hi")
           
       elif (choice2[0] == '3'):
           # show key
           print("hi")
           
       elif (choice2[0] == '4'):
           # generate new key
           print("hi")
          
       elif (choice2[0] == '5'):
           # Exit menu
           print("Bye for now!")
           boolsub2 = True   
           return
    
       else:
           choice2 = input("Invalid choice made. Please enter one of the available options: ")
    

# PUBLIC content********************************************************************************************************************

#public option 1
def sendEncryptedMsg(e, n): #THIS FUNCTION
    # Encrypt message M character by character by converting each char to its ASCII equivalent
    message = input('Type your message: ')
    message = message.upper()
    cyphered_message = '' # empty string
    for i in message:
        i = ord(i) # converts char to int relative to ASCII
        i = chr(pow(i, e, n)) # encrypt, return to char. Uses fast modular exponentiation with built in python function
        cyphered_message += i
    print('The cyphered message is: ', cyphered_message)



# public option 2 - show list of options to authenticate, if none say none
def authenticateDigSig(message, signature, e, n):
    sig_message = '' # Empty string
    authentic = False # Initialize boolean value to false by default
    
    for i in signature: # For each character in the signature string,
        i = ord(i) # Convert current char of signature to ASCII integer
        i = chr(pow(i, e, n)) # Decrypt char using public key e
        sig_message += i # Add current decrypted char to sig_message string
    
    # If message and sig_message are identical, we know the signature is authentic.
    if message == sig_message: 
        authentic = True
    
    return authentic



#public user menu!!!!!!
def publicUser(choice2):
    boolsub2 = False
    encryptedMsg = [""]
    while (boolsub2 == False):
       if (choice2[0] == '1'):
           encryptedMsg[0] = input("Enter a message: ")
           
           # calls for Pub:send encrypt
           sendEncryptedMsg()
           
           print("Message encrypted and sent.")
           return
               
       elif (choice2[0] == '2'):
           # authenticate digital sig.
           
           # calls Pub:authenticate
           authenticateDigSig()
          
       elif (choice2[0] == '3'):
           # Exit menu
           print("Bye for now!")
           boolsub2 = True   
           return
    
       else:
           choice2 = input("Invalid choice made. Please enter one of the available options: ")
            
   
               
# USER TYPE content********************************************************************************************************************
def usertype(choice1):
    boolsub = False
    choice2 = ['']
    while (boolsub == False):
       if (choice1[0] == '1'):
           # Public User
           print("\nAs a public user, what would you like to do?")
           print("      1. Send an encrypted message")
           print("      2. Authenticate a digital signature")
           print("      3. Exit")
           choice2[0] = input("Enter you choice: ")
           
           # calls for public user menu
           publicUser(choice2)
               
       elif (choice1[0] == '2'):
           # Owner of key
           print("\nAs the Owner of the Keys, what would you like to do?")
           print("      1. Decrypt a received message")
           print("      2. Digitally sign a message")
           print("      3. Show key")
           print("      4. Generate new set of key")
           print("      5. Exit")
           choice2[0] = input("Enter you choice: ")
           
           # calls for owner menu
           owner(choice2)
          
       elif (choice1[0] == '3'):
           # Exit program
           print("Bye for now!")
           boolsub = True   
           return
    
       else:
           choice1 = input("Invalid choice made. Please enter one of the available options: ")
           

# BACK-END content****************************************************************************************

# possibly a generate p and q function but idk
 
# Finds the private key d for the public user before messasge can be decrypted
def findPrivateKey(phi, e): #THIS FUNCTION
    (x, y, d) = extendedGCD(e, phi)
    return d # Returns the private key

# Use Extended Euclid's Algorithm to find (x, y, d) such that d = gcd(a, b) = ax + by
def extendedGCD(a, b): #THIS FUNCTION
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extendedGCD(b, a % b)
    return (y, (x - (a // (b * y))), d)
    
# MAIN content************************************************************************************************************************************
def main():

   bool = False
   choice1 = ['']
   while(bool == False):
       print("\nRSA keys have been generated.\nPlease select your user type:")
       print("      1. A public user")
       print("      2. Owner of key")
       print("      3. Exit program")
       choice1[0] = input("Enter your choice: ")
       
       #calls  user type
       usertype(choice1)
       
       if choice1[0] == '3':  # Check if exit was chosen
            break
 
# call main function
if __name__ == "__main__":
    main()
















