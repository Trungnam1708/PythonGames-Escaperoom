import os
import sys
import time
import shutil

from Tesst import wordle_game
from Aarav import reactor_puzzle
from Ayana import maze_game

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
RESET = "\033[0m"
MAGENTA = "\033[95m"
GRAY = "\033[90m"
BOLD = "\033[1m"


def clear_screen():
    """Clears the console screen across different operating systems."""
    os.system('cls' if os.name == 'nt' else 'clear')


def check_terminal_size():
    """Checks whether the terminal meets the minimum 80x24 requirement."""

    while True:
        size = shutil.get_terminal_size(fallback=(80, 24))

        if size.columns >= 80 and size.lines >= 24:
            break

        clear_screen()

        print("=" * 80)
        print(" TERMINAL SIZE REQUIREMENT: MINIMUM 80x24 ".center(80, "="))
        print(
            f" Current terminal size: {size.columns} columns x {size.lines} rows. "
            .center(80)
        )
        print(
            " Please resize your terminal window before continuing. "
            .center(80)
        )
        print("=" * 80)

        input(" Press Enter after resizing the terminal...")


def show_storyline():
    clear_screen()
    print("=" * 40)
    print(" THE PUZZLE ADVENTURE")
    print("=" * 40)
    print()
    story_lines = [
"John is stranded on a spaceship.",
"If he does not get out soon, the spaceship may fail.",
"He must solve a sequence of puzzles",
"to reach the control room door.",
"Can he escape? Play to find out!"
]
    for line in story_lines:
        for ch in line:
            print(ch, end="", flush=True)
            time.sleep(0.04)
        print()
    print()
    input("Press Enter to help John escape...")
    clear_screen()


def banner(title, color=CYAN):
    print(f"{color}{BOLD}╔{'═' * 30}╗{RESET}")
    print(f"{color}{BOLD}║{title.center(30)}║{RESET}")
    print(f"{color}{BOLD}╚{'═' * 30}╝{RESET}")


def win_screen(code, hint=None, extra=None):
    print(f"\n{GREEN}{BOLD}🎉 PUZZLE SOLVED!{RESET}")
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


notes = []


def show_notes():
    print(f"\n{MAGENTA}{BOLD}📓 CLUE NOTEBOOK{RESET}")
    if not notes:
        print(f"{GRAY}Nothing yet. Open a chest to find clues!{RESET}")
    for line in notes:
        print(f"{YELLOW}- {line}{RESET}")
    input(f"{CYAN}Press Enter to go back...{RESET}")


def ask(prompt=""):
    while True:
        answer = input(prompt)
        if answer.strip().lower() in ("n", "notes", "notebook"):
            show_notes()
            continue
        return answer


