import string


def valid_check(choice, options):
    chosen = ""

    for var_list in options:

        if choice in var_list:
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        return "invalid choice"


valid_input = [
    ["make", "m", "encrypt", "e"],
    ["solve", "s", "decrypt", "d"]
]
# This is to help create an error when input is invalid. Applies to Valid Check as well.


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("This Cannot Be Blank")
# Used to stop input from being blank


invalid = "invalid choice"
while invalid == "invalid choice":
    choices = input("Make or solve a Caesar Cipher? ").lower()
    check = valid_check(choices, valid_input)
# Used to initiate the Validity Check

    if check == "Make":
        shift = -3
        print("Shifted by -3 letters (A -> X)")
        answer = not_blank("Please Enter Text: ")
# Is where user inputs text, as well as the number text is shifted by

        alphabet = string.ascii_lowercase + string.ascii_uppercase
        shifted = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted)
# this section is where the translation is made

        cipher = answer.translate(table)
# Uses the previous translation to

        print("Cipher Made: {}".format(cipher))
        break
# How the encrypted text is shown

    elif check == "Solve":
        shift = 3
        print("Shifted by 3 letters (A -> D)")
        answer = not_blank("Please Enter Text: ")

        alphabet = string.ascii_lowercase + string.ascii_uppercase
        shifted = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted)

        cipher = answer.translate(table)
# This code is the same as the above set, just this time the number has changed

        print("Cipher Solved: {}".format(cipher))
        break
# How the Decrypted text is shown
