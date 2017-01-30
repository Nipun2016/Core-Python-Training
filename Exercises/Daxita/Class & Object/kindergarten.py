class kindergarten:
	def __init__(self):
	    diagram = "VRCGVVRVCGGCCGVRGCVCGCGV VRCCCGCRRGVCGCRVVCVGCGCV"
	    self.p = {"G": "Grass","C": "Clover","R": "Radishes","V": "Violets",}
	    students=("Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry").split()
	    self.rows = [list(row) for row in diagram.split()]
	    self.plant_rows = [[self.p[c] for c in row] for row in self.rows]
	    self.students = sorted(students)

	def plants(self, name):
	    return self.plants_for_index(self.students.index(name))

	def plants_for_index(self, k):
	    return (self.plant_rows[0][k * 2],
	            self.plant_rows[0][k * 2 + 1],
	            self.plant_rows[1][k * 2],
	            self.plant_rows[1][k * 2 + 1])
if __name__=="__main__":
	try:
		k=kindergarten()
		name=input("\nAlice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry\nEnter name from above list of Students:")
		print(k.plants(name))
	except ValueError:
		print("Enter Valid Input")