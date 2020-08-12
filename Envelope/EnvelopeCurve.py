execfile('../MTSsetup.py')
import numpy as np
from sympy import *
x = symbols('x')
f1 = Piecewise((4*x, x<=1),((10*x - 4)/(x + 0.5), x>1))
df1 = diff(f1,x)
solx = solve(df1-0.4,x)[0]
soly = f1.subs(x, solx)

f2 = 0.4*(x - solx) + soly
f3 = 4*x

Fx1 = []
Fy1 = []
Fx2 = []
Fy2 = []
Fx3 = []
Fy3 = []
for i in range(0, 100):
	Fx1.append(0.1*i)
	Fy1.append(f1.subs(x, 0.1*i))
	Fx2.append(0.1*i)
	Fy2.append(f2.subs(x, 0.1*i))
	Fx3.append(0.1*i)
	Fy3.append(f3.subs(x, 0.1*i))

# SX1 Data
SX1data = np.loadtxt('SX1EvenlopeDataDense.txt')

# SY1 Data
SY1data = np.loadtxt('SY1EvenlopeDataDense.txt')

# SX2 Data
SX2data = np.loadtxt('SX2EvenlopeData.txt')

# SY2-2 Data
SY2data = np.loadtxt('SY2EvenlopeDataDense.txt')

plt.figure(figsize=(11, 5))
ax1 = plt.subplot(1, 2, 1)
plt.plot(SX1data[:,0], SX1data[:,1]/2, color='k', linestyle='-', label='SX1-2', marker='^', markersize=10, markevery=52)
p1 = mlines.Line2D([], [], color='black', marker='^', markersize=10, label='SX1-2')
plt.plot(SY1data[:,0], SY1data[:,1]/2, color='k', linestyle='-', label='SY1-2', marker='v', markersize=10, markevery=59)
p2 = mlines.Line2D([], [], color='black', marker='v', markersize=10, label='SY1-2')
plt.plot(SX2data[:,0], SX2data[:,1]/2, color='k', linestyle='-', label='SX2-2', marker='*', markersize=10, markevery=20)
p3 = mlines.Line2D([], [], color='black', marker='*', markersize=10, label='SX2-2')
plt.plot(SY2data[:,0], SY2data[:,1]/2, color='k', linestyle='-', label='SY2-2', marker='o', markersize=10, markevery=59)
p4 = mlines.Line2D([], [], color='black', marker='o', markersize=10, label='SY2-2')

plt.legend(handles=[p1, p2, p3, p4], loc=1, bbox_to_anchor=(0.99, 0.35), prop=fontprop)

plt.grid(linestyle='--')
plt.ylim(-250, 250)
plt.xlim(-0.08, 0.08)

plt.xticks([-0.08, -0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08], ['-8', '-6', '-4', '-2', '0', '2', '4', '6', '8'], fontproperties=fontprop)
plt.yticks([-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250], fontproperties=fontprop)

plt.xlabel('Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Shear Force in Column (kN)', fontproperties=fontprop)

ax2 = plt.subplot(1, 2, 2)
plt.plot(Fx1, Fy1, color='k', linestyle='-')
plt.plot(Fx2, Fy2, color='k', linestyle='--')
plt.plot(Fx3, Fy3, color='k', linestyle='--')
plt.ylim(0, 10)
plt.xlim(0, 10)
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [''] * 11, fontproperties=fontprop)
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [''] * 11, fontproperties=fontprop)

plt.text(2.5, 9, 'K', fontproperties=fontprop)
plt.text(6, 9.2, 'K/10', fontproperties=fontprop)

plt.xlabel('Generalized Displacement', fontproperties=fontprop)
plt.ylabel('Generalized Force', fontproperties=fontprop)

plt.subplots_adjust(left=0.1, right=0.98, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)

plt.show()
