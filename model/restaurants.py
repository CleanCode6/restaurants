from dataclasses import dataclass
import json

@dataclass
class Restaurants:
	restaurant_id: int = 0
	distance: int = 0
	category: int = 0
	restaurant_name: str = ""
	description: str = ""
	rating: float =  0.0
	pricing: str = ""
	image: str = "" # image link
	phone: str = ""
	menu: list[dict] = None
	position_x: float = 0.0
	position_y: float = 0.0
	address: dict = ""

class Parser:
	@staticmethod
	def to_obj(_dict_obj):
		tmp = Restaurants(**_dict_obj)
		tmp.menu = json.loads(tmp.menu)
		return tmp

	@staticmethod
	def to_list(_dict_obj_list):
		return list(map(lambda rest: Restaurants(**rest), _dict_obj_list))
