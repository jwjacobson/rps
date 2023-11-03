import random
import typer
from rich import print, box
from rich.prompt import Prompt
from rich.table import Table

weapon_lst = ['rock', 'scissors', 'paper']
weapon_dict = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

def offering():
    """
    Prints a table with the possible weapon choices.
    """
    table = Table(box=box.ASCII, show_edge=False, leading=True)
    table.add_column(':boom-text:')
    table.add_column('[bold magenta]Choose your weapon')
    table.add_row(':mountain:', '[red]rock')
    table.add_row(':memo-text:', '[yellow]paper')
    table.add_row(':kitchen_knife-text:', '[cyan]scissors') # using a knife because the scissors emoji looked small and weird
    print('\n')
    print(table)
    print('\n')

def player_choice():
    """
    The player chooses rock, paper, or scissors when the program is run.
    """
    offering()
    choice = Prompt.ask("[bold]What do you choose?", choices=weapon_lst)
    return choice

def computer_choice():
    """
    The computer chooses randomly from the available options.
    """
    return random.choice(weapon_lst)

def main(
        name: str = typer.Argument("Player", help="The name of the player."),
        computer_choice: str = typer.Argument(default_factory=computer_choice, help='The computer\'s random choice.'),
        player_choice: str = typer.Argument(default_factory=player_choice, help='The player\'s choice.')
    ):
    """
    Play a game of rock paper scissors against the computer.
    """
    print(f'\nYou choose {player_choice}.')
    print(f"Computer chooses {computer_choice}.\n")
    if player_choice == computer_choice:
        print('[bold bright_white]Draw...')
    elif weapon_dict[player_choice] == computer_choice:
        print(f'{player_choice.title()} beats {computer_choice}.')
        print(f'[bold bright_cyan]{name.title()} wins!')
    else:
        print(f'{computer_choice.title()} beats {player_choice}.')
        print('[bold bright_red]Computer wins!')
    

if __name__ == "__main__":
    typer.run(main)
