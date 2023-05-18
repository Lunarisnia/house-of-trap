from libs.levels.placeholder import placeholder
from libs.levels.checkWhiteDoor import checkWhiteDoor
from libs.base.core import Option, Stage


__story = """
You woke up in a strange dimly lit room you don't remember anything that happened a few days back your last memory are
going to a cafe to meet someone. Meet who? you don't remember. You take a look around yourself, you can barely see anything 
that is not lit by the ceiling light, you took a glance around and there is a door!
a single white door with light shining over it as if guiding you.
"""

__options = [
    Option("Check the door.", checkWhiteDoor),
    Option("Check your pocket for your phone.", placeholder),
    Option("Take a look around the room closely.", placeholder),
    Option("Yell for help.", placeholder),
]

awakening = Stage(__story, __options)