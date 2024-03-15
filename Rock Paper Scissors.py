import random 

## Numerical representation of Rock Paper Scissors
user_dict = {"Rock": 1, "Paper": 2, "Scissors": 3}
computer_dict = {"Rock": -1, "Paper": -2, "Scissors": -3}

## Defining a function that numerically compares moves in Rock Paper Scissors
def compareMoves(user_move, computer_move):
    """
    Adds the values of the computer's move and the user's move and returns
    the winner of the game based on the result.
    
    Args:
        user_move (string): the user's choice 
        computer_move (string): the computer's choice
        
    Returns:
        "The game is a draw": If the sum == 0
        "User has won the game!": If the sum == 1, -2
        "The computer has won the game!": If the sum == -1, 2
    
    """
    x = user_dict[user_choice] + computer_dict[computer_choice]
    if x == 0:
        return "The game is a draw!"
    elif x == 1 or x == -2:
        return f"{user_name} has won the game!"
    else:
        return "The computer has won the game!"

## Entering user name
print("\n\nWelcome to Rock Paper Scissors! Please enter your name:")
user_name = input()

repeat_game = "Yes"
while repeat_game == "Yes":
    
    ## Entering choice of move
    print(f"---\nChoose your move {user_name}, (Rock, Paper, Scissors):")
    user_choice = input()
    user_choice = user_choice.capitalize()
    
    ## Generating computer's choice at random
    computer_choice = random.choice(list(computer_dict.keys()))
    
    ## Stating the two choices
    print(f"---\nYou choose {user_choice}, the computer chooses {computer_choice}!\n")
    
    ## Output of the compareMoves function
    print(compareMoves(user_choice, computer_choice))
    
    # Play again prompt
    print("\n---\nWould you like to play again? (Yes or No)")
    repeat_game = input()
    repeat_game = repeat_game.capitalize()