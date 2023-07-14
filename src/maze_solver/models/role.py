from enum import IntEnum, auto

# roles given to a square

class Role(IntEnum):
	NONE = 0 # nullable object
	ENTRANCE = auto()
	EXIT = auto()
	WALL = auto()
	EXTERIOR = auto()
	REWARD = auto()
	ENEMY = auto()
