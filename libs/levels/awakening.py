from libs.levels.endgame import endgame
from libs.base.core import Option, Stage


__story = """
You woke up.
"""

__options = [
    Option("Get up.", endgame),
    Option("Goes back to sleep.", endgame),
]

awakening = Stage(__story, __options)