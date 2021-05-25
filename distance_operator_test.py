import unittest
from distance_operator import DistanceOperator

class DBConnectionTest(unittest.TestCase):
	def test_distance_operation(self):
		p1 = (37.5090436,126.9612882) # heukseok station

		a = (37.505859375, 126.9544677734375) # 스시초이
		b = (37.5083285, 126.9594252) # 장독대
		c = (37.50765609741211, 126.95704650878906) # 하꼬멘

		# 흑석역으로부터 스시초이가 장독대보다 멀다.
		assert(DistanceOperator.calculate_distance(p1[0], p1[1], a[0], a[1]) > DistanceOperator.calculate_distance(p1[0], p1[1], b[0], b[1]))


if __name__ == '__main__':
    unittest.main()