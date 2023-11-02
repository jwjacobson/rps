import random
import typer
from rich import print, box
from rich.prompt import Prompt
from rich.table import Table

weapon_lst = ['rock', 'scissors', 'paper']
weapon_dict = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

def offering():
    table = Table(box=box.ASCII, show_edge=False, leading=True)
    table.add_column(':boom-text:')
    table.add_column('[bold magenta]Choose your weapon')
    table.add_row(':mountain:', '[red]rock')
    table.add_row(':memo-text:', '[yellow]paper')
    table.add_row(':kitchen_knife-text:', '[cyan]scissors')
    print('\n')
    print(table)
    print('\n')

def player_choice():
    offering()
    choice = Prompt.ask("[bold]What do you choose?", choices=weapon_lst)
    return choice

def computer_choice():
    return random.choice(weapon_lst)

def main(
        computer_choice: str = typer.Argument(default_factory=computer_choice),
        player_choice: str = typer.Argument(default_factory=player_choice)
    ):
    print(f'You choose {player_choice}!')
    print(f"Computer chooses {computer_choice}!")
    if player_choice == computer_choice:
        print('Draw...')
    elif weapon_dict[player_choice] == computer_choice:
        print(f'{player_choice.title()} beats {computer_choice}.')
        print('Player wins!')
    else:
        print(f'{computer_choice.title()} beats {player_choice}.')
        print('Computer wins!')
    

if __name__ == "__main__":
    typer.run(main)
