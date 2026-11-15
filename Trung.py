import os
import random

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
RESET = "\033[0m"
MAGENTA = "\033[95m"
GRAY = "\033[90m"
BOLD = "\033[1m"


def banner(title, color=CYAN):
    print(f"{color}{BOLD}╔{'═' * 30}╗{RESET}")
    print(f"{color}{BOLD}║{title.center(30)}║{RESET}")
    print(f"{color}{BOLD}╚{'═' * 30}╝{RESET}")


def win_screen(code, hint=None, extra=None):
    print(f"\n{GREEN}{BOLD}PUZZLE SOLVED!{RESET}")
    if extra:
        print(f"{CYAN}{extra}{RESET}")
    print(f"{YELLOW}{BOLD}🔑 Chest code: {code}{RESET}")
    if hint:
        print(f"{MAGENTA}💡 Hint: {hint}{RESET}")


def lose_screen(reason, code):
    print(f"\n{RED}{BOLD}💀 PUZZLE FAILED!{RESET}")
    print(f"{GRAY}{reason}{RESET}")
    print(f"{YELLOW}{BOLD}🔑 Chest code: {code}{RESET}")
    print(f"{GRAY}No bonus hint for you this time!{RESET}")


def wordle_game():


    WORDS = [
        "python", "rocket", "planet", "garden", "bridge", "castle",
        "forest", "island", "jungle", "magnet", "pencil", "silver",
        "window", "dragon", "monkey", "orange", "purple", "yellow",
        "coffee", "doctor", "flower", "guitar", "hammer", "winter"
    ]

    WORD_LENGTH = 6
    MAX_ATTEMPTS = 6


    def clear():
        os.system("cls" if os.name == "nt" else "clear")


    def check_guess(secret, guess):
        result = ["gray"] * WORD_LENGTH
        remaining = list(secret)

        for i in range(WORD_LENGTH):
            if guess[i] == secret[i]:
                result[i] = "green"
                remaining[i] = None

        for i in range(WORD_LENGTH):
            if result[i] == "green":
                continue

            if guess[i] in remaining:
                result[i] = "yellow"
                remaining[remaining.index(guess[i])] = None

        return result


    def color_letter(letter, status):
        colors = {
            "green": GREEN,
            "yellow": YELLOW,
            "gray": GRAY
        }

        return f"{colors[status]}[{letter.upper()}]{RESET}"


    def draw_board(history):
        print()
        banner("WORDLE", CYAN)
        print()

        for guess, result in history:
            row = ""

            for ch, status in zip(guess, result):
                row += color_letter(ch, status) + " "

            print(row)

        for _ in range(MAX_ATTEMPTS - len(history)):
            print("[ ] [ ] [ ] [ ] [ ] [ ]")

        print()


    def play():

            secret = random.choice(WORDS)
            history = []

            while len(history) < MAX_ATTEMPTS:

                    clear()
                    draw_board(history)

                    guess = input(
                        f"Guess #{len(history) + 1}/{MAX_ATTEMPTS}: "
                    ).lower().strip()

                    if len(guess) != WORD_LENGTH or not guess.isalpha():
                        print("\nWord must contain exactly 6 letters.")
                        input("Press Enter...")
                        continue

                    result = check_guess(secret, guess)
                    history.append((guess, result))

                    if guess == secret:
                        clear()
                        draw_board(history)

                        win_screen("B@D!", "Num is alpha, alpha is num", extra=f"The secret word was {secret.upper()}")

                        return True

            clear()
            draw_board(history)

            lose_screen(f"The word was {secret.upper()}.", "B@D!")
            return False






    return play()
if __name__=="__main__":
    wordle_game()