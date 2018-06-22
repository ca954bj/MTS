import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.lines as mlines

fn = open("/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SteelRods.txt")
fn2 = open("/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/InternalStiffnersAxialLoad.txt")
Disp1 = []
Force1 = []
Disp2 = []
Force2 = []
N11 = []
N12 = []
N12g = []
N13 = []
N21 = []
N22 = []
N23 = []
N31 = []
N32 = []
N32g = []
N33 = []
N41 = []
N42 = []
N43 = []
Force11 = []
Force12 = []
Force13 = []
Force21 = []
Force22 = []
Force23 = []
Force31 = []
Force32 = []
Force33 = []
Force41 = []
Force42 = []
Force43 = []
Force2t = []

for line in fn:
    content = line.split()
    if len(content) > 1:
        if content[0] == 'Disp1':
            for i in range(1, len(content)):
                Disp1.append(float(content[i]))
        if content[0] == 'Force':
            for i in range(1, len(content)):
                Force1.append(float(content[i]))
        if content[0] == 'Disp2':
            for i in range(1, len(content)):
                Disp2.append(float(content[i]))
        if content[0] == 'Force2':
            for i in range(1, len(content)):
                Force2.append(float(content[i]))
        if content[0] == 'N11':
            for i in range(1, len(content)):
                N11.append(float(content[i]))
        if content[0] == 'N12':
            for i in range(1, len(content)):
                N12.append(float(content[i]))
        if content[0] == 'N13':
            for i in range(1, len(content)):
                N13.append(float(content[i]))
        if content[0] == 'N21':
            for i in range(1, len(content)):
                N21.append(float(content[i]))
        if content[0] == 'N22':
            for i in range(1, len(content)):
                N22.append(float(content[i]))
        if content[0] == 'N23':
            for i in range(1, len(content)):
                N23.append(float(content[i]))
        if content[0] == 'N31':
            for i in range(1, len(content)):
                N31.append(float(content[i]))
        if content[0] == 'N32':
            for i in range(1, len(content)):
                N32.append(float(content[i]))
        if content[0] == 'N33':
            for i in range(1, len(content)):
                N33.append(float(content[i]))
        if content[0] == 'N41':
            for i in range(1, len(content)):
                N41.append(float(content[i]))
        if content[0] == 'N42':
            for i in range(1, len(content)):
                N42.append(float(content[i]))
        if content[0] == 'N43':
            for i in range(1, len(content)):
                N43.append(float(content[i]))

length2 = len(N11)
length1 = len(Disp1)

for i in range(0, length1):
    for j in range(1, length2):
        if Disp1[i] >= Disp2[j - 1] and Disp1[i] < Disp2[j]:
            Force11.append((N11[j] - N11[j - 1])/(Disp2[j] - Disp2[j - 1])*(Disp1[i] - Disp2[j - 1]) + N11[j - 1])
            Force12.append((N12[j] - N12[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + N12[j - 1])
            Force13.append((N13[j] - N13[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + N13[j - 1])
            Force21.append((N21[j] - N21[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + N21[j - 1])
            Force22.append((N22[j] - N22[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + N22[j - 1])
            Force23.append((N23[j] - N23[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + N23[j - 1])
            Force31.append((N31[j] - N31[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + N31[j - 1])
            Force32.append((N32[j] - N32[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + N32[j - 1])
            Force33.append((N33[j] - N33[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + N33[j - 1])
            Force41.append((N41[j] - N41[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + N41[j - 1])
            Force42.append((N42[j] - N42[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + N42[j - 1])
            Force43.append((N43[j] - N43[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + N43[j - 1])
            Force2t.append((Force2[j] - Force2[j - 1]) / (Disp2[j] - Disp2[j - 1]) * (Disp1[i] - Disp2[j - 1]) + Force2[j - 1])

print(len(Force11), len(Force2t))

fontpath = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
fontprop = fm.FontProperties(family='Arial', fname=fontpath, size=16)
mpl.rcParams.update({'font.size': 16, 'font.family': 'Arial'})

plt.figure(figsize=(11, 5))
ax1 = plt.subplot(1, 2, 1)
Force2g = []
for i in range(0, length2):
    rel = Force2[i]*1.65
    Force2g.append(rel)
    N12g.append((N12[i] + N22[i]))
    N32g.append((N32[i] + N42[i]))


p1, =plt.plot(Force2g, N12g, color='black', label='Upper Steel Rods', marker='^', markersize=10, markevery=(100, 70))
p2, =plt.plot(Force2g, N32g, color='black', label='Lower Steel Rods', marker='v', markersize=10, markevery=(100, 70))
#plt.plot(Disp2, N11, color='g', label='Right')
plt.grid()
plt.xlabel('Shear Force of Column (kN)', fontproperties=fontprop)
plt.ylabel('Tensile Force of Steel Rods (kN)', fontproperties=fontprop)
plt.legend(bbox_to_anchor=(1.02, 0.23), prop=fontprop)

ForceY = []
ForceISu = []
ForceISl = []

for line in fn2:
    content = line.split()
    if len(content) > 1:
        ForceISu.append(float(content[1])*3)
        ForceISl.append(float(content[2])*3)
        ForceY.append(float(content[3])/1000*1.65)

ax2 = plt.subplot(1, 2, 2)
p3, =plt.plot(ForceY, ForceISu, color='black', label='Upper Stiffener', marker='^', markersize=10, markevery=(40, 30))
p4, =plt.plot(ForceY, ForceISl, color='black', label='Lower Stiffener', marker='v', markersize=10, markevery=(40, 30))
plt.grid()
plt.xlim(0, 200)
plt.xticks([0, 50, 100, 150, 200], fontproperties=fontprop)
plt.xlabel('Shear Force of Column (kN)', fontproperties=fontprop)
plt.ylabel('Tensile Force of Internal Stiffeners (kN)', fontproperties=fontprop)
plt.legend(bbox_to_anchor=(1.02, 0.23), prop=fontprop)

plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)
plt.show()