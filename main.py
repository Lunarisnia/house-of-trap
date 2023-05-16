from libs.base.core import Game
from libs.levels.awakening import awakening
newGame = Game(awakening)

try:
    newGame.start()
except KeyboardInterrupt:
    print("\nYou sit down and rest, slowly you fell asleep...")