def encode(code):
    digits = [int(d) for d in str(code)]
    for i in range(len(digits)):
        digits[i] += 3
        if digits[i] == 10:
            digits[i] = 0
            continue
        if digits[i] == 11:
            digits[i] = 1
            continue
        if digits[i] == 12:
            digits[i] = 2
            continue
    return int("".join(map(str, digits)))

def decode():
    pass

if __name__ == "__main__":
    encoder = True
    while encoder:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            code = int(input("Please enter your password to encode: "))
            encoded_password = encode(code)
            print("Your password has been encoded and stored\n")
        if option == 2:
            # decode stored password
            pass
        if option == 3:
            encoder = False
