inputfiles = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1213.dat"
outfile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1213.txt"

inputfiles2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1210.dat"
outfile2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1210.txt"

FEx = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1-2FELoadDisp.txt"
FEy = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY1-2FELoadDisp.txt"

execfile('../MTSsetup.py')
execfile('/media/chenting/Work/ProgramCode/Tools/Interpolation.py')
difflimit = [60,-1000,90,-10000,1000,-10000]
data1 = readfile(inputfiles, outfile, difflimit)
data2 = readfile(inputfiles2, outfile2, difflimit)

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
    
print(len(data1.Uy1))
print(len(data1.Uy2))
print(data1.Uy1[3500:3520])
print(data1.Uy2[3500:3520])    

Fy2s = [(data2.Fy1[i] - data2.Fy2[i])*2330.0/2820.0 for i in range(0, 3200)]
Fy1s = [(data1.Fy1[i] - data1.Fy2[i])*2330.0/2820.0 for i in range(0, 3520)]
Uy2s = [data2.Uy1[i]/2330.0 for i in range(0, 3200)]
Uy1s = [data1.Uy1[i]/2330.0 for i in range(0, 3520)]

plt.figure(figsize=(11, 11))

ax1 = plt.subplot(2, 2, 2)
#plt.plot(Uy1[0:-180], Fy1[0:-180])
#plt.plot(data1.Uy1[0:-180], data1.Fy1[0:-180], color='k', linestyle='-', label='Right Beam')
plt.plot(Uy1s, Fy1s, color='k', linestyle='-', label='Left Beam')
#plt.plot(FEyd, FEyl, color='g', label='FE')
#plt.legend(bbox_to_anchor=(1.02, 0.3), prop=fontprop)
plt.grid(linestyle='--')
plt.ylim(-250, 250)
plt.xlim(-0.075, 0.075)
plt.xticks([-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], ['-7.5', '-5', '-2.5', '0', '2.5', '5', '7.5'], fontproperties=fontprop)
plt.yticks([-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250], fontproperties=fontprop)
plt.xlabel('Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Shear Force in Column (kN)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.14, 0.5)

# The second pic
'''for i, obj in enumerate(data2.Uy1):
    if obj > 0:
        factor = 0.38/132*obj+1
        data2.Fy1[i] = data2.Fy1[i]*factor
        
for i, obj in enumerate(data2.Uy2):
    if obj > 0:
        #factor = 0.38/132*obj+1
        #data2.Fy2[i] = data2.Fy2[i]*factor
        data2.Fy2[i] = data2.Fy2[i]'''
        
fileout = "ShearForceSX1-2.txt"
filep1 = open(fileout, 'w')
for i, obj in enumerate(Uy2s):
    filep1.write("%f %f\n" % (obj, Fy2s[i]))

fileout = "ShearForceSY1-2.txt"
filep2 = open(fileout, 'w')
for i, obj in enumerate(Uy1s):
    filep2.write("%f %f\n" % (obj, Fy1s[i]))

ax2 = plt.subplot(2, 2, 1)
#plt.plot(Uy2[0:-200], Fy2[0:-200])
plt.plot(Uy2s, Fy2s, color='k', linestyle='-', label='Right Beam')
#plt.plot(FExd, FExl, color='g', label='FE')
#plt.legend(bbox_to_anchor=(1.02, 0.3), prop=fontprop)
plt.grid(linestyle='--')
plt.xlim(-0.075, 0.075)
plt.ylim(-250, 250)
#plt.xlim(0, 180)
plt.xticks([-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], ['-7.5', '-5', '-2.5', '0', '2.5', '5', '7.5'], fontproperties=fontprop)
plt.yticks([-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250], fontproperties=fontprop)
plt.xlabel('Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Shear Force in Column (kN)', fontproperties=fontprop)
ax2.yaxis.set_label_coords(-0.14, 0.5)

# Integration, Area Calculation
data1i = []
print("SY1-2")
for i, obj in enumerate(data1.Uy1):
    if i==0:
        da = data1.Uy1[i]*data1.Fy1[i]/2/1000 + data1.Uy2[i]*data1.Fy2[i]/2/1000
    else:
        da = (data1.Uy1[i]-data1.Uy1[i-1])*(data1.Fy1[i]+data1.Fy1[i-1])*0.5/1000 + (data1.Uy2[i]-data1.Uy2[i-1])*(data1.Fy2[i]+data1.Fy2[i-1])*0.5/1000
    if len(data1i) == 0:
        data1i.append(da)
    else:
        data1i.append(data1i[-1]+da)
    if i>20 and data1.Uy1[i]*data1.Uy1[i-1]<=0:
    	Eg = LinearInterpolation2D(data1.Uy1[i-1], data1i[-2], data1.Uy1[i], data1i[-1], 0)
    	print(Eg)
        
# The third graph
ax3 = plt.subplot(2, 2, 4)
plt.plot(Uy1s, data1i[0:3520], color='k', linestyle='-')
#plt.plot(FEyd, FEyl, color='g', label='FE')
plt.legend(bbox_to_anchor=(1.02, 0.3), prop=fontprop)
plt.grid(linestyle='--')
plt.ylim(0, 350)
plt.yticks([0, 50, 100, 150, 200, 250, 300, 350], fontproperties=fontprop)
plt.xlim(-0.075, 0.075)
plt.xticks([-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], ['-7.5', '-5', '-2.5', '0', '2.5', '5', '7.5'], fontproperties=fontprop)
#plt.yticks([0, 100, 200, 300, 400, 500], fontproperties=fontprop)
plt.xlabel('Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Energy Dissapation (kN*m)', fontproperties=fontprop)
ax3.yaxis.set_label_coords(-0.14, 0.5)

data2i = []
for i, obj in enumerate(data2.Uy1):
    if i==0:
        da = data2.Uy1[i]*data2.Fy1[i]/1000 + data2.Uy2[i]*data2.Fy2[i]/1000
    else:
        da = (data2.Uy1[i]-data2.Uy1[i-1])*data2.Fy1[i]/1000 + (data2.Uy2[i]-data2.Uy2[i-1])*data2.Fy2[i]/1000
    if len(data2i) == 0:
        data2i.append(da)
    else:
        data2i.append(data2i[-1]+da)
        
# The Fourth graph
ax4 = plt.subplot(2, 2, 3)
plt.plot(Uy2s, data2i[0:3200], color='k', linestyle='-')
#plt.plot(FEyd, FEyl, color='g', label='FE')
plt.legend(bbox_to_anchor=(1.02, 0.3), prop=fontprop)
plt.grid(linestyle='--')
#plt.ylim(-20, 500)
plt.xlim(-0.075, 0.075)
plt.xticks([-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], ['-7.5', '-5', '-2.5', '0', '2.5', '5', '7.5'], fontproperties=fontprop)
plt.ylim(0, 350)
plt.yticks([0, 50, 100, 150, 200, 250, 300, 350], fontproperties=fontprop)
#plt.yticks([0, 100, 200, 300, 400, 500], fontproperties=fontprop)
plt.xlabel('Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Energy Dissapation (kN*m)', fontproperties=fontprop)
ax4.yaxis.set_label_coords(-0.14, 0.5)


plt.subplots_adjust(left=0.1, right=0.98, wspace=0.22, hspace=0.22, bottom=0.12, top=0.95)

plt.show()
