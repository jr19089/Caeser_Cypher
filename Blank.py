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

invalid = "invalid choice"
while invalid == "invalid choice":
    choices = input("Make or solve a Caesar Cipher? ").lower()
    check = valid_check(choices, valid_input)

    if check == "Make" or check == "Solve":
        print("*Program continues*")
        break