def open_chest_1():
    os.system("clear")
    print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
    print(f"{RED}|{RESET}                                     47{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {GREEN}*{RESET}                      {RED}|{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|           {RESET}  {BLUE}#{RESET}                       {RED} |{RESET}")
    print(f"{RED}| {RESET}                                    33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print(f"{CYAN}{BOLD}=== CHEST 1: WORDLE ==={RESET} 🔤")
    print(f"Guess the secret {YELLOW}6-letter word{RESET} in {YELLOW}6 tries{RESET}!")
    print(f"{GREEN}Green{RESET} = right spot  {YELLOW}Yellow{RESET} = wrong spot  {GRAY}Gray{RESET} = not in word")
    print(f"{MAGENTA}Solve it to unlock the chest code!{RESET} 🔑")
    input("Press Enter to play the puzzle....")
    if wordle_game():
        notes.append("Chest 1 bonus hint: Num is alpha, alpha is num.")
    input("\nPress Enter to continue...")
    os.system("clear")

    print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {GREEN}*{RESET}                    {RED}  |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                        |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    code = input("Enter the code to open the chest: ").strip()
    while code != "B@D!":
        print("Incorrect code. Please try again.")
        code = input("Enter the code to open the chest: ").strip()
    print("You opened the first chest.")
    print("Clue: The correct door has a 4 in its number.")
    notes.append("Chest 1 clue: the correct door has a 4 in its number.")
    input("Press Enter to continue...")


def open_chest_2():
    os.system("clear")
    print(f"{RED} ----------------{RESET}79{RED}---------------------")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {GREEN}*{RESET}{RED}                      |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print(f"{RED}{BOLD}=== CHEST 2: REACTOR CORE ==={RESET} ⚡")
    print(f"Make all {YELLOW}25 nodes{RESET} {GREEN}stable (energy 1-5){RESET} in {YELLOW}35 moves{RESET}!")
    print(f"Type a node like {CYAN}A1{RESET} to add 1 energy. At 10 it {RED}overloads{RESET} and")
    print(f"spills 1 to neighbours: {YELLOW}T{RESET} = up/down/left/right, {YELLOW}E{RESET} = diagonals.")
    print(f"{MAGENTA}Type HINT for help, QUIT to leave.{RESET}")
    input("Press Enter to play the puzzle....")
    if reactor_puzzle():
        notes.append("Chest 2 bonus hint: Use alphabet positions (A=1, B=2 ... Z=26).")
    input("\nPress Enter to continue...")
    os.system("clear")
    print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {GREEN}*{RESET}{RED}                      |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")

    code = input("Enter the code to open the chest: ").strip()
    while code != "A_J4":
        print("Incorrect code. Please try again.")
        code = input("Enter the code to open the chest: ").strip()
    print("You opened the second chest.")
    print("Clue: The correct door has a 7 in its number.")
    notes.append("Chest 2 clue: the correct door has a 7 in its number.")
    input("Press Enter to continue...")


def main():
    check_terminal_size()

    os.system("clear")
    print("WELCOME TO THE ESCAPE-ROOM GAME")
    print(
        "You are trapped in a room and you have to escape it by solving puzzles to open each chest. Each chest contain a clue for the escape.")
    print(
        "You are inside one room with two chests and several doors. You can only enter one and only one door leads you to freedom")
    print("To find which door to go to, open each chest to find some clues.")
    print("* represents the player. - represents walls. number represents door number # represents chests")
    input("Press Enter to start the game...")

    show_storyline()

    os.system("clear")
    print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                     {RED}   |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                  {RESET} {GREEN}*{RESET}{RED}  |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {RED}                       |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print("Enter your command number to move the player.")
    print("Commands: 1. go near chest 1, 2. go near chest 2, N. clue notebook")
    command = ask()
    command = command.lower().strip()

    while command != "1" and command != "2":
        os.system("clear")
        print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
        print(f"{RED}|{RESET}                                     47")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
        print(f"98{RED}                                     |{RESET}")
        print(f"{RED}|                                  {RESET} {GREEN}*{RESET}{RED}  |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|{RESET}             {BLUE}#{RESET} {RED}                       |{RESET}")
        print(f"{RED}|{RESET}                                     33")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
        print("Invalid command. Please enter a valid command.")
        command = ask("Enter your command: ")
        command = command.lower().strip()

    if command == "1":
        open_chest_1()
        flag = 1
    elif command == "2":
        open_chest_2()
        flag = 2

    print("Now open the other chest to find the other clues.")
    os.system("clear")
    print(f"{RED} ----------------{RESET}79{RED}---------------------")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                  {RESET} {GREEN}*{RESET}{RED}  |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {RED}                       |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print("Commands: 1. go near chest 1, 2. go near chest 2, N. clue notebook")
    command = ask("Enter your command number: ")
    command = command.lower().strip()

    while (command != "1" or flag != 2) and (command != "2" or flag != 1):
        os.system("clear")
        print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
        print(f"{RED}|{RESET}                                     47")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
        print(f"98{RED}                                     |{RESET}")
        print(f"{RED}|                                  {RESET} {GREEN}*{RESET}{RED}  |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|{RESET}             {BLUE}#{RESET} {RED}                       |{RESET}")
        print(f"{RED}|{RESET}                                     33")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
        if (command == "1" and flag == 1) or (command == "2" and flag == 2):
            print("You have already opened this chest. Move closer to the other chest to open it.")
        else:
            print("Invalid command. Please enter a valid command.")
        command = ask("Enter your command: ")
        command = command.lower().strip()

    if command == "1" and flag == 2:
        open_chest_1()
    elif command == "2" and flag == 1:
        open_chest_2()

    os.system("clear")
    print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                  {RESET} {GREEN}*{RESET}{RED}  |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {RED}                       |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print("The clues you found are:")
    print("- The correct door has a 4 in its number.")
    print("- The correct door has a 7 in its number.")
    command = ask(
        "Now that you have opened both chests, enter the door number you want to go through (N = notebook): ").strip()
    while command != "47" and command != "33" and command != "16" and command != "54" and command != "98" and command != "79":
        print("Invalid door number. Please enter a valid door number.")
        command = ask("Enter the door number you want to go through: ").strip()
    if command != "47":
        print("Incorrect door number, you fell into fire. Game Over. Run the game again to try and escape the room.")
        sys.exit(0)

    os.system("clear")
    print("Congratulations! You have escaped one of the rooms. ")
    print(
        "You enter another room and find one more chest. You can open this chest too by the code received after solving another puzzle.")
    print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
    print(
        f"{RED}|                                       __   {RESET}{GREEN}*{RESET} {RED}                            |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(
        f"{RED}|             {BLUE}#{RESET}                        {RED}|  |                         {BLUE}#{RESET}     {RED} |{RESET}")
    print(f"98                                  {RED}   |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(
        f"{RED}|                                      |  |      {RESET} {CYAN}___________________{RESET}{RED}      |{RESET}")
    print(
        f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |   ------{RESET}{CYAN}[VICTORY DOOR:LOCKED]{RESET}{RED}------{RESET}")
    print(f"{RED}|      {RESET}                               33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print("Enter your command number to move the player.")
    print("Commands: 1. go near chest 3, N. clue notebook")
    command = ask()
    command = command.lower().strip()
    while command != "1":
        os.system("clear")
        print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
        print(
            f"{RED}|                                       __   {RESET}{GREEN}*{RESET} {RED}                            |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(
            f"{RED}|             {BLUE}#{RESET}                        {RED}|  |                         {BLUE}#{RESET}     {RED} |{RESET}")
        print(f"98                                  {RED}   |  |                                |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(
            f"{RED}|                                      |  |      {RESET} {CYAN}___________________{RESET}{RED}      |{RESET}")
        print(
            f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |   ------{RESET}{CYAN}[VICTORY DOOR:LOCKED]{RESET}{RED}------{RESET}")
        print(f"{RED}|      {RESET}                               33")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
        print("Invalid command. Please enter a valid command.")
        command = ask("Enter your command: ")
        command = command.lower().strip()

    os.system("clear")
    print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
    print(f"{RED}|                                       __   {RESET}  {RED}                            |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(
        f"{RED}|             {BLUE}#{RESET}                        {RED}|  |                    {GREEN}*{RESET}  {BLUE}#{RESET}       {RED} |{RESET}")
    print(f"98                                  {RED}   |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(
        f"{RED}|                                      |  |      {RESET}{CYAN} ___________________{RESET}{RED}      |{RESET}")
    print(
        f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |   ------{RESET}{CYAN}[VICTORY DOOR:LOCKED]{RESET}{RED}------{RESET}")
    print(f"{RED}|      {RESET}                               33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print(f"{MAGENTA}{BOLD}=== CHEST 3: LABYRINTH ==={RESET} 🧭")
    print(f"Move with {CYAN}W A S D{RESET} (then Enter). Grab the {YELLOW}K{RESET}, then reach the {CYAN}X{RESET}.")
    print(f"Dodge the {RED}E{RESET}, it chases you! {MAGENTA}Escape to get the code.{RESET} 🔑")
    input("Press Enter to play the puzzle....")
    if maze_game():
        notes.append("Chest 3 bonus hint: The letter stays, only the number changes.")
    input("\nPress Enter to continue...")
    os.system("clear")
    print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
    print(f"{RED}|                                       __   {RESET}  {RED}                            |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(
        f"{RED}|             {BLUE}#{RESET}                        {RED}|  |                    {GREEN}*{RESET}  {BLUE}#{RESET}       {RED} |{RESET}")
    print(f"98                                  {RED}   |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(
        f"{RED}|                                      |  |      {RESET}{CYAN} ___________________{RESET}{RED}      |{RESET}")
    print(
        f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |   ------{RESET}{CYAN}[VICTORY DOOR:LOCKED]{RESET}{RED}------{RESET}")
    print(f"{RED}|      {RESET}                               33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")

    code = input("Enter the code to open the chest: ").strip()
    while code != "A0RU":
        print("Incorrect code. Please try again.")
        code = input("Enter the code to open the chest: ").strip()
    print(f"{GREEN}You opened the third chest and found the key for the victory door!{RESET}")
    print(f"The door glows with three codes: {YELLOW}{BOLD}[E19]  [C1]  [P5]{RESET}")
    notes.append("Victory door codes: E19, C1, P5. Decode them to get the secret word.")
    print(f"{MAGENTA}Decode them and type the secret word to open the door.{RESET}")
    command = ask("Secret word (N = notebook): ").strip().upper()
    while command != "ESCAPE":
        os.system("clear")
        print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
        print(f"{RED}|                                       __   {RESET}  {RED}                            |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(
            f"{RED}|             {BLUE}#{RESET}                        {RED}|  |                         {BLUE}#{RESET}          |{RESET}")
        print(f"98                                  {RED}   |  |                                |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(
            f"{RED}|                                      |  |      {RESET}{CYAN} ___________________{RESET}{RED}      |{RESET}")
        print(
            f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |  ------{RESET}{CYAN}[VICTORY DOOR:LOCKED]{RESET}{RED}------{RESET}")
        print(f"{RED}|      {RESET}                               33{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
        print(f"{RED}Wrong word, the door stays locked.{RESET}")
        print(f"The door codes: {YELLOW}{BOLD}[E19]  [C1]  [P5]{RESET}")
        command = ask("Secret word (N = notebook): ").strip().upper()

    os.system("clear")
    print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
    print(f"{RED}|                                       __   {RESET}  {RED}                            |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(
        f"{RED}|             {BLUE}#{RESET}                        {RED}|  |                          {BLUE}#{RESET}      |{RESET}")
    print(f"98                                  {RED}   |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(
        f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |   -----{RESET}{YELLOW}[VICTORY DOOR:UNLOCKED]{RESET}{RED}-----{RESET}")
    print(f"{RED}|      {RESET}                               33                  {GREEN}*{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")

    rainbow = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    W = 60
    time.sleep(1.5)
    os.system("clear")

    def star_line(shift):
        return "".join(f"{rainbow[(j + shift) % 6]}{BOLD}*{RESET}" for j in range(W))

    print(star_line(0))
    print()
    trophy = [
        "     ___________      ",
        "    '._==_==_=_.'     ",
        "    .-\\:      /-.    ",
        "   | (|:.     |) |    ",
        "    '-|:.     |-'     ",
        "      \\::.    /       ",
        "       '::. .'        ",
        "         ) (          ",
        "       _.' '._        ",
        "      '-------'       ",
    ]
    for i, line in enumerate(trophy):
        print(f"{rainbow[i % 6]}{BOLD}{line.center(W)}{RESET}")
        time.sleep(0.12)
    print()
    msg = "YOU ESCAPED! YOU WIN!"
    print(f"{GREEN}{BOLD}{'=' * W}{RESET}")
    print("".join(f"{rainbow[i % 6]}{BOLD}{c}{RESET}" for i, c in enumerate(msg.center(W))))
    print(f"{GREEN}{BOLD}{'=' * W}{RESET}")
    print()
    print(f"{YELLOW}{BOLD}{'All 3 chests opened. Victory door unlocked.'.center(W)}{RESET}")
    print(f"{CYAN}{BOLD}{'Congratulations, champion!'.center(W)}{RESET}")
    print()
    print(star_line(3))


if __name__ == "__main__":
    main()