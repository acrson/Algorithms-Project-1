"""
Algorithms Project 1 - RSA Cryptosystem

Fathia Tafesh
Sera Yang
Carson Stell
"""
import random
import math

# OWNER content***********************************************************************

# Owner option 1 - Decrypt received message
def decryptMsg(cyphered_message, d, n):
    message = "" # Empty string
    for i in cyphered_message: # Loop through each encrypted char of the cyphered message.
        i = pow(i, d, n) # Decrpyt. Uses fast modular exponentiation with built in python function
        # Detects if the keys have been changed, if so, the value of i exceeds that of the
        # ASCII table's upper limit (i = 127).
        if (i > 127): 
            print("\nError: Unable to decrypt message. Did you change the keys?")
            break
        else: # If the keys have not been changed, continue with the decryption process
            message += chr(i) # Return encrypted char to alphabetized char
    if message != "": # Ensure the message is not empty
        print("\nThe decyphered message is: ", message)
        
    return message



# Owner option 2 - Generate ditigal signature
def genDigSig(message, d, n): 
    signature = [] # Empty list
    new_message = input("Enter a signature: ")
    capitalized_new_message = new_message.upper() # Capitalize all of the message
    
    for i in capitalized_new_message: # For each character in the message string,
        i = ord(i) # Convert current char of message to ASCII integer
        i = pow(i, d, n) # Encrypt char using private key d
        signature.append(i) # Add current encrypted char to signature string
    
    return signature, new_message 



# Owner option 3 - Print the current public and private key to the console
def showKeys(e, d):
    print("\nPublic Key:  ", e)
    print("Private Key: ", d)


# Owner option 4 - Generate a new set of keys (the following 5 functions):

# Generates a pseudo-prime number
def gen_pseudoPrime(bit_length):
    while True:
        num = random.randrange(2**(bit_length-1), 2**bit_length)
        if is_pseudoPrime(num):
            return num
        
        
        
# Checks if number is a pseudo prime number using Fermat's test
def is_pseudoPrime(num, k = 5):
    if num <= 1:
        return False
    for _ in range(k):
        a = random.randrange(2,num)
        if pow(a, num-1, num) != 1:
            return False
    return True       



# Generates a public key (e)
def findPublicKey(phi):
    e = random.randint(2,phi)
    while math.gcd(e,phi) != 1:
        e = random.randint(2,phi)
    return e



# Find the extended GCD
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)



