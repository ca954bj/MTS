import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
fontpath = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
fontprop = fm.FontProperties(family='Arial', fname=fontpath, size=16)
mpl.rcParams.update({'font.size': 16, 'font.family': 'Arial'})

infile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/FilletWeldForce.txt"

content = open(infile, 'r')
data = []

for j, line in enumerate(content):
    temp = line.split()
    data.append([float(i) for i in temp])
        
for i in range(1, 7):
    for j in range(0, 11):
        if j == 0 or j == 10:
            data[i][j] = data[i][j]/50
        else:
            data[i][j] = data[i][j]/100

plt.figure(figsize=(6, 5))
ax1 = plt.subplot(1, 1, 1)

plt.plot(data[1], data[0], color='black', label='Experiment', linestyle='-', marker='^', markersize=7)
plt.plot(data[2], data[0], color='black', label='Experiment', linestyle='-', marker='o', markersize=7)
plt.plot(data[4], data[0], color='black', label='Experiment', linestyle='--', marker='^', markersize=7)
plt.plot(data[5], data[0], color='black', label='Experiment', linestyle='--', marker='o', markersize=7)

plt.yticks([i for i in range(0, 110, 10)], fontproperties=fontprop)
plt.xticks([float(i)/50*1000 for i in range(-10, 60, 10)], fontproperties=fontprop)

plt.ylim(0, 100)
plt.xlim(-200, 1000)
plt.ylabel('Position (mm)', fontproperties=fontprop)
plt.xlabel('Average Shear Stress (MPa)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.07, 0.5)
plt.grid(linestyle='--')
plt.subplots_adjust(left=0.13, right=0.96, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)

plt.show()
