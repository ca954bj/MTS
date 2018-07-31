inputfiles = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1215.dat"
outfile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1215.txt"

inputfiles2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1218.dat"
outfile2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1218.txt"

inputfiletrrm1 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX2-1FELoadDisp.txt"
inputfiletrrm2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY2-1FELoadDisp.txt"

execfile('MTSsetup2.py')
difflimit = 20
data1 = readfile(inputfiles, outfile, difflimit)

reverse1 = []
reverse2 = []
for i in range(0, len(data1.Uy1)):
    reverse1.append(-(data1.Uy1[i]*(1-0.074)))
    reverse2.append(-(data1.Fy1[i]))

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

# ====================== Start to Plot ======================================================================
# ======================= The first plot ====================================================================

plt.figure(figsize=(11, 5))

ax1 = plt.subplot(1, 2, 2)

p1, = plt.plot(reverse1[200:-100], reverse2[200:-100], color='black', label='Experiment', marker='^', markersize=10, markevery=(50, 60))
p5, = plt.plot(Trrm2x, Trrm2y, color = 'black', label='FEM', marker='o', markersize=10, markevery=(30, 30))
plt.legend(handles=[p1, p5], loc=1, bbox_to_anchor=(0.99, 0.3), prop=fontprop)

plt.grid()
plt.ylim(0, 180)
plt.xlim(0, 135)
plt.xticks([0, 30, 60, 90, 120, 135], fontproperties=fontprop)
plt.yticks([0, 30, 60, 90, 120, 150, 180], fontproperties=fontprop)
plt.xlabel('Vertical Displacement (mm)', fontproperties=fontprop)
plt.ylabel('Vertical Load (kN)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.1, 0.5)

# ============================ The second pic ===============================================================
data2 = readfile(inputfiles2, outfile2, difflimit)

ax2 = plt.subplot(1, 2, 1)
reverse1 = []
reverse2 = []
for i in range(0, len(data2.Uy1)):
    reverse1.append(-(data2.Uy1[i]*(1-0.074)))
    reverse2.append(-(data2.Fy1[i]))
#plt.plot(reverse1, reverse2, color='b', label='Right Beam')
p1, = plt.plot(reverse1[200:-100], reverse2[200:-100], color='black', label='Experiment', marker='^', markersize=10, markevery=(50, 40))
p5, = plt.plot(Trrm1x, Trrm1y, color = 'black', label='FEM', marker='o', markersize=10, markevery=(60, 60))
plt.legend(handles=[p1, p5], loc=1, bbox_to_anchor=(0.99, 0.3), prop=fontprop)
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

