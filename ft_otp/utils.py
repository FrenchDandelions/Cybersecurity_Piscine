import argparse


class Argument():
    def __init__(self):

        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required=True)

        group.add_argument("-g", action="store_true")
        group.add_argument("-k", action="store_true")
        parser.add_argument("file", type=str)
        parser.add_argument("-v", action="store_true")
        parser.add_argument("-c", action="store_true")

        args = parser.parse_args()

        # True if we have to create new password, False if
        # we have to create a new key
        self.mode = True if args.k else False
        self.file = args.file
        self.verbose = args.v
        self.color = args.c
        # print(args)
        # print(args.g, args.k)
        pass


class bcolors:
    HEADER = '\033[95m'  # Light Magenta
    OKBLUE = '\033[94m'  # Blue
    OKCYAN = '\033[96m'  # Cyan
    OKGREEN = '\033[92m'  # Green
    WARNING = '\033[93m'  # Yellow
    FAIL = '\033[91m'  # Red
    ENDC = '\033[0m'  # Reset
    BOLD = '\033[1m'  # Bold
    UNDERLINE = '\033[4m'  # Underline
    
    # Additional Colors
    BLACK = '\033[30m'  # Black
    RED = '\033[31m'  # Dark Red
    GREEN = '\033[32m'  # Dark Green
    YELLOW = '\033[33m'  # Dark Yellow / Orange
    BLUE = '\033[34m'  # Dark Blue
    MAGENTA = '\033[35m'  # Dark Magenta
    CYAN = '\033[36m'  # Dark Cyan
    WHITE = '\033[37m'  # White
    
    # Bright Versions
    BRIGHT_BLACK = '\033[90m'  # Gray
    BRIGHT_RED = '\033[91m'  # Bright Red
    BRIGHT_GREEN = '\033[92m'  # Bright Green
    BRIGHT_YELLOW = '\033[93m'  # Bright Yellow
    BRIGHT_BLUE = '\033[94m'  # Bright Blue
    BRIGHT_MAGENTA = '\033[95m'  # Bright Magenta
    BRIGHT_CYAN = '\033[96m'  # Bright Cyan
    BRIGHT_WHITE = '\033[97m'  # Bright White


def _change_color(s, ed=""):
    print(s, end=ed)
    
    
def print_header(s):
    print()
    print(s.center(40, "~"))
    print()
    
    
def print_key_value(key, value, color=""):
    _change_color(color)
    print(key, end=" ")
    _change_color(bcolors.ENDC)
    print(value)