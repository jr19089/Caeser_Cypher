import string


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("This Cannot Be Blank")
# Used to stop input from being blank


shift = -3
print("Shifted by -3 letters (A -> X) ")
answer = not_blank("Please Enter Text: ")
# Is where user inputs text, as well as the number text is shifted by

alphabet = string.ascii_lowercase + string.ascii_uppercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)
# this section is where the translation is made

cipher = answer.translate(table)
# Uses the previous translation to

print("Cipher Made: {}".format(cipher))
# How the encrypted text is shown
