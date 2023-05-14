from libs.levels.placeholder import placeholder
from libs.base.core import Stage, Option


__story = """
You picked the telephone up and proceed to dial 911.
...
..
.

Nobody answers. You lift the dial and look around to realize the cable is cut off.
The phone is broken. You feel a bit anxious and desperate "Crap.." you say to yourself.
You place the telephone back on the table then when you're just about to leave.
"""

__options = [
    Option("Turn around.", placeholder)
]

callThePolice = Stage(__story, __options)