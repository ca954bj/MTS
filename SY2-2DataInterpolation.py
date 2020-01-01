data = open("New1222g.txt", 'r')
disp = []
load = []
for line in data:
	content = line.split()
	disp.append(float(content[0]))
	load.append(float(content[1]))

length = len(disp)
intercept = []

for i in range(1, length - 1):
	diffl = disp[i] - disp[i-1]
	diffr = disp[i+1] - disp[i]
	mul = diffl * diffr
	if mul < 0:
		intercept.append(i)
		
print(intercept)
print(len(intercept))
	
data.close()

data2 = open("New1222g2.txt", 'r')
disp2 = []
for line in data2:
	content = line.split()
	disp2.append(float(content[0]))

length2 = len(disp2)
intercept2 = []
print("length2 = %d" % length2)

for i in range(1, length2 - 1):
	diffl = disp2[i] - disp2[i-1]
	diffr = disp2[i+1] - disp2[i]
	mul = diffl * diffr
	if mul < 0:
		intercept2.append(i)
		
print(intercept2)
print(len(intercept2))

execfile("/media/chenting/Work/ProgramCode/Tools/Interpolation.py")

result = []

for i in range(0, len(intercept)):
	if i == 0:
		lower1 = 0
		upper1 = intercept[0]
		lower2 = 0
		upper2 = intercept2[0]
	else:
		lower1 = intercept[i - 1]
		upper1 = intercept[i]
		lower2 = intercept2[i - 1]
		upper2 = intercept2[i]
		
	result += List2ListLinearInterpolation2D(disp[lower1:upper1], load[lower1:upper1], disp2[lower2:upper2], tol=0.01)
	
print(result)
fn = open("SY2-2Interp.txt", 'w')
for obj in result:
	fn.write("%s\n"%obj)
	
	
	
	
	
	
	
	
	
