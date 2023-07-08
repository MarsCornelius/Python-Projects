############################################################################
#                                                                          #
#                          Created By: Kibwe Gooding                       #
#                             Date: July 7th 2023                          #
#                              A Simple Converter                          #
############################################################################
import random


def gen_random_letter():
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z']

    random_char = random.choice(upper + lower)
    return random_char


def gen_random_numbers():
    numerical = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    random_num = random.choice(numerical)

    return random_num


def gen_random_chars():
    special = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=']
    random_spec = random.choice(special)

    return random_spec


def gen_letter_or_number():
    value = ['1', '2', '3']
    random_val = random.choice(value)

    return random_val


if __name__ == "__main__":
    length = int(input("Select length of password: "))
    password = ""

    while len(password) < length:
        char = gen_letter_or_number()
        match char:
            case '1':
                password += gen_random_numbers()
            case '2':
                password += gen_random_letter()
            case '3':
                password += gen_random_chars()

    print(password)
