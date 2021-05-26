import math

class DistanceOperator:
	@staticmethod
	def calculate_position(rx, ry, cx, cy):
		return math.sqrt((rx-cx)**2+(ry-cy)**2)