import termcolor    # import termcolor library
import cprint       # import cprint library
import random       # import random library

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '~' ,'!', '@', '$',
'%', '^', '&', '*'] # list with all the random characters 

class Password:
    def GeneratePassword(self):
        password = ''   # starting password
        length = input("Enter the number of characters long the password will be : (Press Enter for total randomness)")
        if length == '':    # if they press enter
            size = random.randint(5,40)   # size will be from 5 to 40
            for num in range(size):     # iterate over the size
                char = random.choice(characters)  #choose a random character from the characters list      
                password += char        # add that character to the password
        else:
            size = int(length)      # size will be equal to length
            for num in range(size):     # iterate over the size
                char = random.choice(characters)    # choose a random character from the characters list
                password += char        # add the character to the password

        termcolor.cprint(f"Your password is : {password} ","green")     # print out the password in green

generate = Password()       # make an instance of Password called generate
generate.GeneratePassword()     # Run the generate Password method
