import string


def int_check(number, error):
    valid = False

    while not valid:
        try:
            response = int(input(number))

            if response != "":
                return response
            else:
                print(error)
        except ValueError:
            print(error)


key = "A"
shift = int_check("What whole number do you want to shift by? ", "This must be a whole number, Positive or Negative")

alphabet = string.ascii_lowercase + string.ascii_uppercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

full_key = key.translate(table).upper()

print("Shifted by {} letters (A -> {})".format(shift, full_key))
