from libs.levels.placeholder import placeholder
from libs.levels.callThePolice import callThePolice
from libs.base.core import Option, Stage


__story = """
You walk down the corridor, you look around the wall, there is a family photo of 4, parents son and daughter, classic.
They look happy, but you can't shake off the weird feeling you have. There is also a clock on the wall showing
2 AM, but the clock seem to be broken, the needle doesnt move. You arrived in front of the window, you noticed there is
a telephone on a table near the window to the left. To the right of you is a turn to a hallway with a couple of doors lining up,
one next to the turn and the other is at the end of the hallway.
"""

__options = [
    Option("Try opening the window.", placeholder),
    Option("Walk to the door next to the turn.", placeholder),
    Option("Walk to the door at the end of the hallway.", placeholder),
    Option("Try using the phone to call the police.", callThePolice),
]

walkDownCorridor = Stage(__story, __options)