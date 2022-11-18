import string

# This is how we get the string.ascii to work in the following codes.


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
# Used to stop input from being blank.


def caesar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)
# This is how the encrypted and decrypted text is made, the main part of the program.


invalid = "invalid choice"
while invalid == "invalid choice":
    choices = input("Make or solve a Caesar Cipher? ").lower()
    check = valid_check(choices, valid_input)
# Used to initiate the Validity Check, displaying an error if it is not valid.

    if check == "Make":
        print("Shifted by -3 Letters (A -> X)")
        letters = not_blank("Please Enter Text: ")
        print("Cipher Made: {}".format(caesar(letters, -3, [string.ascii_lowercase, string.ascii_uppercase])))
        break
    elif check == "Solve":
        print("Shifted by 3 Letters (A -> D)")
        letters = not_blank("Please Enter Text: ")
        print("Cipher Solved: {}".format(caesar(letters, 3, [string.ascii_lowercase, string.ascii_uppercase])))
        break
# This is how the main program is run, and how it displays the Key and outputted message.
# This also is where the not blank function works, similar to the Valid function but not
# dependent on lists.
