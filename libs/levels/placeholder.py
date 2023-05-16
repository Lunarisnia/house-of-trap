from libs.base.core import Stage

class __placeholder(Stage):
    def play(self) -> None:
        print("Please implement this action.")
        exit(0)

placeholder = __placeholder("", [])