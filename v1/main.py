cells = []
buffer = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
import sys
silent = False
try:
	if sys.argv[1] == "-s":
		silent=True
except Exception as e:
	pass
with open("file.frw", "r") as file:
	data = file.read()
	line_num = 1
	for line in data.split('\n'):
		if line[:1] == "(":
			for i in range(int(line[1:-1], base=16)):
				cells.append('`')
			# break
		elif line[:1] == "~":
			p1 = line.split('[')[1].strip()
			loc = line.split('[')[0].strip()
			loc = int(loc[3:], base=16)
			if "'" in p1:
				p2 = str(p1)[1:]
				cells[loc] = p2
			else:
				if line[-1] == "h":
					p2 = int(p1[:len(p1)-1], base=16)
					cells[loc] = p2
				elif p1[-1] == "d":
					p2 = int(p1[:len(p1)-1], base=10)
					cells[loc] = p2

		elif line[:1] == "&":
			loc = int(line[1:], base=16)
			if cells[loc] == "`" and silent==False:
				print("\nwarning, the address requested is empty, printing cell padding. This may not be the desired output. Please tweak pointer at " + str(line_num) + ".")
				print("To suppress such warnings, use -s (Silent) flag while running.\n")
			print(cells[loc])

		line_num +=1