from mpmath import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontpath = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
fontprop = fm.FontProperties(family='Arial', fname=fontpath, size=16)
mpl.rcParams.update({'font.size': 16, 'font.family': 'Arial'})

kx = 1.07e5
ky = 3.29e4

Fyx = 7.88e2
Fyy = 5.07e2

dataxx = []
dataxy = []
for i in range(1, 300):
	x = 0.0001*i
	dataxx.append(x)
	if kx*x < Fyx:
		dataxy.append(kx*x)
	else:
		dataxy.append(Fyx + 0.01*kx*(x - Fyx/kx))
		
datayx = []
datayy = []
for i in range(1, 300):
	x = 0.0001*i
	datayx.append(x)
	if ky*x < Fyy:
		datayy.append(ky*x)
	else:
		datayy.append(Fyy + 0.01*ky*(x - Fyy/ky))
		
plt.figure(figsize=(11, 5))

ax1 = plt.subplot(1, 2, 1)

p1, = plt.plot(dataxx, dataxy, color = 'black', label='SX1-2 & SX2-2', marker='^', markersize=10, markevery=(250, 600))
p5, = plt.plot(datayx, datayy, color = 'black', label='SY1-2 & SY2-2', marker='o', markersize=10, markevery=(250, 600))
plt.legend(handles=[p1, p5], loc=1, bbox_to_anchor=(0.99, 0.3), prop=fontprop)

plt.grid(linestyle='--')
plt.ylim(0, 1000)
plt.xlim(0, 0.03)
plt.xticks([0, 0.01, 0.02, 0.03], fontproperties=fontprop)
plt.yticks([0, 200, 400, 600, 800, 1000], fontproperties=fontprop)
#plt.xlabel('Curvature (mm$^-$$^1$)', fontproperties=fontprop)
#plt.ylabel('Moment (kN*m)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.1, 0.5)

plt.show()
