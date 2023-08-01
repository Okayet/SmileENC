#Creator Okayet/Deserved
#Give republishing the code with modifications
#smile it looks good on u :)
import random

# Dictionary to map numbers to pipes
mapping = {
    0: "|-",
    1: "|.",
    2: "|--",
    3: "|..",
    4: "|---",
    5: "|...",
    6: "|----",
    7: "|....",
    8: "|-----",
    9: "|....."
}


def translate(code):
    mapping = {
        "|-": "0",
        "|.": "1",
        "|--": "2",
        "|..": "3",
        "|---": "4",
        "|...": "5",
        "|----": "6",
        "|....": "7",
        "|-----": "8",
        "|.....": "9"
    }
    output = ""
    segments = code.split("|")  # Split the code string into individual segments
    for segment in segments:
        if segment != "":
            output += mapping.get("|" + segment, "")  # Look up the segment in the mapping
    return output


def decrypted():
    d = input("Enter a code you want to decrypt: ")
    decrypted_number = translate(d)
    
    if decrypted_number == "":
        print("Invalid code. Please enter a valid code.")
        return
    
    print("Decrypted number:", decrypted_number)

    print("Hello, do you have keys of the encrypted version?")
    print("1). Yes, of course, how come I'll read it without keys >.<")
    print("2). No, I'm a good person and i like to smile!")
    print("3). Quit, I like people who i trust!")
    choiceD = input("Choose from 1, 2, 3: ")

    if choiceD == "1":
        print("Okay, sure. How many keys do you have?")
        num_keys = int(input("Enter a number: "))

        keys = []
        for i in range(num_keys):
            key = int(input("Enter key {}: ".format(i + 1)))
            keys.append(key)

        print("Your decryption keys are:", keys)

        print("Which operation do you want to use?")
        print("1). Addition")
        print("2). Subtraction")
        print("3). Multiplication")
        print("4). Division")
        operation_choice = input("Choose from 1, 2, 3, 4: ")

        if operation_choice == "1":
            result = int(decrypted_number) // sum(keys)
            print("Your decrypted message is:", result)
        elif operation_choice == "2":
            result = int(decrypted_number) + sum(keys)
            print("Your decrypted message is:", result)
        elif operation_choice == "3":
            result = int(decrypted_number)
            for key in keys:
                result *= key
            print("Your decrypted message is:", result)
        elif operation_choice == "4":
            result = int(decrypted_number)
            for key in keys:
                result //= key
            print("Your decrypted message is:", result)
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

    elif choiceD == "2":
        print("Sorry, without keys, the message cannot be decrypted.")

    elif choiceD == "3":
        print("Goodbye!")
        exit()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")



        
def number_to_pipes(number):
    # Convert the number to a string so we can access each digit
    number_string = str(number)

    # Create a list to store the pipe representation of each digit
    pipes = []

    # Loop through each digit in the number string and get its pipe representation
    for digit in number_string:
        # Get the pipe representation for this digit
        pipe = mapping[int(digit)]
        # Add the pipe representation to the list
        pipes.append(pipe)

    # Join the pipe representations of each digit into a single string without any separator
    return "".join(pipes)


def encrypted():
    o = input("Enter a number you want to encrypt: ")
    print(number_to_pipes(int(o)))  # Output: "|.|--|..|---|...|----|....|-----|....."

    print("Hello, do you want your encryption to have keys?")
    print("1). Yes, of course it's better.")
    print("2). No, I'm a cutie patootie.")
    print("3). Quit, I'm love helpting people!")
    choice1 = input("Choose from 1, 2, 3: ")

    if choice1 == "1":
        print("Okay, sure. How many keys do you want?")
        num_keys = int(input("Enter a number: "))

        keys = []
        for i in range(num_keys):
            key = int(input("Add every number for every key you made: "))
            keys.append(key)

        print("Your encryption keys are:", keys)

        print("Which operation do you want to use?")
        print("1). Addition")
        print("2). Subtraction")
        print("3). Multiplication")
        print("4). Division")
        operation_choice = input("Choose from 1, 2, 3, 4: ")

        if operation_choice == "1":
            result = sum(keys) * int(o)
            print("Your encrypted message is:", number_to_pipes(result))
        elif operation_choice == "2":
            result = int(o) - sum(keys)
            result = int(o) - sum(keys)
            print("Your encrypted message is:", number_to_pipes(result))
        elif operation_choice == "3":
            result = int(o)
            for key in keys:
                result *= key
            print("Your encrypted message is:", number_to_pipes(result))
        elif operation_choice == "4":
            result = int(o)
            for key in keys:
                result //= key
            print("Your encrypted message is:", number_to_pipes(result))
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

    elif choice1 == "2":
        o = input("Enter a number you want to encrypt: ")
        encrypted_num = int(o)
        print("Your encrypted message is:", number_to_pipes(encrypted_num))

    elif choice1 == "3":
        print("Goodbye!")
        exit()

def help():
    print("Looks like you have chosen to help yourself!")
    choice5 = input("Enter a number you: im stuck with dobby type 1). idk how this works explain 2). I'm a softie so please don't harm me 3).")
    if choice5 == "1":
        print("I think Dobby is unavoidable, so I can't help.")
    elif choice5 == "2":
        print("This encryption system works by adding pipes and dots as numbers. The only way to decrypt it is by having a key!")
        print("Although if there's no key, there's no message or letter.")
    elif choice5 == "3":
        print("Damn bro, you're a bitch like Dobby!")
        exit()
    else:
        print("Invalid number. Please enter a rational number!")


print("""╔══╗░░░░╔╦╗░░╔═════╗
║╚═╬════╬╣╠═╗║░▀░▀░║
╠═╗║╔╗╔╗║║║╩╣║╚═══╝║
╚══╩╝╚╝╚╩╩╩═╝╚═════╝
""")
print("WELCOME to my enc/dec method called SMILE!")
print("1). Encrypt a message using SMILE!")
print("2). Decrypt a message using SMILE!")
print("3). Help! Seems like you are stuck. Let me help you!")
print("4). Exit")

print("5). use a new tool to convert nums in words!!")

while True:
    choice = input("Please choose a number between 1-4: ")

    if choice == "1":
         encrypted()
    elif choice == "2":
        decrypted()
    elif choice == "3":
        help()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")
