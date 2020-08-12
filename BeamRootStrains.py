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
			DataSX1[sym].append(-float(obj))
	elif num >= 5:
		sym = float(data[0])
		EDataSX1[sym] = []
		for obj in data[1:]:
			EDataSX1[sym].append(-float(obj))

DataSY1 = {}
EDataSY1 = {}
content = open(inputfileSY1, "r")
for num, line in enumerate(content):
	data = line.split()
	if num < 5:
		sym = float(data[0])
		DataSY1[sym] = []
		for obj in data[1:]:
			DataSY1[sym].append(-float(obj))
	elif num >= 5:
		sym = float(data[0])
		EDataSY1[sym] = []
		for obj in data[1:]:
			EDataSY1[sym].append(-float(obj))
		
DataSX2 = {}
EDataSX2 = {}
content = open(inputfileSX2, "r")
for num, line in enumerate(content):
	data = line.split()
	if num < 5:
		sym = float(data[0])
		DataSX2[sym] = []
		for obj in data[1:]:
			DataSX2[sym].append(-float(obj))
	elif num >= 5:
		sym = float(data[0])
		print("len", len(data))
		EDataSX2[sym] = []
		for obj in data[1:]:
			EDataSX2[sym].append(-float(obj))

DataSY2 = {}
EDataSY2 = {}
content = open(inputfileSY2, "r")
for num, line in enumerate(content):
	data = line.split()
	if num < 5:
		sym = float(data[0])
		DataSY2[sym] = []
		for obj in data[1:]:
			DataSY2[sym].append(-float(obj))
	elif num >= 5:
		sym = float(data[0])
		EDataSY2[sym] = []
		for obj in data[1:]:
			EDataSY2[sym].append(-float(obj))
			
print(EDataSX2)
		
plt.figure(figsize=(11, 11))
ax1 = plt.subplot(2, 2, 1)

p11,= plt.plot(DataSX1[40], DataSX1[0], color='black', label='40kN', linestyle='solid')
p12,= plt.plot(DataSX1[60], DataSX1[0], color='black', label='60kN', linestyle='dashdot')
p13,= plt.plot(DataSX1[80], DataSX1[0], color='black', label='80kN', linestyle='dashed')
p14,= plt.plot(DataSX1[100], DataSX1[0], color='black', label='100kN', linestyle='dotted')

p11e,= plt.plot(EDataSX1[40][1:], EDataSX1[0][1:], color='black', linestyle='None', marker='s', markersize=7, label='40kN')
p12e,= plt.plot(EDataSX1[60][1:], EDataSX1[0][1:], color='black', linestyle='None', marker='^', markersize=7, label='60kN')
p13e,= plt.plot(EDataSX1[80][1:], EDataSX1[0][1:], color='black', linestyle='None', marker='v', markersize=7, label='80kN')
p14e,= plt.plot(EDataSX1[100][1:], EDataSX1[0][1:], color='black', linestyle='None', marker='o', markersize=7, label='100kN')

