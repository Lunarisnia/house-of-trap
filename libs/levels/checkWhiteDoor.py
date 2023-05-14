from libs.levels.placeholder import placeholder
from libs.base.core import Option, Stage


__story = """
You walk up to the door, took a glance at it and then reached for the handle and twist... It's open!
You open the door and you are greeted with a corridor of a house? The corridor is quite long for a house. directly infront of
you at the end of the corridor is a window to the outside, its all so dark I can't see anything from here. This place looks like a normal house, 
its wooden floor white wall, some artwork, plants, everything feels like... Home. But something is off, where is everyone?
"""

__options = [
    Option("Walk down the corridor.", placeholder),
    Option("Yell for help.", placeholder),
]

checkWhiteDoor = Stage(__story, __options)