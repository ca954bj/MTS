inputfiles = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1220.dat"
outfile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1220.txt"

inputfiles2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/d1222.dat"
outfile2 = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1222.txt"



execfile('MTSsetup2.py')
difflimit = 20
data1 = readfile(inputfiles, outfile, difflimit)



plt.figure(figsize=(11, 5))

ax1 = plt.subplot(1, 2, 1)
reverse1 = []
reverse2 = []
for i in range(0, len(data1.Uy1)-15):
    reverse1.append(-(data1.Uy1[i]))
    reverse2.append(-(data1.Fy1[i]))
plt.plot(reverse1, reverse2, color='b')

#plt.plot(reverse1, reverse2, color='r', label='Left Beam')
plt.legend(bbox_to_anchor=(0.5, 1), prop=fontprop)
plt.grid()
plt.ylim(-175, 175)
plt.xlim(-180, 180)
plt.xticks([-180, -120, -60, 0, 60, 120, 180], fontproperties=fontprop)
plt.yticks([-175, -150, -100, -50, 0, 50, 100, 150, 175], fontproperties=fontprop)
plt.xlabel('Vertical Displacement (mm)', fontproperties=fontprop)
plt.ylabel('Vertical Load (kN)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.1, 0.5)

# The second pic
data2 = readfile(inputfiles2, outfile2, difflimit)

ax2 = plt.subplot(1, 2, 2)
reverse1 = []
reverse2 = []
for i in range(0, len(data2.Uy1)-25):
    reverse1.append(-(data2.Uy1[i]))
    reverse2.append(-(data2.Fy1[i]))
#plt.plot(reverse1, reverse2, color='b', label='Right Beam')
plt.plot(reverse1, reverse2, color='b')

plt.legend(bbox_to_anchor=(0.5, 1), prop=fontprop)
plt.grid()
plt.ylim(-175, 175)
plt.xlim(-180, 180)
plt.xticks([-180, -120, -60, 0, 60, 120, 180], fontproperties=fontprop)
plt.yticks([-175, -150, -100, -50, 0, 50, 100, 150, 175], fontproperties=fontprop)
plt.xlabel('Vertical Displacement (mm)', fontproperties=fontprop)
plt.ylabel('Vertical Load (kN)', fontproperties=fontprop)
ax2.yaxis.set_label_coords(-0.1, 0.5)

plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)

plt.show()

