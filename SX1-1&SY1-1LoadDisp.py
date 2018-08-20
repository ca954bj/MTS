inputfiles = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1130.dat"
outfile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1130.txt"

inputfiles2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1206.dat"
outfile2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1206.txt"

inputfiles2FE = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1-1FELoadDisp.txt"
inputfilesFE = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY1-1FELoadDisp.txt"

inputfiletr2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1-1TheoreticalInitialStiffness.txt"
inputfiletr1 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY1-1TheoreticalInitialStiffness.txt"

inputfiletrrm1 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY1-1InitialStiffnesswithMR.txt"
inputfiletrrm2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1-1InitialStiffnesswithMR.txt"

execfile('MTSsetup.py')
difflimit = [60, -15, 90, -0.5, 1000, -0.1]

MySX = 108.622
MySY = 103.240

MyX = range(0, 50)

FE1x = []
FE1y = []
FESX11 = open(inputfiles2FE)
for line in FESX11:
    nums = line.split()
    if len(nums) > 1:
        FE1x.append(float(nums[0]))
        FE1y.append(float(nums[1]))

FE2x = []
FE2y = []
FESX21 = open(inputfilesFE)
for line in FESX21:
    nums = line.split()
    if len(nums) > 1:
        FE2x.append(float(nums[0]))
        FE2y.append(float(nums[1]))

Tr2x = []
Tr2y = []
TRSX21 = open(inputfiletr2)
for line in TRSX21:
    nums = line.split()
    if len(nums) > 1:
        Tr2x.append(float(nums[0]))
        Tr2y.append(float(nums[1]))

Tr1x = []
Tr1y = []
TRSX11 = open(inputfiletr1)
for line in TRSX11:
    nums = line.split()
    if len(nums) > 1:
        Tr1x.append(float(nums[0]))
        Tr1y.append(float(nums[1]))

Trrm1x = []
Trrm1y = []
TRrmSY21 = open(inputfiletrrm1)
for line in TRrmSY21:
    nums = line.split()
    if len(nums) > 1:
        Trrm1x.append(float(nums[0]))
        Trrm1y.append(float(nums[1]))

Trrm2x = []
Trrm2y = []
TRrmSX21 = open(inputfiletrrm2)
for line in TRrmSX21:
    nums = line.split()
    if len(nums) > 1:
        Trrm2x.append(float(nums[0]))
        Trrm2y.append(float(nums[1]))

# The first plot, SY1-1
data1 = readfile(inputfiles, outfile, difflimit)
print(data1.Uy1)
print(data1.Uy2)

data1Uy1g = []
for i, obj in enumerate(data1.Uy1):
    data1Uy1g.append(obj*(1-0.074))

plt.figure(figsize=(11, 5))

ax1 = plt.subplot(1, 2, 2)
reverse1 = []
reverse2 = []
for i in range(0, len(data1.Uy2)):
    reverse1.append((-(data1.Uy2[i]) - 4)*(1-0.074))
    reverse2.append(-(data1.Fy2[i]) - 4)

#Uy1[0:-100]

# Plot Right Beam Experimental Data
plt.plot(data1Uy1g, data1.Fy1, color='black', label='Right Beam', marker='^', markersize=10, markevery=(115, 35))
p1 = mlines.Line2D([], [], color='black', marker='^', markersize=10, label='Right Beam')

# Plot Left Beam Experimental Data
plt.plot(reverse1[5:], reverse2[5:], color='black', label='Left Beam', marker='v', markersize=10, markevery=(110, 35))
p2 = mlines.Line2D([], [], color='black', marker='v', markersize=10, label='Left Beam')

# Plot Detailed FE Data
plt.plot(FE2x, FE2y, color='black', label='FEM', marker='o', markersize=10, markevery=(72, 18))
p3 = mlines.Line2D([], [], color='black', marker='o', markersize=10, label='FEM')

# Plot Rigid Connection Curve
#p4, = plt.plot(Tr1x, Tr1y, color='y', label='Theoretical Initial Stiffness')

# Plot Simplified Simulation Curve
#p5, = plt.plot(Trrm2x, Trrm2y, color = 'black', label='Modelling', marker='s', markersize=10, markevery=(40, 10))
#plt.legend(handles=[p1, p5], loc=1, bbox_to_anchor=(0.99, 0.3), prop=fontprop)

plt.legend(handles=[p1, p2, p3], loc=1, bbox_to_anchor=(0.99, 0.3), prop=fontprop)
#plt.gca().add_artist(legend1)
#plt.gca().add_artist(legend2)
plt.grid()
plt.ylim(0, 180)
plt.xlim(0, 135)
plt.xticks([0, 30, 60, 90, 120, 135], fontproperties=fontprop)
plt.yticks([0, 30, 60, 90, 120, 150, 180], fontproperties=fontprop)
plt.xlabel('Vertical Displacement (mm)', fontproperties=fontprop)
plt.ylabel('Vertical Load (kN)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.1, 0.5)

# The second pic, SX1-1
data2 = readfile(inputfiles2, outfile2, difflimit)
print(data2.Uy1)
print(data2.Uy2)

ax2 = plt.subplot(1, 2, 1)
reverse1 = []
reverse2 = []
for i in range(0, len(data2.Uy1)):
    reverse1.append(-(data2.Uy1[i])*(1-0.074))
    reverse2.append(-(data2.Fy1[i]))

data2uy2g = []
for i in range(0, len(data2.Uy2)):
    data2uy2g.append((data2.Uy2[i] - 1)*(1-0.074))

#Uy2[0:-200]
plt.plot(reverse1[40:], reverse2[40:], color='black', label='Right Beam', marker='^', markersize=10, markevery=(120, 40))
p1 = mlines.Line2D([], [], color='black', marker='^', markersize=10, label='Right Beam')
plt.plot(data2uy2g[61:], data2.Fy2[61:], color='black', label='Left Beam', marker='v', markersize=10, markevery=(100, 40))
p2 = mlines.Line2D([], [], color='black', marker='v', markersize=10, label='Left Beam')
plt.plot(FE1x, FE1y, color='black', marker='o', markersize=10, label='FEM', markevery=(90, 40))
p3 = mlines.Line2D([], [], color='black', marker='o', markersize=10, label='FEM')
#plt.plot(MyX, [MySX]*len(MyX), linestyle='dashed')

plt.legend(handles=[p1, p2, p3], loc=1, bbox_to_anchor=(0.99, 0.3), prop=fontprop)

plt.grid()
plt.ylim(0, 180)
plt.xlim(0, 135)
plt.xticks([0, 30, 60, 90, 120, 135], fontproperties=fontprop)
plt.yticks([0, 30, 60, 90, 120, 150, 180], fontproperties=fontprop)
plt.xlabel('Vertical Displacement (mm)', fontproperties=fontprop)
plt.ylabel('Vertical Load (kN)', fontproperties=fontprop)
ax2.yaxis.set_label_coords(-0.1, 0.5)

plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)

plt.show()

