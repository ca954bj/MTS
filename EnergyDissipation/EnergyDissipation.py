import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import xlrd

fontpath = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
fontprop = fm.FontProperties(family='Arial', fname=fontpath, size=16)
mpl.rcParams.update({'font.size': 16, 'font.family': 'Arial'})

XData = [6, 5, 4, 3, 2]
SX1data = [51.498, 41.008, 30.517, 21.9346, 11.4908]
SY1data = [39.006, 29.755, 21.648, 15.6404, 6.8507]
SX2data = [25.749, 21.935, 16.6893, 12.1108, 6.3419]
SY2data = [23.6516, 16.7848, 10.4053, 6.78, 3.6643]

execfile('/media/chenting/Work/ProgramCode/Tools/LinearRegression.py')

ksx1, asx1 = LinearRegression(XData, SX1data)
ksy1, asy1 = LinearRegression(XData, SY1data)
ksx2, asx2 = LinearRegression(XData, SX2data)
ksy2, asy2 = LinearRegression(XData, SY2data)

SX1fit = map(lambda x: ksx1*x + asx1, XData)
SY1fit = map(lambda x: ksy1*x + asy1, XData)
SX2fit = map(lambda x: ksx2*x + asx2, XData)
SY2fit = map(lambda x: ksy2*x + asy2, XData)

plt.figure(figsize=(6, 5))
ax1 = plt.subplot(1, 1, 1)

p1, = plt.plot(XData, SX1data, color='black', label='SX1', marker='o', markersize=6, linestyle='-')
p2, = plt.plot(XData, SY1data, color='black', label='SY1', marker='^', markersize=6, linestyle='-')
p3, = plt.plot(XData, SX2data, color='black', label='SX2', marker='v', markersize=6, linestyle='-')
p4, = plt.plot(XData, SY2data, color='black', label='SY2', marker='s', markersize=6, linestyle='-')

plt.plot(XData, SX1fit, color='gray', linestyle='--')
plt.plot(XData, SY1fit, color= 'gray', linestyle='--')
plt.plot(XData, SX2fit, color='gray', linestyle='--')
plt.plot(XData, SY2fit, color='gray', linestyle='--')

plt.text(1.8, 20-5, 'C26', fontproperties=fontprop)
plt.text(2.8, 30-5, 'C28', fontproperties=fontprop)
plt.text(3.8, 40-5, 'C30', fontproperties=fontprop)
plt.text(4.8, 50-5, 'C32', fontproperties=fontprop)
plt.text(5.8, 60-5, 'C34', fontproperties=fontprop)

ax1.legend(handles=[p1, p2, p3, p4], loc=1, bbox_to_anchor=(1.04, 0.35), prop=fontprop, frameon=False)
ax1.grid(linestyle='--')
plt.ylim(0, 60)
plt.xlim(1.8, 6.2)
plt.xticks([2, 3, 4, 5, 6], fontproperties=fontprop)
plt.yticks([0, 10, 20, 30, 40, 50, 60], fontproperties=fontprop)
plt.xlabel('Peak Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Energy Dissipation (kN*m)', fontproperties=fontprop)

plt.show()
