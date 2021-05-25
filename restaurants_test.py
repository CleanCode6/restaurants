import unittest
from model.restaurants import Parser, Restaurants

class RestaurantTest(unittest.TestCase):
	def test_convert_of_restaurant(self):
		sample = {'restaurant_id': 1, 'description': '중앙대학교 중문에 위치해 있습니다. 중앙대학교 중문에 위치해 있습니다.', 'rating': 4.1, 'menu': '[{"price": 10000, "menu_name": "찹스테이크 덮밥"}, {"price": 5000, "menu_name": "치즈고로케"}, {"price": 5000, "menu_name": "새우튀김"}]', 'restaurant_name': '스시초이', 'category': 3, 'image': None, 'position_x': 37.505859375, 'position_y': 126.9544677734375, 'address': '서울 동작구 흑석로6길 18'}
		list_sample = [sample]
		print(Parser.to_obj(sample))
		print(Parser.to_list(list_sample))

if __name__ == '__main__':
    unittest.main()