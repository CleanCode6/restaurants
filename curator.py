from distance_operator import DistanceOperator
from functools import cmp_to_key

def is_item_not_defined(_dict, field):
	return (_dict.get(field) is None) or (_dict[field] == '-1')

class Curator:
	@staticmethod
	def curate_restaurant(restaurants, condition):
		curated = []
		# Check condition of category
		for rest in restaurants:
			if rest.score >= 4.0:
				if is_item_not_defined(condition, "category"):
					curated.append(rest)
				elif str(rest.category) == condition["category"]:
					curated.append(rest)

		position_map = {
			'0': (37.5066244,126.9524722),
			'1': (37.5066412,126.9524722),
			'2': (37.4995973,126.9372955),
			'3': (37.5090436,126.9612882)
		}

		if not is_item_not_defined(condition, "pos_x") and not is_item_not_defined(condition, "pos_y"):
			position_map['4'] = (float(condition["pos_x"]), float(condition["pos_y"]))

		if is_item_not_defined(condition, "pos"):
			position = '0'
		else:
			position = condition["pos"]
		start_x = position_map[position][0]
		start_y = position_map[position][1]

		def comparing_dist(a, b):
			a_dt = DistanceOperator.calculate_position(a.position_x, a.position_y, start_x, start_y)
			b_dt = DistanceOperator.calculate_position(b.position_x, b.position_y, start_x, start_y)
			return a_dt - b_dt

		# sort oredering
		if not is_item_not_defined(condition, "order"):
			if condition["order"] == '0':
				curated.sort(key=lambda rest: rest.score, reverse=True)
			elif condition["order"] == '1':
				curated.sort(key=cmp_to_key(comparing_dist))

		return curated
