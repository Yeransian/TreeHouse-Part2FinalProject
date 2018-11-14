import os
import sys
import time
import caesar
import atbash
import key_word
import polybius


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def hello():
    clear_screen()
    print("Welcome agent. Press any key to begin.")
    input()
    clear_screen()


def goodbye():
    clear_screen()
    print("Thank you for using my program!\n")
    count = 3
    while count:
        sys.stdout.write("\r")
        sys.stdout.write(
            "This program will self destruct in {:2d} seconds...".format(
                count))
        sys.stdout.flush()
        time.sleep(1)
        count -= 1
    clear_screen()


def program_loop():
    available_ciphers = {
        '1': 'caesar',
        '2': 'polybius square',
        '3': 'atbash',
        '4': 'keyword'
    }


    program_running = True
    input_char = "→ "

    while program_running:


        print("The available ciphers are:")

        for option, cipher in available_ciphers.items():
            print("{}: {}".format(option, cipher))

        print(
            "Choose a cipher by entering its corresponding number below. "
            "Enter QUIT to quit.\n")


        user_input = str.lower(input(input_char))

        if user_input == "quit":
            break


        if user_input in available_ciphers:
            executing_cipher = True

            clear_screen()
            selected_cipher = available_ciphers[user_input]

            while executing_cipher:

                options = {
                    "1": "encrypting",
                    "2": "decrypting"
                }

                print(
                    "You've selected {}, are you encrypting or "
                    "decrypting?".format(str.capitalize(selected_cipher)))
                print(
                    "Enter 1 if encrypting, or 2 if decrypting. "
                    "Enter BACK to return to the main menu.\n")

                encrypt_or_decrypt = str.lower(input(input_char))

                if encrypt_or_decrypt == "back":
                    break

                elif encrypt_or_decrypt in options:

                    action = options[encrypt_or_decrypt]


                    print("Enter the text you will be {}:".format(action))
                    users_message = str.upper(input(input_char))

                    if selected_cipher == "caesar":
                        instance = caesar.Caesar()

                    elif selected_cipher == "atbash":

                        instance = atbash.Atbash()

                    elif selected_cipher == "keyword":
                        instance = key_word.Keyword()
                        # keyword cipher requires a keyword
                        print(
                            "The Keyword Cipher requires a keyword."
                            "Enter it below:")
                        cipher_keyword = str.upper(input(input_char))

                        users_message = [users_message, cipher_keyword]
                    elif selected_cipher == "polybius square":
                        # create an instance
                        instance = polybius.Polybius()

                    # run the selected action on the created instance
                    if action == "encrypting":
                        print(instance.encrypt(users_message))
                    else:
                        print(instance.decrypt(users_message))

                    executing_cipher = False

                else:
                    print(
                        "\nError. {} is not a valid option, please try "
                        "again...\n".format(encrypt_or_decrypt))

            program_running = False

        else:
            print(
                "\nError. {} is not a valid option. Please "
                "try again.\n".format(selected_cipher))

    else:
        print("Would you like to encrypt another message? [Y,n]\n")
        if input(input_char).lower() != "n":
            program_loop()


if __name__ == '__main__':

    hello()

    program_loop()

    goodbye()
