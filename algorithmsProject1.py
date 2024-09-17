"""

FUNCTIONS UP HERE,,,

MAIN ON BOTTOM

"""







# define main function// front end
def main():
    print("\nRSA keys have been generated.\nPlease select your user type:")
    print("      1. A public user")
    print("      2. Owner of key")
    print("      3. Exit program")
    choice = input("Enter your choice: ")
    
    # verification thingy for user type
    # uh, read ur notes Sera, in "Scratch'
    # we are doing this on paper first :[ 
    bool = False
    while(bool == False):
        if (choice == 1):
            print("As a public user, what would you like to do?")
            print("      1. Send an encrypted message")
            print("      2. Authenticate a digital signature")
            print("      3. Exit")
            # add snippet thingy
            bool = True
        elif (choice == 2):
            print ("hi")
        elif (choice == 3):
            print("hi")
        else:
            print("hi")
        
    
    
# call main function
main()

