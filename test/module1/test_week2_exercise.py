import unittest

from src.module1.week2.exercise1 import max_kernel
from src.module1.week2.exercise2 import character_count
from src.module1.week2.exercise3 import count_word
from src.module1.week2.exercise4 import levenshtein_distance


class TestWeek2(unittest.TestCase):
	def test_get_max_numb_list(self):
		num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
		self.assertEqual(max_kernel(num_list, 3), [5, 5, 5, 5, 10, 12, 33, 33])  # add assertion here
		self.assertEqual(max_kernel([], 1), [])  # add assertion here
		self.assertEqual(max_kernel(num_list, 0), [])  # add assertion here

	def test_count_char(self):
		string = 'Happiness'
		result = {'H': 1, 'a': 1, 'i': 1, 'n': 1, 'e': 1, 'p': 2, 's': 2}
		self.assertEqual(character_count(string), result)
		string = 'Happines0'
		self.assertEqual(character_count(string), dict())

	def test_count_word(self):
		file_path = 'data/module1/week2/P1_data.txt'

		result = {'conquers': 1, 'himself': 1, 'mightiest': 1, 'warrior': 1, 'not': 1, 'but': 1, 'rather': 1,
		          'value': 1,
		          'courage': 1, 'makes': 1, 'majority': 1, 'secret': 1, 'be': 1, 'ready': 1, 'opportunity': 1,
		          'profit': 1,
		          'from': 1, 'mistakes': 1, 'and': 1, 'try': 1, 'again': 1, 'different': 1, 'way': 1, 'lay': 1,
		          'firm': 1,
		          'foundation': 1, 'bricks': 1, 'others': 1, 'have': 1, 'thrown': 1, 'at': 1, 'him': 1, 'usually': 1,
		          'those': 1, 'are': 1, 'too': 1, 'busy': 1, 'looking': 1, 'cannot': 1, 'solve': 1, 'problems': 1,
		          'kind': 1, 'thinking': 1, 'employed': 1, 'came': 1, 'up': 1, 'them': 1, 'small': 1, 'positive': 1,
		          'thought': 1, 'morning': 1, 'change': 1, 'your': 1, 'whole': 1, 'day': 1, 'everything': 1, 'if': 1,
		          'just': 1, 'help': 1, 'enough': 1, 'other': 1, 'people': 1, 'what': 1, 'they': 1, 'become': 2,
		          'success': 2, 'life': 2, 'his': 2, 'when': 2, 'it': 2, 'comes': 2, 'successful': 2, 'will': 2,
		          'one': 2,
		          'we': 2, 'get': 2, 'you': 2, 'want': 2, 'who': 3, 'is': 3, 'to': 3, 'for': 3, 'can': 3, 'the': 4,
		          'of': 4,
		          'with': 4, 'in': 4, 'a': 6, 'man': 6}
		self.assertEqual(count_word(file_path), result)
		file_path = 'P2_data_1.txt'
		self.assertEqual(count_word(file_path), dict())

	def test_levenshtein_distance(self):
		# Ví dụ sử dụng
		s = "kitten"
		t = "sitting"
		self.assertEqual(levenshtein_distance(s, t), 3)


if __name__ == '__main__':
	unittest.main()
