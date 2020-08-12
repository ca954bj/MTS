execfile("/media/chenting/Work/ProgramCode/Tools/Interpolation.py")
execfile('MTSsetup2.py')

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 120kN -> 1.194411
# 90kN -> 1.1223716
# 60kN -> 1.0754854

# ================================= Input Location ================================

# Internal Stiffener 120kN
Infile2 = '/media/chenting/Work/ProgramCode/AbaqusInpScript2/SY2ISSYN2.txt'
Infile1 = '/media/chenting/Work/ProgramCode/AbaqusInpScript2/SY2ISSYN1.txt'

# Internal Stiffener 90kN
Infile4 = '/media/chenting/Work/ProgramCode/AbaqusInpScript2/SY2ISSYN4.txt'
Infile3 = '/media/chenting/Work/ProgramCode/AbaqusInpScript2/SY2ISSYN3.txt'

# Internal Stiffener 60kN
Infile6 = '/media/chenting/Work/ProgramCode/AbaqusInpScript2/SY2ISSYN6.txt'
Infile5 = '/media/chenting/Work/ProgramCode/AbaqusInpScript2/SY2ISSYN5.txt'

# SteelRod 120kN
Infile7 = '/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX2SRYNZP.txt'

# ================================= Output Location ===============================
# Internal Stiffener 120kN
Outfile1 = '/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY2ISSYN120.txt'

# Internal Stiffener 90kN
Outfile2 = '/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY2ISSYN90.txt'

# Internal Stiffener 60kN
Outfile3 = '/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY2ISSYN60.txt'

f1 = open(Infile1, 'r')
f2 = open(Infile2, 'r')
f3 = open(Infile3, 'r')
f4 = open(Infile4, 'r')
f5 = open(Infile5, 'r')
f6 = open(Infile6, 'r')
f7 = open(Infile7, 'r')

# ======================== Step Interpolation for SX1 ===============================
# for 120kN
step11 = 1.177581
step12 = 1.208791
steprequired1 = 1.194411

# for 90kN
step21 = 1.111052
step22 = 1.127492
steprequired2 = 1.1223716

# for 60kN
step31 = 1.070235
step32 = 1.076009
steprequired3 = 1.0754854


# ==================== Tensile side -> Compressive side =================================
# ========================================= Internal Stiffeners =========================

# for 120kN
X1 = []
Fx11 = []
Mz11 = []
LineCounter = 0

for line in f1:
    content = line.split()
    LineCounter += 1
    if LineCounter == 1:
        for obj in content:
            X1.append(float(obj))
    if LineCounter == 2:
        for obj in content:
            Fx11.append(float(obj))
    if LineCounter == 3:
        for obj in content:
            Mz11.append(float(obj))

Fx12 = []
Mz12 = []
LineCounter = 0

for line in f2:
    content = line.split()
    LineCounter += 1
    if LineCounter == 2:
        for obj in content:
            Fx12.append(float(obj))
    if LineCounter == 3:
        for obj in content:
            Mz12.append(float(obj))

Fx1 = []
Mz1 = []

for i, obj in enumerate(X1):
    X1[i] = obj + 190

for i, obj in enumerate(Fx11):
    Fx1.append(LinearInterpolation2D(step11, obj, step12, Fx12[i], steprequired1)/1000.0)

for i, obj in enumerate(Mz11):
    Mz1.append(-LinearInterpolation2D(step11, obj, step12, Mz12[i], steprequired1)/1000000.0)

ofile = open(Outfile1, 'w')
for i, obj in enumerate(X1):
    ofile.write("%d " % obj)
ofile.write('\n')
for obj in Fx1:
    ofile.write("%f " % obj)
ofile.write('\n')
for obj in Mz1:
    ofile.write("%f " % obj)
ofile.close()

# for 90kN
X2 = []
Fx21 = []
Mz21 = []
LineCounter = 0

for line in f3:
    content = line.split()
    LineCounter += 1
    if LineCounter == 1:
        for obj in content:
            X2.append(float(obj))
    if LineCounter == 2:
        for obj in content:
            Fx21.append(float(obj))
    if LineCounter == 3:
        for obj in content:
            Mz21.append(float(obj))

Fx22 = []
Mz22 = []
LineCounter = 0

for line in f4:
    content = line.split()
    LineCounter += 1
    if LineCounter == 2:
        for obj in content:
            Fx22.append(float(obj))
    if LineCounter == 3:
        for obj in content:
            Mz22.append(float(obj))

Fx2 = []
Mz2 = []

for i, obj in enumerate(X2):
    X2[i] = obj + 190

