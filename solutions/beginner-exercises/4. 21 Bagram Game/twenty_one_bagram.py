from random import randint 

def starting_game():
    choices = {'y':'First','n':'Second'}
    while True:
        player_pos = input('Do you want to go first (Y/n)? ').lower()
        if player_pos not in 'yn':
            print("ℹ️ Info: Please ensure you have entered 'Y' for yes or 'N' for no!\n")
        else:
            break
    print(f'You have chosen to go {choices[player_pos]}!')
    return player_pos=='y'


def is_validate_submission(submission,last_value):
    submission_list = submission.split(',')
    print(submission_list)
    num_of_values = len(submission_list)
    if (num_of_values == 1 and int(submission_list[0])-1 == last_value):
        return True
    
    if num_of_values>4:
        return False
    
    for i in range(num_of_values-1):
        if int(submission_list[i])+1 != int(submission_list[i+1]):
            return False
        
    return int(submission_list[0])==last_value+1

def add_to_list(progress,total_values):
    for i in range(1,total_values):
        last_value = progress[-1]
        progress.append(last_value+1) 
    
    
def current_player(is_player):
     return '🤔 You: ' if is_player else '💻 Computer: '
 

def play_game():
    # Give Game Intro TODO
    # Choose who goes first
    is_player = starting_game()
   
    playing = True
    progress = [0]
    
        
    while playing:
        print(f"\n{'-'*30}\nGame State: {','.join(str(x) for x in progress)}\n{'-'*30}\n")
        if is_player:
            submission = input(f"{current_player(is_player)} e.g 1,2,3 > ")
            try:
                value = int(submission.replace(",",""))
                print(value)
                is_valid = is_validate_submission(submission,progress[-1])
                print(is_valid)
                if not is_valid:
                    print('❌ Game Over, You have been disqualified')
                    playing=False
                    break
                else:
                    add_to_list(progress,len(submission))
                    is_player = not is_player
            except:
                print('❌ Please enter only numbers in the format e.g 5,6')
        else:
            total_values = randint(1,4)
            add_to_list(progress,total_values)
            print(f"{current_player(is_player)}: {progress[-total_values:]}")
            is_player = not is_player
      
    print('End of Game')
   

if __name__ == "__main__":
    play_game()