execfile("//media/chenting/Work/ProgramCode/Tools/PolygonArea.py")

fn = "SX1P.txt"
content = open(fn)

coo = []
for line in content:
	sp = line.split(',')
	coo.append([float(sp[0]), float(sp[1])])
	
print(coo)

AP = PolygonArea([0, 0], coo)/1000
print(AP)