for i, obj in enumerate(Fx21):
    Fx2.append(LinearInterpolation2D(step21, obj, step22, Fx22[i], steprequired2)/1000.0)

for i, obj in enumerate(Mz21):
    Mz2.append(-LinearInterpolation2D(step21, obj, step22, Mz22[i], steprequired2)/1000000.0)

ofile = open(Outfile2, 'w')
for i, obj in enumerate(X2):
    ofile.write("%d " % obj)
ofile.write('\n')
for obj in Fx2:
    ofile.write("%f " % obj)
ofile.write('\n')
for obj in Mz2:
    ofile.write("%f " % obj)
ofile.close()

# for 60kN
X3 = []
Fx31 = []
Mz31 = []
LineCounter = 0

for line in f5:
    content = line.split()
    LineCounter += 1
    if LineCounter == 1:
        for obj in content:
            X3.append(float(obj))
    if LineCounter == 2:
        for obj in content:
            Fx31.append(float(obj))
    if LineCounter == 3:
        for obj in content:
            Mz31.append(float(obj))

Fx32 = []
Mz32 = []
LineCounter = 0

for line in f6:
    content = line.split()
    LineCounter += 1
    if LineCounter == 2:
        for obj in content:
            Fx32.append(float(obj))
    if LineCounter == 3:
        for obj in content:
            Mz32.append(float(obj))

Fx3 = []
Mz3 = []

for i, obj in enumerate(X3):
    X3[i] = obj + 190

for i, obj in enumerate(Fx31):
    Fx3.append(LinearInterpolation2D(step31, obj, step32, Fx32[i], steprequired3)/1000.0)

for i, obj in enumerate(Mz31):
    Mz3.append(-LinearInterpolation2D(step31, obj, step32, Mz32[i], steprequired3)/1000000.0)

ofile = open(Outfile3, 'w')
for i, obj in enumerate(X3):
    ofile.write("%d " % obj)
ofile.write('\n')
for obj in Fx3:
    ofile.write("%f " % obj)
ofile.write('\n')
for obj in Mz3:
    ofile.write("%f " % obj)
ofile.close()

del X3[5]
del Fx3[5]
del Mz3[5]

del X2[5]
del Fx2[5]
del Mz2[5]

del X1[5]
del Fx1[5]
del Mz1[5]

# ============================== Steel Rods =================================
X7 = []
Fx7 = []
Mz7 = []
LineCounter = 0

for line in f7:
    content = line.split()
    LineCounter += 1
    if LineCounter == 1:
        for obj in content:
            X7.append(float(obj) - 230.0)
    if LineCounter == 2:
        for obj in content:
            Fx7.append(float(obj)/1000.0*2)
    if LineCounter == 3:
        for obj in content:
            Mz7.append(-float(obj)/1000000.0*2)

Fx7.reverse()
Mz7.reverse()

def fitfunction(x, a, b, c, d, e, f, g):
    return a*x**6 + b*x**5 + c*x**4 + d*x**3 + e*x**2 + f*x + g

# ========================================= Plot Figures ======================================

plt.figure(figsize=(11, 5))
plt.subplot(1, 2, 1)
plt.plot(X1, Fx1, 'ro', color='black')
plt.plot(X7, Fx7, color='black')
plt.grid()
plt.ylim(0, 500)
plt.xlim(-250, 250)
plt.xticks([-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250], fontproperties=fontprop)
plt.xlabel('Position in Stiffened Member (mm)', fontproperties=fontprop)
plt.ylabel('Axial Load (kN)', fontproperties=fontprop)
#plt.yticks([0, 30, 60, 90, 120, 150, 180], fontproperties=fontprop)

plt.subplot(1, 2, 2)

plt.plot(X7, Mz7, color='black', linestyle='--')

popt1, pcov1 = curve_fit(fitfunction, X1, Mz1)
plt.plot(X1, map(lambda x: fitfunction(x, *popt1), X1), color='black')
popt2, pcov2 = curve_fit(fitfunction, X2, Mz2)
plt.plot(X2, map(lambda x: fitfunction(x, *popt2), X2), color='black')
popt3, pcov3 = curve_fit(fitfunction, X3, Mz3)
plt.plot(X3, map(lambda x: fitfunction(x, *popt3), X3), color='black')

plt.grid()
plt.ylim(-12, 2)
plt.xlim(-250, 250)
plt.xticks([-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250], fontproperties=fontprop)
plt.xlabel('Position in Stiffened Member (mm)', fontproperties=fontprop)
plt.ylabel('Bending Moment (kN*m)', fontproperties=fontprop)
#plt.yticks([0, 30, 60, 90, 120, 150, 180], fontproperties=fontprop)


plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)
plt.show()

