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
    if j == 0:
        data.append([float(i) for i in temp])
    else:
        data.append([float(i)/1000 for i in temp])

plt.figure(figsize=(6, 5))
ax1 = plt.subplot(1, 1, 1)

plt.plot(data[0], data[1], color='black', label='Experiment', linestyle='-', marker='^', markersize=7)
plt.plot(data[0], data[2], color='black', label='Experiment', linestyle='-', marker='o', markersize=7)
plt.plot(data[0], data[3], color='black', label='Experiment', linestyle='-', marker='v', markersize=7)
plt.plot(data[0], data[4], color='black', label='Experiment', linestyle='--', marker='^', markersize=7)
plt.plot(data[0], data[5], color='black', label='Experiment', linestyle='--', marker='o', markersize=7)
plt.plot(data[0], data[6], color='black', label='Experiment', linestyle='--', marker='v', markersize=7)

plt.xticks([i for i in range(0, 110, 10)], fontproperties=fontprop)
plt.yticks([i for i in range(-10, 60, 10)], fontproperties=fontprop)

plt.xlabel('Position (mm)', fontproperties=fontprop)
plt.ylabel('Force (kN)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.07, 0.5)

plt.subplots_adjust(left=0.12, right=0.96, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)

plt.show()