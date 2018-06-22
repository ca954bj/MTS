# ======= This tool is for computing the stress-strain curve for concrete confined by rectangular steel tube ============
from sympy import *

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.lines as mlines

filepath = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/ConcreteStressStrain.txt"

# ================================= Compressive strength of the concrete ====================================
fc_ = 41

# ================================= Young's Modulus of the Concrete =========================================
Ec = 34500

# ================================= Dimensions of the steel tube ============================================
D = 440
B = 220
t = 12

# ================================= Standard yield stress of steel and concrete =============================
fy = 345
fck = 33.5

# =================================== Range of Strain =======================================================
epstart = 0
epend = 0.05
interval = 0.0001

# ================ Computation Begin ============================================

epco = 4.26*fc_/(Ec*fc_**0.25)
As = 4*t*(B-t)
Ac = (B-2*t)**2
alpha = As/Ac
cosi = alpha*fy/fck
if cosi <= 3.0:
    beta = fc_**0.1/(1.35*(1+cosi)**0.5)
else:
    beta = fc_**0.1/(1.35*(1+cosi)**0.5*(cosi-2)**2)
sig0 = (1 + (-0.0135*cosi**2 + 0.1*cosi)*(24.0/fc_)**0.45)*fc_
ep0 = epco + (1330 + 760.0*(fc_/24 - 1))*cosi**0.2
epcc = 1300 + 12.5*fc_

sig, ep = symbols('sig, ep')

x = ep/ep0
eta = 1.6 + 1.5/x

stress = Piecewise((2*x - x**2, ep <= ep0), (x/(beta*abs(x - 1)**eta + x), ep > ep0))*sig0
print(stress)

# ================================ Write to file ========================================
file = open(filepath, 'w')
file.write('0, 0\n')
t = interval
xdataset = [0]
ydataset = [0]
while(t <= epend):
    ydata = stress.evalf(subs={ep: t})
    xdataset.append(t)
    ydataset.append(ydata)
    file.write('%f, %f\n' % (t, ydata))
    t = t + interval

file.close()

# ================================= Properties of Steel Material ==========================
Sx = [0]
Sy = [0]
Sinterval = 0.1e-3
fy = 345.0
t = Sinterval
while(t <= 1e-2):
    Sx.append(t)
    if t <= fy/205000:
        Sy.append(205000*t)
    else:
        Sy.append(fy + 4100*(t - fy/205000))
    t = t + Sinterval

# ================================= Plot the curve ======================================

fontpath = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
fontprop = fm.FontProperties(family='Arial', fname=fontpath, size=18)
mpl.rcParams.update({'font.size': 18, 'font.family': 'Arial'})

plt.figure(figsize=(11, 5))
ax1 = plt.subplot(1, 2, 2)
plt.grid()
p5, = plt.plot(xdataset, ydataset, color = 'black')
plt.legend(handles=[p5], loc=1, bbox_to_anchor=(0.99, 0.3), prop=fontprop, frameon=False)
plt.xlabel('Strain', fontproperties=fontprop)
plt.ylabel('Stress (MPa)', fontproperties=fontprop)
plt.xlim(0, 0.03)
plt.xticks([0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03])

a1 = ax1.get_xticks().tolist()
a1[0] = '0'
a1[1] = '0.5%'
a1[2] = '1.0%'
a1[3] = '1.5%'
a1[4] = '2.0%'
a1[5] = '2.5%'
a1[6] = '3.0%'
ax1.set_xticklabels(a1)

ax2 = plt.subplot(1, 2, 1)
plt.grid()
p4, = plt.plot(Sx, Sy, color = 'black')
plt.legend(handles=[p4], loc=1, bbox_to_anchor=(0.99, 0.3), prop=fontprop, frameon=False)
plt.xlabel('Strain', fontproperties=fontprop)
plt.ylabel('Stress (MPa)', fontproperties=fontprop)
plt.xlim(0, 0.01)
plt.xticks([0, 0.002, 0.004, 0.006, 0.008, 0.01])
a2 = ax2.get_xticks().tolist()
a2[0] = '0'
a2[1] = '0.2%'
a2[2] = '0.4%'
a2[3] = '0.6%'
a2[4] = '0.8%'
a2[5] = '1.0%'
ax2.set_xticklabels(a2)

plt.subplots_adjust(left=0.08, right=0.97, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)

flist = [f.name for f in mpl.font_manager.fontManager.ttflist]
print(flist)

plt.show()
