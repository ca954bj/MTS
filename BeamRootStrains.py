inputfileSX1 = "SX1-1FEBeamEndStrainsSelected.txt"
inputfileSY1 = "SY1-1FEBeamEndStrainsSelected.txt"
inputfileSX2 = "SX2-1FEBeamEndStrainsSelected.txt"
inputfileSY2 = "SY2-1FEBeamEndStrainsSelected.txt"

execfile('MTSsetup.py')

DataSX1 = {}
EDataSX1 = {}
content = open(inputfileSX1, "r")
for num, line in enumerate(content):
	data = line.split()
	if num < 5:
		sym = float(data[0])
		DataSX1[sym] = []
		for obj in data[1:]:
			DataSX1[sym].append(float(obj))
	elif num >= 5:
		sym = float(data[0])
		EDataSX1[sym] = []
		for obj in data[1:]:
			EDataSX1[sym].append(float(obj))

DataSY1 = {}
EDataSY1 = {}
content = open(inputfileSY1, "r")
for num, line in enumerate(content):
	data = line.split()
	if num < 5:
		sym = float(data[0])
		DataSY1[sym] = []
		for obj in data[1:]:
			DataSY1[sym].append(float(obj))
	elif num >= 5:
		sym = float(data[0])
		EDataSY1[sym] = []
		for obj in data[1:]:
			EDataSY1[sym].append(float(obj))
		
DataSX2 = {}
EDataSX2 = {}
content = open(inputfileSX2, "r")
for num, line in enumerate(content):
	data = line.split()
	if num < 5:
		sym = float(data[0])
		DataSX2[sym] = []
		for obj in data[1:]:
			DataSX2[sym].append(float(obj))
	elif num >= 5:
		sym = float(data[0])
		print("len", len(data))
		EDataSX2[sym] = []
		for obj in data[1:]:
			EDataSX2[sym].append(float(obj))

DataSY2 = {}
EDataSY2 = {}
content = open(inputfileSY2, "r")
for num, line in enumerate(content):
	data = line.split()
	if num < 5:
		sym = float(data[0])
		DataSY2[sym] = []
		for obj in data[1:]:
			DataSY2[sym].append(float(obj))
	elif num >= 5:
		sym = float(data[0])
		EDataSY2[sym] = []
		for obj in data[1:]:
			EDataSY2[sym].append(float(obj))
			
print(EDataSX2)
		
plt.figure(figsize=(11, 11))
ax1 = plt.subplot(2, 2, 1)

plt.plot(DataSX1[40], DataSX1[0], color='black', label='40kN')
plt.plot(DataSX1[60], DataSX1[0], color='black', label='60kN')
plt.plot(DataSX1[80], DataSX1[0], color='black', label='80kN')
plt.plot(DataSX1[100], DataSX1[0], color='black', label='100kN')

plt.plot(EDataSX1[40], EDataSX1[0], color='black', linestyle='None', marker='s', markersize=7, label='40kN')
plt.plot(EDataSX1[60], EDataSX1[0], color='black', linestyle='None', marker='^', markersize=7, label='60kN')
plt.plot(EDataSX1[80], EDataSX1[0], color='black', linestyle='None', marker='v', markersize=7, label='80kN')
plt.plot(EDataSX1[100], EDataSX1[0], color='black', linestyle='None', marker='o', markersize=7, label='100kN')

plt.grid()

ax2 = plt.subplot(2, 2, 2)

plt.plot(DataSX2[40], [-i for i in DataSX2[0]], color='black', label='40kN')
plt.plot(DataSX2[60], [-i for i in DataSX2[0]], color='black', label='60kN')
plt.plot(DataSX2[80], [-i for i in DataSX2[0]], color='black', label='80kN')
plt.plot(DataSX2[100], [-i for i in DataSX2[0]], color='black', label='100kN')

plt.plot(EDataSX2[40], [-i for i in EDataSX2[0]], color='black', linestyle='None', marker='s', markersize=7, label='40kN')
plt.plot(EDataSX2[60], [-i for i in EDataSX2[0]], color='black', linestyle='None', marker='^', markersize=7, label='60kN')
plt.plot(EDataSX2[80], [-i for i in EDataSX2[0]], color='black', linestyle='None', marker='v', markersize=7, label='80kN')
plt.plot(EDataSX2[100], [-i for i in EDataSX2[0]], color='black', linestyle='None', marker='o', markersize=7, label='100kN')

plt.grid()

ax3 = plt.subplot(2, 2, 3)

plt.plot(DataSY1[40], DataSY1[0], color='black', label='40kN')
plt.plot(DataSY1[60], DataSY1[0], color='black', label='60kN')
plt.plot(DataSY1[80], DataSY1[0], color='black', label='80kN')
plt.plot(DataSY1[100], DataSY1[0], color='black', label='100kN')

plt.plot(EDataSY1[40][0:-1], EDataSY1[0][0:-1], color='black', linestyle='None', marker='s', markersize=7, label='40kN')
plt.plot(EDataSY1[60][0:-1], EDataSY1[0][0:-1], color='black', linestyle='None', marker='^', markersize=7, label='60kN')
plt.plot(EDataSY1[80][0:-1], EDataSY1[0][0:-1], color='black', linestyle='None', marker='v', markersize=7, label='80kN')
plt.plot(EDataSY1[100][0:-1], EDataSY1[0][0:-1], color='black', linestyle='None', marker='o', markersize=7, label='100kN')

plt.grid()

ax3 = plt.subplot(2, 2, 4)

plt.plot(DataSY2[40], [-i for i in DataSY2[0]], color='black', label='40kN')
plt.plot(DataSY2[60], [-i for i in DataSY2[0]], color='black', label='60kN')
plt.plot(DataSY2[80], [-i for i in DataSY2[0]], color='black', label='80kN')
plt.plot(DataSY2[100], [-i for i in DataSY2[0]], color='black', label='100kN')

plt.plot(EDataSY2[40], [-i for i in EDataSY2[0]], color='black', linestyle='None', marker='s', markersize=7, label='40kN')
plt.plot(EDataSY2[60], [-i for i in EDataSY2[0]], color='black', linestyle='None', marker='^', markersize=7, label='60kN')
plt.plot(EDataSY2[80], [-i for i in EDataSY2[0]], color='black', linestyle='None', marker='v', markersize=7, label='80kN')
plt.plot(EDataSY2[100], [-i for i in EDataSY2[0]], color='black', linestyle='None', marker='o', markersize=7, label='100kN')

plt.grid()

plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)
plt.show()
