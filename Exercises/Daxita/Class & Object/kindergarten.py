class kindergarten:
	stu=("Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry").split()
	p = {"G": "Grass","C": "Clover","R": "Radishes","V": "Violets",}
	p1="VRCGVVRVCGGCCGVRGCVCGCGV VRCCCGCRRGVCGCRVVCVGCGCV"
	def __init__(self, diagram=p1, students=stu):
	    self.diagram = diagram
	    self.rows = [list(row) for row in diagram.split()]
	    self.plant_rows = [[self.p[c] for c in row] for row in self.rows]
	    self.students = sorted(students)

	def plants(self, name):
	    return self.plants_for_index(self.students.index(name))

	def plants_for_index(self, k):
	    print (self.plant_rows[0][k * 2],
	            self.plant_rows[0][k * 2 + 1],
	            self.plant_rows[1][k * 2],
	            self.plant_rows[1][k * 2 + 1])

k=kindergarten()
k.plants(input("\nAlice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry\nEnter name from above list of Students:"))