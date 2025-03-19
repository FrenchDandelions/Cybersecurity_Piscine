import os
from utils import Arguments, Extensions


extensions = []

class Stockholm(Arguments, Extensions):
    def __init__(self):
        super().__init__()
        if self.version:
            self.display_version()
        if self.help:
            self.display_help()
        # print(self.extensions)
        
# l = os.listdir("./infection/")
# print(*l, sep="\n")

s = Stockholm()
