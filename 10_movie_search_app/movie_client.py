import requests
import collections

MovieResult = collections.namedtuple(
	'MovieResult',
	'imdb_code, title, director, keywords, duration, genres, rating, year, imdb_score'
)

class MovieClient:
	def __init__(self, search_text):
		if not search_text or not search_text.strip():
			raise ValueError("Please specify a search string.")
		self.search_text = search_text

	def perform_search(self):
		search_url = "https://movieservice.talkpython.fm/api/search/{}".format(
			self.search_text
		)
		response = requests.get(search_url).json()
		data = response["hits"]

		movies = [MovieResult(**m) for m in data]

		return movies
