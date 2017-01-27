from itertools import combinations
class sum_zero:
	def __init__(self):
		self.final=[]
	def compute(self,nums):
		self.nums=nums
		for comb in combinations(self.nums,3):
			if sum(comb) == 0:
				self.final.append(list(comb))
		return self.final
sz=sum_zero()
l=([int(a) for a in input('Enter values: ').split()])
print(sz.compute(l))