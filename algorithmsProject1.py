"""

FUNCTIONS UP HERE,,,

MAIN ON BOTTOM

"""







# define main function// front end
def main():
   
   bool = False
   while(bool == False):
       print("\nRSA keys have been generated.\nPlease select your user type:")
       print("      1. A public user")
       print("      2. Owner of key")
       print("      3. Exit program")
       choice = input("Enter your choice: ")
       
       if (choice == 1):
           # Public User
           print("As a public user, what would you like to do?")
           print("      1. Send an encrypted message")
           print("      2. Authenticate a digital signature")
           print("      3. Exit")
       elif (choice == 2):
           # Owner of key
           print("As the Owner of the Keys, what would you like to do?")
           print("      1. Decrypt a received message")
           print("      2. Digitally sign a message")
           print("      3. Show key")
           print("      4. Generate new set of key")
           print("      5. Exit")
       elif (choice == 3):
           # Exit program
           print("Bye for now!")
           bool = True 
            
           
    
    
# call main function
main()
















