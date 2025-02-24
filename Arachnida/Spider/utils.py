import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def cc(s, ed=""):
    print(s, end=ed)

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
        s = bcolors.HEADER
        s += pattern + " ARGUMENT " + pattern
        s += bcolors.ENDC + "\n"
        s += f"URL : {self.url}\n"
        s += f"Recursive : {self.recursive}\n"
        s += f"Depth : {self.max_depth}\n"
        s += f"Path : {self.path}"
        return s


def _print_dict(dic):
    for key, val in dic.items():
        print(key, val, sep=" : ")
