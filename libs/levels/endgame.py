from libs.base.core import Stage

class __Endgame(Stage):
    def play(self) -> None:
        print("The game has ended!.")
        exit(0)

endgame = __Endgame("", [])