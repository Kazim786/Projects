
phoneBook = {"key" : "281-701-8297" } 

def electric_PhoneBk (phone_Book):
    while True:

        print("Electronic phone book")
        print((input("1. Look up an entry" + "\n\n" + "2. Set an entry " + "\n\n" + "3. Delete an entry" + "\n\n" + "4. List all entries" + "\n\n" + "5. Quit")))
        ask = int(input("What do you want to do (1-5)? "))
        

        print(ask)
        
    # For loop requires the size of the dictionary. Hence you cant use it here since you are adding to the phonebook        
        if (ask == 1):
            key_word = input("Enter the key ")
            look_up = phone_Book[key_word]
            print(look_up)
        elif (ask == 2):
            the_name = input("Enter a name ")
            the_number = input("Enter Phone Number ")
            phone_Book[the_name] = the_number
            print(phone_Book)
        elif (ask == 3):
            key_word = input("Enter the key ")
            del phone_Book[key_word]
            print(phone_Book)
        elif (ask == 4):
            contents = phone_Book.items()
            print(contents)
        elif (ask == 5):
            exit()

print(electric_PhoneBk(phoneBook))
