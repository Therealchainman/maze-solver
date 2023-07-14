from enum import IntFlag, auto

class Border(IntFlag):
	EMPTY = 0
	NORTH = auto()
	SOUTH = auto()
	EAST = auto()
	WEST = auto()

	@property
	def corner(self):
		return self in (
			self.NORTH | self.EAST,
			self.NORTH | self.WEST,
			self.SOUTH | self.EAST,
			self.SOUTH | self.WEST
		)

	@property
	def dead_end(self):
		return self.bit_count() == 3

	@property
	def intersection(self):
		return self.bit_count() < 2