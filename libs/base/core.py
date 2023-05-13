class Option:
    def __init__(self, text: str, nextStage) -> None:
        self.text = text
        self.nextStage = nextStage

    def activate(self):
        self.nextStage.play()

class Stage:
    def __init__(self, story: str, options: list[Option]) -> None:
        self.story = story
        self.options = options

    def play(self) -> None:
        self.showStory()
        self.showOption()
        self.askPlayerInput()
        pass

    def showStory(self) -> None:
        print('============================================')
        print(self.story)
        print('============================================')
        print('What would you do?\n')

    def showOption(self) -> None:
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option.text}")

    def askPlayerInput(self) -> None:
        while True:
            playerChoice = 0
            try:
                playerChoice = int(input("Enter the number of your chosen option: ")) - 1
                if (playerChoice >= 0) and (playerChoice < len(self.options)):
                    chosenOption = self.options[playerChoice]
                    chosenOption.activate()
                    return
                print("Invalid Option.")
            except ValueError:
                print("Please enter a proper number you jerk.")
                pass


class Game:
    def __init__(self, startingStage: Stage) -> None:
        self.startingStage = startingStage

    def start(self) -> None:
        self.startingStage.play()