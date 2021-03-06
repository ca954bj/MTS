inputfiles = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1220.dat"
outfile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1220.txt"

inputfiles2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1222.dat"
outfile2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1222.txt"

inputfiletrrm1 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX2-2FELoadDisp.txt"
inputfiletrrm2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY2-2FELoadDisp.txt"



execfile('../MTSsetup2.py')
difflimit = 20
data1 = readfile(inputfiles, outfile, difflimit)
data2 = readfile(inputfiles2, outfile2, difflimit)

reverse1 = []
reverse2 = []
for i in range(0, len(data1.Uy1)):
    reverse1.append(-(data1.Uy1[i])/2330.0)
    reverse2.append(-(data1.Fy1[i])*2330.0/2820)
    
reverse3 = []
reverse4 = []
for i in range(0, len(data2.Uy1)):
    reverse3.append(-(data2.Uy1[i])/2330.0)
    reverse4.append(-(data2.Fy1[i])*2330.0/2820)

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

# ========================================================================================================

fileout = "ShearForceSX2-2.txt"
filep1 = open(fileout, 'w')
for i, obj in enumerate(reverse1[0:-25]):
    filep1.write("%f %f\n" % (obj, reverse2[i]))

fileout = "ShearForceSY2-2.txt"
filep2 = open(fileout, 'w')
for i, obj in enumerate(reverse3[0:-25]):
    filep2.write("%f %f\n" % (obj, reverse4[i]))

# ====================== Start to Plot ======================================================================
# ======================= The first plot ====================================================================

plt.figure(figsize=(11,11))

ax1 = plt.subplot(2, 2, 1)

p1, = plt.plot(reverse1[0:-25], reverse2[0:-25], color='black', label='Experiment', linestyle='-')
#p5, = plt.plot(Trrm1x, Trrm1y, color = 'black', label='FEM', linestyle='--')
#plt.legend(handles=[p1, p5], loc=1, bbox_to_anchor=(0.99, 0.2), prop=fontprop)

plt.grid(linestyle='--')
plt.ylim(-250, 250)
plt.xlim(-0.075, 0.075)
plt.xticks([-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], ['-7.5', '-5', '-2.5', '0', '2.5', '5', '7.5'], fontproperties=fontprop)
plt.yticks([-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250], fontproperties=fontprop)
plt.xlabel('Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Shear Force in Column (kN)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.14, 0.5)

# ============================ The second pic ===============================================================
data2 = readfile(inputfiles2, outfile2, difflimit)

ax2 = plt.subplot(2, 2, 2)
p1, = plt.plot(reverse3[0:-25], reverse4[0:-25], color='black', label='Experiment', linestyle='-')
#p5, = plt.plot(Trrm2x, Trrm2y, color = 'black', label='FEM', linestyle='--')
#plt.legend(handles=[p1, p5], loc=1, bbox_to_anchor=(0.99, 0.2), prop=fontprop)
plt.grid(linestyle='--')
plt.ylim(-250, 250)
plt.xlim(-0.075, 0.075)
plt.xticks([-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], ['-7.5', '-5', '-2.5', '0', '2.5', '5', '7.5'], fontproperties=fontprop)
plt.yticks([-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250], fontproperties=fontprop)
plt.xlabel('Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Shear Force in Column (kN)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.14, 0.5)

## ============================ The third pic ===============================================================
Length1 = len(data1.Uy1)
EnergyIncr = 0
Energy1 = []
for i in range(1, Length1):
    EnergyIncr += (data1.Uy1[i] - data1.Uy1[i-1]) * (data1.Fy1[i] + data1.Fy1[i-1])/2/1000
    Energy1.append(EnergyIncr)

ax2 = plt.subplot(2, 2, 3)
p1, = plt.plot(reverse1[1:], Energy1[0:], color='black', label='Experiment', linestyle='-')
plt.grid(linestyle='--')
#plt.ylim(0, 500)
plt.xlim(-0.075, 0.075)
plt.ylim(0, 350)
plt.xticks([-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], ['-7.5', '-5', '-2.5', '0', '2.5', '5', '7.5'], fontproperties=fontprop)
plt.yticks([0, 50, 100, 150, 200, 250, 300, 350], fontproperties=fontprop)
plt.xlabel('Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Energy (kN*m)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.14, 0.5)

## ============================ The fourth pic ===============================================================
Length2 = len(data2.Uy1)
EnergyIncr = 0
Energy2 = []
for i in range(1, Length2):
    EnergyIncr += (data2.Uy1[i] - data2.Uy1[i-1]) * (data2.Fy1[i] + data2.Fy1[i-1])/2/1000
    Energy2.append(EnergyIncr)

ax2 = plt.subplot(2, 2, 4)
p1, = plt.plot(reverse3[1:], Energy2[0:], color='black', label='Experiment', linestyle='-')
plt.grid(linestyle='--')
#plt.ylim(0, 500)
plt.xlim(-0.075, 0.075)
#plt.ylim(0, 350)
plt.ylim(0, 150)
plt.xticks([-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], ['-7.5', '-5', '-2.5', '0', '2.5', '5', '7.5'], fontproperties=fontprop)
#plt.yticks([0, 50, 100, 150, 200, 250, 300, 350], fontproperties=fontprop)
plt.yticks([0, 50, 100, 150], fontproperties=fontprop)
plt.xlabel('Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Energy (kN*m)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.14, 0.5)

plt.subplots_adjust(left=0.1, right=0.98, wspace=0.22, hspace=0.22, bottom=0.12, top=0.95)

plt.show()

