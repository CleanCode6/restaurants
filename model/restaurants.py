from dataclasses import dataclass

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
	menu: str = ""
	address: dict = ""