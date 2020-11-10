import random


def user_guess():
    '''
    Function user_guess returns the number entered by the user.
    If user entered not a number, the function will ask to enter data until the data is of type int.
    '''
    while True:
        try:
            number = int(input("Guess the number between 1 and 100: "))
            break
        except ValueError:
            print("It's not a number!")
    return number


def guess():
    '''
    Function guess checks if the user guessed the number.
    '''
    user_number = user_guess()
    random_number = random.randint(1, 100)
    while user_number != random_number:
        if user_number < random_number:
            print("Too small!")
        elif user_number > random_number:
            print("Too big!")
        user_number = user_guess()
    if user_number == random_number:
        print("You win!")


if __name__ == '__main__':
    guess()
