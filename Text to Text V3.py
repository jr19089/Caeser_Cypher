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


def caesar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)


print("Shifted by -3 letters (A -> X)")
letters = not_blank("Please Enter Text: ")
print(caesar(letters, -3, [string.ascii_lowercase, string.ascii_uppercase]))
