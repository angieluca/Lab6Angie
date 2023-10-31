def encoder(password):
    pass_list = []
    # change the string characters to int, add 3, change back to str, append to list
    for i in password:
        pass_list.append(str(int(i) + 3))
    # change list to string without whitespace
    pass_string = "".join(pass_list)
    return pass_string


def decode(password):
    dec_pass = ""
    for dig in password:
        # if the integer is less than 3, the encoded number will be the same as adding 7
        if int(dig) < 3:
            dec_pass += str(int(dig) + 7)
        else:
            dec_pass += str(int(dig) - 3)
    print(f"The encoded password is {password}, and the original password is {dec_pass}.")


def main():
    stay = True
    new_pw = ""

    while stay:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")  # print menu
        user_choice = int(input("Please enter an option: "))
        # Quit option
        if user_choice == 3:
            stay = False
            break
        # Encode option
        elif user_choice == 1:
            user_pw = str(input("Please enter your password to encode: "))
            new_pw = encoder(user_pw)  # this is the input for the decoder function
            print("Your password has been encoded and stored!")
        elif user_choice == 2:
            decode(new_pw)
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()

