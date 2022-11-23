
secret_word = "giraffe"
guess = ""
count = 0

while guess.lower() != secret_word.lower():
    guess = input("Enter guess: ")
    count += 1
    if secret_word.lower() == guess.lower():
        print("You did it!")

    elif count == 3:
        print("Sorry")
        break



