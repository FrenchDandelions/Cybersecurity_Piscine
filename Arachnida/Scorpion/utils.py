import argparse


class Arguments:
    def __init__(self):

        help_map=[
        "one image path at least",
        ]

        parser = argparse.ArgumentParser()

        parser.add_argument("image", type=str, nargs='+', help=help_map[0])

        args = parser.parse_args()

        self.image = args.image

    def __str__(self):
        pattern = "*" * 15
        s = "\n" + bcolors.HEADER
        s += pattern + " ARGUMENT " + pattern
        s += bcolors.ENDC + "\n"
        for n, image in enumerate(self.image):
            s += f'Image {n} : {image}\n'
        s += bcolors.HEADER
        s += pattern + "**********" + pattern
        s += bcolors.ENDC + "\n"
        return s


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


def cc(s, ed=""):
    print(s, end=ed)