import random
import typer
from rich import print, box
from rich.prompt import Prompt
from rich.table import Table


def offering():
    print('[bold bright_magenta]Choose your weapon:')
    print(':moai: [bold yellow]rock')
    print(':newspaper: [bold green]paper')
    print(':scissors: [bold cyan]scissors')

table = Table(box=box.ASCII, show_edge=False, leading=True)
table.add_column(':boom-text:')
table.add_column('[bold magenta]Choose your weapon')
table.add_row(':mountain:', '[red]rock')
table.add_row(':memo-text:', '[yellow]paper')
table.add_row(':kitchen_knife-text:', '[cyan]scissors')

print(table)

def player_choice():
    choice = Prompt.ask("[bold]Choose your weapon")
    return choice

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# def main(
#         computer_choice: str = typer.Argument(default_factory=computer_choice),
#         player_choice: str = typer.Argument(default_factory=player_choice)
#     ):
#     print(f'You choose {player_choice}!')
#     print(f"Computer chooses {computer_choice}!")

# if __name__ == "__main__":
#     typer.run(main)

# offering()