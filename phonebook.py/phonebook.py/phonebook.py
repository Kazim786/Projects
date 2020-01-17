
phoneBook = {"key" : "281-701-8297" } 

def electric_PhoneBk (phone_Book):

    "Electronic phone book"
    print((input("1. Look up an entry" + "\n\n" + "2. Set an entry " + "\n\n" + "3. Delete an entry" + "\n\n" + "4. List all entries" + "\n\n" + "5. Quit")))
    ask = int(input("What do you want to do (1-5)? "))
    key_word = input("Enter the key ")

    print(ask)
    for o in phone_Book:
        

        if (ask == 1):
            look_up = phone_Book[key_word]
            print(look_up)
        elif (ask == 2):
            look_up ["key "] = [""]
            print(look_up)
        elif (ask == 3):
            look_up = phone_Book[key_word]
            print(look_up)
        elif (ask == 4):
            look_up = phone_Book[key_word]
            print(look_up)
        elif (ask == 5):
            look_up = phone_Book[key_word]
            print(look_up)

print(electric_PhoneBk(phoneBook))
