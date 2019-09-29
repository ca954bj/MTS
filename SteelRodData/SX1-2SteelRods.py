execfile("/media/chenting/Work/ProgramCode/Tools/Interpolation.py")
execfile("/media/chenting/Work/ProgramCode/Tools/ExcelTools.py")

filelocation = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1210.txt"

fn = open(filelocation, 'r')

disp = []
moment = []

for line in fn:
	numbers = line.split()
	if len(numbers) > 0:
		load1 = float(numbers[0])
		disp1 = float(numbers[1])
		load2 = float(numbers[2])
		disp2 = float(numbers[3])
		if abs(disp1) > 39:
			break
		disp.append(0.5 * (disp1 - disp2))
		moment.append(4.66 * (load1 - load2))

Copied = "0	4.37	8.74	4.37	-4.37	-8.74	-4.37	0	4.37	8.74	4.37	0	-4.37	-8.74	-4.37	0	4.37	8.74	4.37	0	-4.37	-8.74	-4.37	0	5.83	11.65	5.83	0	-5.83	-11.65	-5.83	0	5.83	11.65	5.83	0	-5.83	-11.65	-5.83	0	5.83	11.65	5.83	0	-5.83	-11.65	-5.83	0	5.83	11.65	17.48	11.65	5.83	0	-5.83	-11.65	-17.48	-11.65	-5.83	0	5.83	11.65	17.48	11.65	5.83	0	-5.83	-11.65	-17.48	-11.65	-5.83	0	5.83	11.65	17.48	11.65	5.83	0	-5.83	-11.65	-17.48	-11.65	-5.83	0	7.77	15.53	23.3	15.53	7.77	0	-7.77	-15.53	-23.3	-15.53	-7.77	0	7.77	15.53	23.3	15.53	7.77	0	-7.77	-15.53	-23.3	-15.53	-7.77	0	7.77	15.53	23.3	15.53	7.77	0	-7.77	-15.53	-23.3	-15.53	-7.77	0	11.65	23.3	29.13	34.95	23.3	11.65	0	-11.65	-23.3	-29.13	-34.95	-23.3	-11.65	0	11.6	23.3	29.13	34.95	23.3	11.65	0	-11.65	-23.3	-29.13	-34.95	-23.3	-11.65	0"

ST = []
NumberList(Copied, ST)

turning = [0]
STturning = [0]

for i in range(1, len(disp)-1):
	if (disp[i] - disp[i-1])*(disp[i+1] - disp[i]) <= 0:	
		turning.append(i)
		
for i in range(1, len(ST)-1):
	if (ST[i] - ST[i-1])*(ST[i+1] - ST[i]) <= 0:	
		STturning.append(i)

resultmoment = []
resultset = []
for i in range(1, len(turning)):
	index1 = turning[i] + 1
	index0 = turning[i - 1]
	STindex1 = STturning[i] + 1
	STindex0 = STturning[i - 1]
	print(index0, index1, STindex0, STindex1)
	dispdata = disp[index0:index1]
	momentdata = moment[index0:index1]
	STdata = ST[STindex0:STindex1]
	result = List2ListLinearInterpolation2D(dispdata, momentdata, STdata)
	resultset.append(result)
	
result = List2ListLinearInterpolation2D(disp[turning[-1]:], moment[turning[-1]:], ST[STturning[-1]:])
resultset.append(result)
	
for i, obj in enumerate(resultset):
	if i == 0:
		resultmoment += obj[0:-1]
		last = obj[-1]
	elif i == len(resultset) - 1:
		resultmoment.append(last)
		resultmoment += obj[1:]
	else:
		first = obj[0]
		thefirst = 0.5*(first + last)
		resultmoment.append(thefirst)
		resultmoment += obj[1:-1]
		last = obj[-1]

print(len(resultmoment))
print(len(ST))
print(disp[0:30])
print(moment[0:30])
print(resultmoment)