plt.grid(linestyle = "--")
plt.ylim(-200, 200)
plt.xlim(-1700, 1700)
plt.xticks([-1500, -1000, -500, 0, 500, 1000, 1500], ['-0.15', '-0.1', '-0.05', '0', '0.05', '0.1', '0.15'], fontproperties=fontprop)
plt.yticks([-200, -150, -100, -50, 0, 50, 100, 150, 200], fontproperties=fontprop)
plt.xlabel('Strain (%)', fontproperties=fontprop)
plt.ylabel('Position (mm)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.1, 0.5)
firstlegend = plt.legend(handles=[p11, p12, p13, p14], loc=1, bbox_to_anchor=(0.35, 0.99), prop=fontprop, title='FE:', frameon=False)
secondlegend = plt.legend(handles=[p11e, p12e, p13e, p14e], loc=1, bbox_to_anchor=(0.98, 0.45), prop=fontprop, title='Exp:', frameon=False)
plt.gca().add_artist(firstlegend)
plt.gca().add_artist(secondlegend)

ax2 = plt.subplot(2, 2, 2)

p11,= plt.plot(DataSX2[40], [-i for i in DataSX2[0]], color='black', label='40kN', linestyle='solid')
p12,= plt.plot(DataSX2[60], [-i for i in DataSX2[0]], color='black', label='60kN', linestyle='dashdot')
p13,= plt.plot(DataSX2[80], [-i for i in DataSX2[0]], color='black', label='80kN', linestyle='dashed')
p14,= plt.plot(DataSX2[100], [-i for i in DataSX2[0]], color='black', label='100kN', linestyle='dotted')

p11e,= plt.plot(EDataSX2[40], [-i for i in EDataSX2[0]], color='black', linestyle='None', marker='s', markersize=7, label='40kN')
p12e,= plt.plot(EDataSX2[60], [-i for i in EDataSX2[0]], color='black', linestyle='None', marker='^', markersize=7, label='60kN')
p13e,= plt.plot(EDataSX2[80], [-i for i in EDataSX2[0]], color='black', linestyle='None', marker='v', markersize=7, label='80kN')
p14e,= plt.plot(EDataSX2[100], [-i for i in EDataSX2[0]], color='black', linestyle='None', marker='o', markersize=7, label='100kN')

plt.grid(linestyle = "--")
plt.ylim(-200, 200)
plt.xlim(-1700, 1700)
plt.xticks([-1500, -1000, -500, 0, 500, 1000, 1500], ['-0.15', '-0.1', '-0.05', '0', '0.05', '0.1', '0.15'], fontproperties=fontprop)
plt.yticks([-200, -150, -100, -50, 0, 50, 100, 150, 200], fontproperties=fontprop)
plt.xlabel('Strain (%)', fontproperties=fontprop)
plt.ylabel('Position (mm)', fontproperties=fontprop)
ax2.yaxis.set_label_coords(-0.1, 0.5)
firstlegend = plt.legend(handles=[p11, p12, p13, p14], loc=1, bbox_to_anchor=(0.35, 0.99), prop=fontprop, title='FE:', frameon=False)
secondlegend = plt.legend(handles=[p11e, p12e, p13e, p14e], loc=1, bbox_to_anchor=(0.98, 0.45), prop=fontprop, title='Exp:', frameon=False)
plt.gca().add_artist(firstlegend)
plt.gca().add_artist(secondlegend)

ax3 = plt.subplot(2, 2, 3)

p11,= plt.plot(DataSY1[40], DataSY1[0], color='black', label='40kN', linestyle='solid')
p12,= plt.plot(DataSY1[60], DataSY1[0], color='black', label='60kN', linestyle='dashdot')
p13,= plt.plot(DataSY1[80], DataSY1[0], color='black', label='80kN', linestyle='dashed')
p14,= plt.plot(DataSY1[100], DataSY1[0], color='black', label='100kN', linestyle='dotted')

p11e,= plt.plot(EDataSY1[40][1:], EDataSY1[0][1:], color='black', linestyle='None', marker='s', markersize=7, label='40kN')
p12e,= plt.plot(EDataSY1[60][1:], EDataSY1[0][1:], color='black', linestyle='None', marker='^', markersize=7, label='60kN')
p13e,= plt.plot(EDataSY1[80][1:], EDataSY1[0][1:], color='black', linestyle='None', marker='v', markersize=7, label='80kN')
p14e,= plt.plot(EDataSY1[100][1:], EDataSY1[0][1:], color='black', linestyle='None', marker='o', markersize=7, label='100kN')

firstlegend = plt.legend(handles=[p11, p12, p13, p14], loc=1, bbox_to_anchor=(0.35, 0.99), prop=fontprop, title='FE:', frameon=False)
secondlegend = plt.legend(handles=[p11e, p12e, p13e, p14e], loc=1, bbox_to_anchor=(0.98, 0.45), prop=fontprop, title='Exp:', frameon=False)
plt.gca().add_artist(firstlegend)
plt.gca().add_artist(secondlegend)

plt.grid(linestyle = "--")
plt.ylim(-200, 200)
plt.xlim(-1700, 1700)
plt.xticks([-1500, -1000, -500, 0, 500, 1000, 1500], ['-0.15', '-0.1', '-0.05', '0', '0.05', '0.1', '0.15'], fontproperties=fontprop)
plt.yticks([-200, -150, -100, -50, 0, 50, 100, 150, 200], fontproperties=fontprop)
plt.xlabel('Strain (%)', fontproperties=fontprop)
plt.ylabel('Position (mm)', fontproperties=fontprop)
ax3.yaxis.set_label_coords(-0.1, 0.5)

ax4 = plt.subplot(2, 2, 4)

p11,= plt.plot(DataSY2[40], [-i for i in DataSY2[0]], color='black', label='40kN', linestyle='solid')
p12,= plt.plot(DataSY2[60], [-i for i in DataSY2[0]], color='black', label='60kN', linestyle='dashdot')
p13,= plt.plot(DataSY2[80], [-i for i in DataSY2[0]], color='black', label='80kN', linestyle='dashed')
p14,= plt.plot(DataSY2[100], [-i for i in DataSY2[0]], color='black', label='100kN', linestyle='dotted')

p11e,= plt.plot(EDataSY2[40], [-i for i in EDataSY2[0]], color='black', linestyle='None', marker='s', markersize=7, label='40kN')
p12e,= plt.plot(EDataSY2[60], [-i for i in EDataSY2[0]], color='black', linestyle='None', marker='^', markersize=7, label='60kN')
p13e,= plt.plot(EDataSY2[80], [-i for i in EDataSY2[0]], color='black', linestyle='None', marker='v', markersize=7, label='80kN')
p14e,= plt.plot(EDataSY2[100], [-i for i in EDataSY2[0]], color='black', linestyle='None', marker='o', markersize=7, label='100kN')

plt.grid(linestyle = "--")
plt.ylim(-200, 200)
plt.xlim(-1700, 1700)
plt.xticks([-1500, -1000, -500, 0, 500, 1000, 1500], ['-0.15', '-0.1', '-0.05', '0', '0.05', '0.1', '0.15'], fontproperties=fontprop)
plt.yticks([-200, -150, -100, -50, 0, 50, 100, 150, 200], fontproperties=fontprop)
plt.xlabel('Strain (%)', fontproperties=fontprop)
plt.ylabel('Position (mm', fontproperties=fontprop)
ax4.yaxis.set_label_coords(-0.1, 0.5)
firstlegend = plt.legend(handles=[p11, p12, p13, p14], loc=1, bbox_to_anchor=(0.35, 0.99), prop=fontprop, title='FE:', frameon=False)
secondlegend = plt.legend(handles=[p11e, p12e, p13e, p14e], loc=1, bbox_to_anchor=(0.98, 0.45), prop=fontprop, title='Exp:', frameon=False)
plt.gca().add_artist(firstlegend)
plt.gca().add_artist(secondlegend)

plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.2, bottom=0.07, top=0.95)
plt.show()

## For printing data only ================================================================
outputd = [DataSY1[40], DataSY1[0], DataSY1[60], DataSY1[0], DataSY1[80], DataSY1[0], DataSY1[100], DataSY1[0], DataSY2[40], DataSY2[0], DataSY2[60], DataSY2[0], DataSY2[80], DataSY2[0], DataSY2[100], DataSY2[0]]
fnout = open('Fig.txt', 'w')
for obj1 in outputd:
    for obj2 in obj1:
        fnout.write('%s'%obj2)
        fnout.write(' ')
    fnout.write('\n')
fnout.close()
## =====================================================================================
