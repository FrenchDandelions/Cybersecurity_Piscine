import argparse


class Argument():
    def __init__(self):

        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required=True)

        group.add_argument("-g", action="store_true")
        group.add_argument("-k", action="store_true")
        parser.add_argument("file", type=str)

        args = parser.parse_args()

        # True if we have to create new password, False if
        # we have to create a new key
        self.mode = True if args.k else False
        self.file = args.file
        # print(args)
        # print(args.g, args.k)
        pass
