import random
import typer

def player_choice():
    pass

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def main(computer_choice: str = typer.Argument(default_factory=computer_choice)):
    print(f"Computer chooses {computer_choice}!")

if __name__ == "__main__":
    typer.run(main)