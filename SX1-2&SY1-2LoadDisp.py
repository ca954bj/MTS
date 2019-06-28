inputfiles = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1213.dat"
outfile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1213.txt"

inputfiles2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1210.dat"
outfile2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1210.txt"

FEx = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1-2FELoadDisp.txt"
FEy = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY1-2FELoadDisp.txt"

execfile('MTSsetup.py')
difflimit = [60,-1000,90,-10000,1000,-10000]
data1 = readfile(inputfiles, outfile, difflimit)

FExd = []
FExl = []
FEyd = []
FEyl = []
FExf = open(FEx)
FEyf = open(FEy)
for line in FExf:
    spl = line.split()
    FExd.append(float(spl[0]))
    FExl.append(float(spl[1]))

for line in FEyf:
    spl = line.split()
    FEyd.append(float(spl[0]))
    FEyl.append(float(spl[1]))

plt.figure(figsize=(11, 11))

ax1 = plt.subplot(2, 2, 2)
#plt.plot(Uy1[0:-180], Fy1[0:-180])
plt.plot(data1.Uy1[0:-180], data1.Fy1[0:-180], color='k', linestyle='-', label='Right Beam')
plt.plot(data1.Uy2[0:-180], data1.Fy2[0:-180], color='k', linestyle='--', label='Left Beam')
#plt.plot(FEyd, FEyl, color='g', label='FE')
plt.legend(bbox_to_anchor=(1.02, 0.3), prop=fontprop)
plt.grid(linestyle='--')
plt.ylim(-175, 175)
plt.xlim(-180, 180)
plt.xticks([-180, -120, -60, 0, 60, 120, 180], fontproperties=fontprop)
plt.yticks([-175, -150, -100, -50, 0, 50, 100, 150, 175], fontproperties=fontprop)
plt.xlabel('Vertical Displacement (mm)', fontproperties=fontprop)
plt.ylabel('Vertical Load (kN)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.1, 0.5)

# The second pic
data2 = readfile(inputfiles2, outfile2, difflimit)
for i, obj in enumerate(data2.Uy1):
    if obj > 0:
        factor = 0.38/132*obj+1
        data2.Fy1[i] = data2.Fy1[i]*factor
        
for i, obj in enumerate(data2.Uy2):
    if obj > 0:
        factor = 0.38/132*obj+1
        data2.Fy2[i] = data2.Fy2[i]*factor
        
fileout = "ModifiedDataSX1-2-1.txt"
filep1 = open(fileout, 'w')
for i, obj in enumerate(data2.Uy1):
    filep1.write("%f\n" % data2.Fy1[i])

fileout = "ModifiedDataSX1-2-2.txt"
filep2 = open(fileout, 'w')
for i, obj in enumerate(data2.Uy2):
    filep2.write("%f\n" % data2.Fy2[i])

ax2 = plt.subplot(2, 2, 1)
#plt.plot(Uy2[0:-200], Fy2[0:-200])
plt.plot(data2.Uy1[0:-180], data2.Fy1[0:-180], color='k', linestyle='-', label='Right Beam')
plt.plot(data2.Uy2[0:-180], data2.Fy2[0:-180], color='k', linestyle='--', label='Left Beam')
#plt.plot(FExd, FExl, color='g', label='FE')
plt.legend(bbox_to_anchor=(1.02, 0.3), prop=fontprop)
plt.grid(linestyle='--')
plt.xlim(-180, 180)
plt.ylim(-175, 175)
#plt.xlim(0, 180)
plt.xticks([-180, -120, -60, 0, 60, 120, 180], fontproperties=fontprop)
plt.yticks([-175, -150, -100, -50, 0, 50, 100, 150, 175], fontproperties=fontprop)
plt.xlabel('Vertical Displacement (mm)', fontproperties=fontprop)
plt.ylabel('Vertical Load (kN)', fontproperties=fontprop)
ax2.yaxis.set_label_coords(-0.12, 0.5)

# Integration, Area Calculation
data1i = []
for i, obj in enumerate(data1.Uy1):
    da = data1.Uy1[i]*data1.Fy1[1]/1000 + data1.Uy2[i]*data1.Fy2[1]/1000
    if len(data1i) == 0:
        data1i.append(da)
    else:
        data1i.append(data1i[-1]+da)
        
# The third graph
ax3 = plt.subplot(2, 2, 4)
plt.plot(data1.Uy1[0:-180], data1i[0:-180], color='k', linestyle='-')
#plt.plot(FEyd, FEyl, color='g', label='FE')
plt.legend(bbox_to_anchor=(1.02, 0.3), prop=fontprop)
plt.grid(linestyle='--')
plt.ylim(-20, 500)
plt.xlim(-180, 180)
plt.xticks([-180, -120, -60, 0, 60, 120, 180], fontproperties=fontprop)
plt.yticks([0, 100, 200, 300, 400, 500], fontproperties=fontprop)
plt.xlabel('Vertical Displacement (mm)', fontproperties=fontprop)
plt.ylabel('Energy Dissapation (N*m)', fontproperties=fontprop)
ax3.yaxis.set_label_coords(-0.12, 0.5)

data2i = []
for i, obj in enumerate(data2.Uy1):
    da = data2.Uy1[i]*data2.Fy1[1]/1000 + data2.Uy2[i]*data2.Fy2[1]/1000
    if len(data2i) == 0:
        data2i.append(da)
    else:
        data2i.append(data2i[-1]+da)
        
# The Fourth graph
ax4 = plt.subplot(2, 2, 3)
plt.plot(data2.Uy1[0:-180], data2i[0:-180], color='k', linestyle='-')
#plt.plot(FEyd, FEyl, color='g', label='FE')
plt.legend(bbox_to_anchor=(1.02, 0.3), prop=fontprop)
plt.grid(linestyle='--')
plt.ylim(-20, 500)
plt.xlim(-180, 180)
plt.xticks([-180, -120, -60, 0, 60, 120, 180], fontproperties=fontprop)
plt.yticks([0, 100, 200, 300, 400, 500], fontproperties=fontprop)
plt.xlabel('Vertical Displacement (mm)', fontproperties=fontprop)
plt.ylabel('Energy Dissapation (N*m)', fontproperties=fontprop)
ax4.yaxis.set_label_coords(-0.12, 0.5)


plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.22, bottom=0.12, top=0.95)

plt.show()
