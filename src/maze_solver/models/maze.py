from maze_solver.models.square import Square
from maze_solver.models.role import Role
from dataclasses import dataclass
from functools import cached_property
from itertools import product

@dataclass(frozen = True)
class Maze():
	squares: tuple[Square, ...]

	def post_init(self):
		validate_indices(self)
		validate_rows_columns(self)
		validate_entrance(self)
		validate_exit(self)

	# makes maze subscriptable and iterable by squares
	def __iter__(self):
		return iter(self.squares)

	def __getitem__(self, index):
		return self.squares[index]
	
	def __len__(self):
		return len(self.squares)

	@cached_property
	def height(self):
		return max(square.row for square in self.squares)

	@cached_property
	def width(self):
		return max(square.column for square in self.squares)
	
	@cached_property
	def entrance(self):
		return next(square for square in self.squares if square.role == Role.ENTRANCE)
	
	@cached_property
	def exit(self):
		return next(square for square in self.squares if square.role == Role.EXIT)
	
def validate_indices(maze):
	assert (
		[square.index for square in maze] == list(range(len(maze))),
		'Indices are not sequential'
	)

def validate_rows_columns(maze):
	for r, c in product(range(maze.height), range(maze.width)):
		square = maze[r * maze.width + c)
		assert square.row == r, "wrong square.row"
		assert square.column == c, "wrong square.column"

def validate_entrance(maze):
	assert (
		sum(square.role == Role.ENTRANCE for square in maze) == 1,
		'Incorrect number of entrances'
	)
	
def validate_exit(maze):
	assert (
		sum(square.role == Role.EXIT for square in maze) == 1,
		'Incorrect number of exits'
	)

