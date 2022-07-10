from colorama import Fore, Back, Style

def print_garis(length: int, color: Fore = Fore.WHITE) -> None:
    [print("-", end="") if i != length-1 else print("-") for i in range(length)]

def print_white_space(length: int, printlineafter: bool = False) -> None:
    if not printlineafter: [print(" ", end="") for i in range(length)]
    else: [print(" ", end="") if i != length-1 else print(" ") for i in range(length)]

def get_highest(array: list) -> int:
    highest = 0
    for item in array:
        highest = len(item) if len(item) > highest else highest
    return highest