# Find the modular inverse, return d (private key)
def findPrivateKey(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m



# OWNER MENU #

def owner(choice2, message, cyphered_message, signature, signature_name, e, n, phi, current_message):
    d = findPrivateKey(e, phi) # Generate the private key
    boolsub2 = False # Boolean value used for repetition and error handling
     
    while (boolsub2 == False):
       if (choice2[0] == '1'): # Decrypt recieved msg
           
           if (len(cyphered_message) == 0): # If the cyphered_message list is empty,
               print("\nNo messages to decypher.")
               break
           
           else: 
               decrypt_repeat = True # Boolean value used for repetition and error handling
               
               while decrypt_repeat == True:
                   index = 0
                   print("The following messages are available to decrypt: \n")
                   
                   for m in cyphered_message: # Prints each message option to decrypt
                       print(index + 1, ". ( length =", len(cyphered_message[index]), ")") # Prints all options
                       index = index + 1
                       
                   choice = input("\nEnter your choice: ")
                       
                   if choice.isdigit() == False: # Error handling: if entered choice is not a number,
                       print("\nInvalid choice made. Please choose from the available options: \n") 
                       break
                       
                   choice = int(choice) # Convert choice string to integer datatype
                       
                   if choice <= len(cyphered_message) and choice > 0: # Ensure the choice was within the specified range
                       message[choice - 1] = decryptMsg(cyphered_message[choice - 1], d, n) # Decrypt selected message
                           
                       current_message = message[choice - 1] # Set the current message to the selected message
                           
                       decrypt_repeat = False # Stop the loop
                           
                       return message, signature, signature_name, e, n, phi, current_message
                       break
                   
                   else: # If number is not within specified range, display this error message
                       print("\nInvalid choice made. Please choose from the available options: \n") 
            
       elif (choice2[0] == '2'): # Digitally sign message
           
           if (current_message == ""):
               print("\nNo messages to sign.")
               break
           
           else:
               new_signature, new_message = genDigSig(current_message, d, n) # Assign signature and signature name
               signature.append(new_signature) # Add the encrypted signature to the signature list
               signature_name.append(new_message) # Add the signature name to the signature name list
               
               print("\nDigital signature sent.")
               return message, signature, signature_name, e, n, phi, current_message
               break
           
       elif (choice2[0] == '3'): # Show keys
       
           showKeys(e, d)
           
           break
           
       elif (choice2[0] == '4'): # Generate new keys
       
           p = gen_pseudoPrime(22)
           q = gen_pseudoPrime(22)
           n = p * q
           phi = (p - 1) * (q - 1)
           e = findPublicKey(phi)
           d = findPrivateKey(e, phi)
           
           print("\nNew keys generated.\n")
           return message, signature, signature_name, e, n, phi, current_message
           
           break
          
       elif (choice2[0] == '5'):
           # Exit menu
           print("\nBye for now!\n")

           boolsub2 = True # Stop loop 
           break
    
       else:
           choice2 = input("Invalid choice made. Please enter one of the available options: ")
           
    return message, signature, signature_name, e, n, phi, current_message



# PUBLIC content*************************************************************************************

# Public option 1 - # Encrypt message M character by character by converting each char to its ASCII equivalent
def sendEncryptedMsg(e, n):
    message = input("Type your message: ")
    message = message.upper() # Convert message to be completely uppercase
    cyphered_message = [] # Initizlize empty list
    
    for i in message: # Loops through every char in message
        i = ord(i) # Converts char to int relative to ASCII
        i = pow(i, e, n) # Encrypt, return to char. Uses fast modular exponentiation with built in python function
        cyphered_message.append(i)
        
    return cyphered_message



# Public option 2 - Show list of options to authenticate. 
def authenticateDigSig(message, signature, e, n):
    sig_message = "" # Empty string
    authentic = False # Initialize boolean value to false by default
    message = message.upper() # Convert message to be completely uppercase
    
    for i in signature: # For each character in the signature string,
        i = chr(pow(i, e, n)) # Decrypt char using public key e
        sig_message += i # Add current decrypted char to sig_message string
    
    # If message and sig_message are identical, we know the signature is authentic.
    if message == sig_message: 
        authentic = True
    
    return authentic



# PUBLIC USER MENU #

def publicUser(choice2, e, n, phi, message, cyphered_message, signature, signature_name, current_message):
    repeat2 = False
    authentic = False
    
    while (repeat2 == False):
       if (choice2[0] == '1'):
           
           # calls for Pub:send encrypt
           new_message, new_cyphered_message = sendEncryptedMsg(e, n)
           
           message.append(new_message)
           cyphered_message.append(new_cyphered_message)
           
           print("\nMessage encrypted and sent.")
           #return message, cyphered_message
           
           break
            
       # authenticate digital sig.
       elif (choice2[0] == '2'):
           
           if (len(signature) == 0):
               print("\nThere are no signatures to authenticate.")
               break
           
           else:
               print("\nThe following signatures are available for authentication: \n")
               
               authentication_repeat = True
               
               while authentication_repeat == True: 
                   index = 0
                   
                   for m in signature_name: # prints each signature option
                       print(index + 1, ". ", signature_name[index])
                       index = index + 1
                       
                   choice = input("\nEnter your choice: ")
                       
                   if choice.isdigit() == False:
                       print("\nInvalid choice. Please choose from the available options: \n")
                       break
                       
                   choice = int(choice)
                       
                   if choice <= len(signature) and choice > 0:                           
                       authentic = authenticateDigSig(signature_name[choice - 1], signature[choice - 1], e, n)
                           
                       if authentic:
                           print("\nSignature is valid.")
                       else:
                           print("\nSignature is invalid.")
                            
                       authentication_repeat = False
                           
                       return message, cyphered_message, signature, signature_name
                       break
                           
                   else:
                       print("\nInvalid choice made. Please choose from the available options: \n")
                                           
          
       elif (choice2[0] == '3'):
           # Exit menu
           repeat2 = True  
           break
    
       else:
           choice2 = input("Invalid choice made. Please enter one of the available options: ")
       
    return message, cyphered_message, signature, signature_name
            
   
               
# USER TYPE content*********************************************************************************

def usertype(choice1, e, n, phi, message, cyphered_message, signature, signature_name, current_message):
    repeat1 = False
    choice2 = ['']
    while (repeat1 == False):
       if (choice1[0] == '1'):
           # Public User
           print("\nAs a public user, what would you like to do?")
           print("      1. Send an encrypted message")
           print("      2. Authenticate a digital signature")
           print("      3. Exit")
           choice2[0] = input("Enter your choice: ")
           
           # If exit is selected, exit back to the main menu.
           if (choice2[0] == '3'):
               repeat1 = True
               break
           
           # Calls for public user menu
           message, cyphered_message, signature, signature_name = publicUser(choice2, e, n, phi, message, cyphered_message, signature, signature_name, current_message) 
               
       elif (choice1[0] == '2'):
           # Owner of key
           print("\nAs the Owner of the Keys, what would you like to do?")
           print("      1. Decrypt a received message")
           print("      2. Digitally sign a message")
           print("      3. Show keys")
           print("      4. Generate a new set of keys")
           print("      5. Exit")
           choice2[0] = input("Enter your choice: ")
           
           # If exit is selected, exit back to the main menu.
           if (choice2[0] == '5'):
               repeat1 = True
               break
           
           # Calls for owner menu
           message, signature, signature_name, e, n, phi, current_message = owner(choice2, message, cyphered_message, signature, signature_name, e, n, phi, current_message)
          
       elif (choice1[0] == '3'):
           # Exit entire program
           repeat1 = True   
           break
    
       else:
           choice1 = input("Invalid choice made. Please enter one of the available options: ")
           
    return message, cyphered_message, signature, signature_name, e, n, phi, current_message
    
# MAIN content*********************************************************************************

def main():

   repeat = True
   choice1 = ['']
   
   # Variable declaration and initialization
   p = gen_pseudoPrime(22)
   q = gen_pseudoPrime(22)
   n = p * q
   phi = (p - 1) * (q - 1)
   e = findPublicKey(phi)
   message = []
   cyphered_message = []
   signature = []
   signature_name = []
   current_message = ""
   
   print("\nRSA keys have been generated.")
   
   # Main menu
   while(repeat == True):
       print("\nPlease select your user type:")
       print("      1. A public user")
       print("      2. Owner of keys")
       print("      3. Exit program")
       choice1[0] = input("Enter your choice: ")
       
       # Calls user type menu
       message, cyphered_message, signature, signature_name, e, n, phi, current_message = usertype(choice1, e, n, phi, message, cyphered_message, signature, signature_name, current_message)
       
       if choice1[0] == '3': # Check if exit was chosen
           break
 
# Call main function
if __name__ == "__main__":
    main()
















