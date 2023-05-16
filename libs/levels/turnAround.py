from libs.levels.placeholder import placeholder
from libs.base.core import Stage, Option


__story = """
A Grimy voice came behind it sounds like its coming from the telephone.
"Dad, what's that outside the window?" the voice says.
"That son, is our G..Aaxzzst" the voice cut off suddenly
Everything turns dark.
"""

__options = [
    Option("Yell out in anger.", placeholder),
    Option("Look at the telephone and the window.", placeholder),
    Option("Run back to the room you came out from.", placeholder),
    Option("Run towards the door at the end of the corridor.", placeholder),
]

callThePolice = Stage(__story, __options)


