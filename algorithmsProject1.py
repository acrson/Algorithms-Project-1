"""

FUNCTIONS UP HERE,,,

MAIN ON BOTTOM

"""







"""

This is all code relative to the main driver vvv


completed:
    - main
    - user type

to do:
    - public user
    - owner
    * debug main 

***figure out return stuff,,, idk if i did it right or not

"""



# Owner content****************************************************************************************************************************

#print("      1. Decrypt a received message")
#print("      2. Digitally sign a message")
#print("      3. Show key")
#print("      4. Generate new set of key")
#print("      5. Exit")

def owner(choice2):
    boolsub2 = False
    while (boolsub2 == False):
        print("hi")
    

# Public user content********************************************************************************************************************

#print("      1. Send an encrypted message")
#print("      2. Authenticate a digital signature")
#print("      3. Exit")
        

def publicUser(choice2):
    boolsub2 = False
    while (boolsub2 == False):
        print("hi")
   
               
# User Type content********************************************************************************************************************
def usertype(choice1):
    boolsub = False
    while (boolsub == False):
       if (choice1 == 1):
           # Public User
           print("As a public user, what would you like to do?")
           print("      1. Send an encrypted message")
           print("      2. Authenticate a digital signature")
           print("      3. Exit")
           choice2 = input("Enter you choice: ")
           
           # calls for public user menu
           publicUser(choice2)
               
       elif (choice1 == 2):
           # Owner of key
           print("As the Owner of the Keys, what would you like to do?")
           print("      1. Decrypt a received message")
           print("      2. Digitally sign a message")
           print("      3. Show key")
           print("      4. Generate new set of key")
           print("      5. Exit")
           choice2 = input("Enter you choice: ")
           
           # calls for owner menu
           owner(choice2)
          
       elif (choice1 == 3):
           # Exit program
           print("Bye for now!")
           boolsub = True   
           return 0
    
       else:
           choice1 = input("Invalid choice made. Please enter one of the available options: ")
           


# main content************************************************************************************************************************************
def main():

   bool = False
   while(bool == False):
       print("\nRSA keys have been generated.\nPlease select your user type:")
       print("      1. A public user")
       print("      2. Owner of key")
       print("      3. Exit program")
       choice1 = input("Enter your choice: ")
       
       #calls  user type
       usertype(choice1)
            
   # end function/while loop
   return 0
            

# call main function
main()
















