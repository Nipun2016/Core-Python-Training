from itertools import combinations
class Sumzero:
	def __init__(self):
		self.lst = [float(a) for a in input('Enter real numbers: ').split()]
	def compute_Sum(self):
		ans = []
		for c in combinations(self.lst,3):
			if sum(c) == 0:
				ans.append(list(c))
		print(ans)
s = Sumzero()
s.compute_Sum()
