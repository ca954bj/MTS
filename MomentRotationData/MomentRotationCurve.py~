import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.lines as mlines
import numpy as np

fontpath = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
fontprop = fm.FontProperties(family='Arial', fname=fontpath, size=16)
mpl.rcParams.update({'font.size': 16, 'font.family': 'Arial'})

data1 = np.loadtxt("/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MomentRotationData/SX1MomentRotation.txt")
data2 = np.loadtxt("/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MomentRotationData/SY1MomentRotation.txt")

data31 = np.loadtxt("/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MomentRotationData/DispX.out")
data32 = np.loadtxt("/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MomentRotationData/ForceX.out")

data41 = np.loadtxt("/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MomentRotationData/DispY.out")
data42 = np.loadtxt("/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MomentRotationData/ForceY.out")

plt.figure(figsize=(10, 5))

ax1 = plt.subplot(1, 2, 1)
plt.grid()
plt.xlim(-0.015, 0.015)
plt.ylim(-200, 200)
plt.plot(data1[0:-260, 0], data1[0:-260, 1], color='black', label='Experiment')
plt.plot(data31, data32, color='black', linestyle = '--', label='FE model', dashes=[4,4])
plt.xticks([-0.02, -0.01, 0, 0.01, 0.02], fontproperties=fontprop)
plt.yticks([-300, -200, -100, 0, 100, 200, 300], fontproperties=fontprop)
plt.xlabel('Rotation (rad)', fontproperties=fontprop)
plt.ylabel('Bending Moment (kN*m)', fontproperties=fontprop)
plt.legend(bbox_to_anchor=(0.9, 0.2), prop=fontprop)
ax1.yaxis.set_label_coords(-0.15, 0.5)

ax2 = plt.subplot(1, 2, 2)
plt.grid()
plt.xlim(-0.015, 0.015)
plt.ylim(-200, 200)
plt.plot(data2[0:-235, 0], data2[0:-235, 1], color='black', label='Experiment')
plt.plot(data41[0:-40], data42[0:-40], color='black', linestyle = '--', label='FE model', dashes=[4,4])
plt.xticks([-0.02, -0.01, 0, 0.01, 0.02], fontproperties=fontprop)
plt.yticks([-300, -200, -100, 0, 100, 200, 300], fontproperties=fontprop)
plt.xlabel('Rotation (rad)', fontproperties=fontprop)
plt.ylabel('Bending Moment (kN*m)', fontproperties=fontprop)
plt.legend(bbox_to_anchor=(0.9, 0.2), prop=fontprop)
ax1.yaxis.set_label_coords(-0.15, 0.5)

plt.subplots_adjust(left=0.09, right=0.97, wspace=0.25, hspace=0.1, bottom=0.12, top=0.95)
plt.show()
