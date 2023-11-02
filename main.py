import random
import typer
from rich.prompt import Prompt

# def offering():
#     print('Choose your wea')

def player_choice():
    choice = Prompt.ask("Choose your weapon")
    return choice

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def main(
        computer_choice: str = typer.Argument(default_factory=computer_choice),
        player_choice: str = typer.Argument(default_factory=player_choice)
    ):
    print(f'You choose {player_choice}!')
    print(f"Computer chooses {computer_choice}!")

if __name__ == "__main__":
    typer.run(main)

player_choice()