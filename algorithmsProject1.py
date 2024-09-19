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

# OWNER content****************************************************************************************************************************

# Owner option 1

# Owner option 2

# Owner option 3

# Owner option 4

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
def sendEncryptedMsg():
    print("hi")
    

# public option 2
def authenticateDigSig():
    print("hi")

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
















