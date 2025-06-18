from random import randint

def print_level_intro(level, chances):
    objective = {
        1:f'Code Cracker: Guess the generated number in the range 1-20 inclusive.\nYou have {chances} Chances to figure it out.',
        2:f'Secret Word: Guess the generated word between (python,coding,wizard,techie).\nYou have {chances} Chances to figure it out.',
        3:f'Hangman: Guess the generated number in the range 1-20 inclusive.\nYou have {chances} Chances to figure it out.'
    }
    print('~'*60)
    print(f'Welcome to the guessing game, LEVEL {level} of 3\nObjective: {objective[level]}')
    print('~'*60)


def print_success_msg():
    print('🏆'*30)
    print("✅ Congratulations, That's Correct, you advance to the next level.")
    
    
def number_guess_game():
    chances = 4
    user_attempts = 0
    target = randint(1,20)
    is_correct = False;
    
    print_level_intro(1, chances)
    
    while not is_correct and chances!=user_attempts:
        guess = int(input('Guess the drawn number between 1-20: '))
        user_attempts+=1
        is_correct = guess == target
        if is_correct:
            level = 2
            print_success_msg()
            return True, level
        if guess < target:
            print('Too Low')
        else: 
            print('Too High')
        print(f"❌: Oops that's incorrect, let's retry. Attempts Left:{chances-user_attempts}")

    return False, 1


def word_guess_game():
    six_letter_words = ['python','coding','wizard','techie','coders']
    chances = 6
    target = six_letter_words[randint(0,3)]
    is_correct = False;
    user_attempts = 0
    print_level_intro(2, chances)
    while not is_correct and chances!=user_attempts:
        guess = input("Guess the drawn word between ('python','coding','wizard','techie','coders'): ")
        user_attempts+=1
        is_correct = guess.lower() == target
        if is_correct:
            level = 3
            print_success_msg()
            return True, level
        print(f"❌: Oops that's incorrect, let's retry. Attempts Left:{chances-user_attempts}")
    
    return False, 2


def placeholder():
    None


def draw_hangman():
    print()

def hangman_game():
    chances = 7
    print_level_intro(3, chances)
    
    stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
    
    return False, 3
    
    
def play_game(level):
    if level == 1:
        return number_guess_game()
    elif level == 2:
        return word_guess_game()
    else:
        return hangman_game()


if __name__ == "__main__":
    level = 1
    chances = 0
    playing = True
    
    draw_hangman()
    
    """ while playing:
       playing, level = play_game(level)
       
    if level <=3:
        print(f'Game Over, Unfortunately you failed level {level}')
    else:
        print('Game Over, Congratulations you have completed all levels') """