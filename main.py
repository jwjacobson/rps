import random
import typer
from rich import print, box
from rich.prompt import Prompt
from rich.table import Table

class Weapon:
    def __init__(self, name, beats):
        self.name = name
        self.beats = beats

    def __repr__(self):
        return f'{self.name} | beats {self.beats}'


choices = ['rock', 'paper', 'scissors']

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
    choice = Prompt.ask("[bold]What do you choose?", choices=choices)
    return choice

def computer_choice():
    return random.choice(choices)

def main(
        computer_choice: str = typer.Argument(default_factory=computer_choice),
        player_choice: str = typer.Argument(default_factory=player_choice)
    ):
    print(f'You choose {player_choice}!')
    print(f"Computer chooses {computer_choice}!")
    if player_choice == computer_choice:
        print('Draw...')
    

if __name__ == "__main__":
    typer.run(main)
