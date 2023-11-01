def menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")

def encoder(initial_password):
    final_password = ''
    for number in initial_password:
        final_password += str((int(number) + 3) % 10)
    return final_password

def main():
    while True:
        menu()
        user_option = int(input("\nPlease enter an option: "))
        if user_option == 1:
            initial_password = input("Please enter your password to encode: ")
            if initial_password.isnumeric() and len(initial_password) == 8:
                encoded_password = encoder(initial_password)
                print("Your password has been encoded and stored!\n")
            else:
                print("Invalid password\n")
                continue
        elif user_option == 2:
            None
        elif user_option == 3:
            break
        else:
            print("Enter a valid menu option\n")
            continue

if __name__ == "__main__":
    main()