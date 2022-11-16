import string


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("This Cannot Be Blank")


answer = not_blank("Please Enter Text: ")
shift = -3

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

cipher = answer.translate(table)

print(cipher)
