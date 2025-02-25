import argparse


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


class Arguments:
    def __init__(self):

        help_map=[
        "Required URL",
        "• Option -r : recursively downloads the images in a URL received as a parameter.",
        "• Option -r -l [N] : indicates the maximum depth level of the recursive download. If not indicated, it will be 5.",
        "• Option -p [PATH] : indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used."
        ]

        parser = argparse.ArgumentParser()

        parser.add_argument("url", type=str, nargs=1, help=help_map[0])
        parser.add_argument("-r", action="store_true", help=help_map[1])
        parser.add_argument("-l", type=int, nargs="?", default=5, help=help_map[2])
        parser.add_argument("-p", type=str, nargs="?", default="./data/", help=help_map[3])

        args = parser.parse_args()

        self.url = args.url[0]
        self.recursive = args.r
        self.max_depth = args.l
        self.path = args.p

    def __str__(self):
        pattern = "*" * 15
        s = "\n" + bcolors.HEADER
        s += pattern + " ARGUMENT " + pattern
        s += bcolors.ENDC + "\n"
        s += f"URL : {self.url}\n"
        s += f"Recursive : {self.recursive}\n"
        s += f"Depth : {self.max_depth}\n"
        s += f"Path : {self.path}\n"
        s += bcolors.HEADER
        s += pattern + "**********" + pattern
        s += bcolors.ENDC + "\n"
        return s


def _print_header(color, text):
    print(color + "*" * 45)
    w = 45 - len(text) - 2
    w = w // 2
    if w % 2:
        w -= 1
        text += " "
    print("*" + (" " * w) + text + (" " * w) + "*")
    print(color + "*" * 45)


def cc(s, ed=""):
    print(s, end=ed)
