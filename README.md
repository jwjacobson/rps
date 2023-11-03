# RPS: CLI rock paper scissors simulator

### About the project
This past week I've been reading through the documentation for the **Typer** and **Rich** libraries. Typer is used for passing CLI arguments and options to programs, and Rich is for adding beautiful formatting to CLI programs. To practice and consolidate what I learned, this afternoon I coded up a little rock paper scissors game.

### About the game
![image](https://github.com/jwjacobson/rps/assets/116485484/5d1b47f7-1b3a-4445-b845-3a8fe11ea42a)

The program plays a single game of rock paper scissors against the computer. You can determine both your own choice and the computer's by means of CLI arguments when you run the program, or you can make your choice from within the program and the computer will select randomly. After determining and announcing the winner, the program ends.

### Prerequisites
RPS is written entirely in **Python 3** and depends on the **Typer** and **Rich** libraries. Specifically, it was written using **Python 3.11.5**, **Typer 0.9.0**, and **Rich 13.6.0**. It has not been tested with other versions of Python or the libraries.

### Installation
The easiest way to play RPS is by [cloning this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) then setting up a **virtual environment** to install the dependencies in their proper versions. Once you've cloned the repo, take the following steps:
1. Navigate to the 'rps' directory.
2. Create a virtual environment (not strictly necessary, but you may end up installing some unneeded Python packages to your system if you don't): ```python -m venv venv``` (Windows/Linux) or ```python3 -m venv venv``` (Mac).
3. Activate the virtual environment by typing ```. venv/bin/activate``` (Linux/Mac) or ```.\venv\Scripts\activate``` (Windows).
4. Install the necessary packages: ```pip install -r requirements.txt``` Now your system is ready to run RPS!

### Running the program
From the RPS directory, simply type ```python main.py``` (Windows/Linux) or ```python3 main.py``` (Mac) and follow the onscreen instructions.

If you want to explore other options via the command line, the beautiful help message will guide you:
```python main.py --help``` :
![image](https://github.com/jwjacobson/rps/assets/116485484/f4fab86c-9089-4c5c-993e-984958da78b4)



### License
RPS is [free software](https://www.fsf.org/about/what-is-free-software), released under version 3.0 of the GPL. Everyone has the right to use, modify, and distribute RPS subject to the [stipulations](https://github.com/jwjacobson/oopmanor/blob/main/License) of that license.
