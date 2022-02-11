import os
import time
import random
from typing import List

MAX_TRIES = 6
WORD_LENGTH = 5


def paint(string: str, color: str = "white", bold: bool = False) -> str:
    ANSI_codes = {
        "white": 0,
        "red": 31,
        "green": 32,
        "yellow": 33
    }
    return f"\u001b[{ANSI_codes[color]}{';1' * bold}m{string}\u001b[0m"


def clear_screen(delay: float = 0.5) -> None:
    time.sleep(delay)
    os.system("cls" if os.name == "nt" else "clear")


def update_ui(history: List[str], tries: int) -> None:
    clear_screen()
    print(paint("P L V R A", bold=True), end="\n\n")
    for guess in history:
        print(guess)
    for i in range((MAX_TRIES - tries)):
        print("· · · · ·")


def format_guess(guess: str, ans: str) -> str:
    guess = list(guess)
    for index, char in enumerate(guess):
        if ans[index] == char:
            color = "green"
        elif char in ans[index:] or char in ans[:index]:
            color = "yellow"
        else:
            color = "red"
        guess[index] = paint(f"{char.upper()}", color)
    return " ".join(guess)


def driver() -> None:
    with open("words.txt", "r") as file:
        ans = random.choice(file.read().split("\n"))
    tries = 0
    history = []
    guess = ""

    while tries < MAX_TRIES and guess != ans:
        update_ui(history, tries)

        guess = input("\n")
        if len(guess) != WORD_LENGTH:
            print(paint(
                f"\nApenas palavras com {WORD_LENGTH} letras são válidas.\n", "yellow", bold=True))
            continue

        history.append(format_guess(guess, ans))
        tries += 1
    update_ui(history, tries)

    if guess == ans:
        print(paint(
            f"\nVocê conseguiu em {tries} tentativa{'s' * (tries > 1)}!", "green", bold=True))
    else:
        print(paint(f"\nA palavra era {ans}...", "red", bold=True))

def main() -> None:
    try:
        driver()
    except KeyboardInterrupt:
        pass        
    finally:
        clear_screen()


if __name__ == "__main__":
    main()
