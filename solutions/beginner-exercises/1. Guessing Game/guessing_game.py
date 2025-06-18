from random import randint as randomizer

def set_range():
    print("Let's define a range you would like to guess from, e.g from 1 to 100\n")
    min_num = int(input("Enter your minimum range value (an integer), inclusive: "))
    max_num = int(input("Enter your maximum range value (an integer), inclusive: "))
    while(max_num<=min_num):
        print("Error: Ensure that your minumum value is greater than the maximum value and they not equal.")
        max_num = int(input("Enter your maximum range value (an integer), inclusive:"))
    return min_num,max_num


def check_guess(target, guess,num_guesses):
    if guess < target:
        return f'Guess:{num_guesses} {guess} -> Too Low', False  
    if guess > target:
        return f'Guess:{num_guesses} {guess} -> Too high', False  
    return 'Correct!', True


def generate_random_number(min_num,max):
    return randomizer(min_num,max)


def get_user_input(min_num,max_num):
    return int(input(f'Guess a number in the range ({min_num}-{max_num}) Inclusively: '))


def play_game():
    min_num,max_num = set_range()
    target = generate_random_number(min_num,max_num)
    num_guesses = 0
    total_chances = 4

    message = ''
    is_correct= False

    while not is_correct and total_chances != num_guesses :
        user_guess = get_user_input(min_num,max_num)
        num_guesses+=1
        message, is_correct = check_guess(target,user_guess,num_guesses)
        print(message)
    print(f'Total Guesses: {num_guesses}')
    

if __name__ == "__main__":
    play_game()