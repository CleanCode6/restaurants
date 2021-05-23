
class Curator:
	@staticmethod
	def curate_restaurant(restaurants, condition):
		curated = []
		# Check condition of category
		for rest in restaurants:
			if rest["rating"] >= 4.0:
				curated.append(rest)
		return curated
