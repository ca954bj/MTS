execfile("/media/chenting/Work/ProgramCode/Tools/Interpolation.py")
execfile('MTSsetup2.py')

import matplotlib.pyplot as plt

# Input Location
Infile2 = '/media/chenting/Work/ProgramCode/AbaqusInpScript2/SY1ISSYN2.txt'
Infile1 = '/media/chenting/Work/ProgramCode/AbaqusInpScript2/SY1ISSYN1.txt'
Infile3 = '/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1SRYNZP.txt'

# Output Location
Outfile = '/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY1ISSYN.txt'

f1 = open(Infile1, 'r')
f2 = open(Infile2, 'r')
f3 = open(Infile3, 'r')

# Step Interpolation for SX1
step1 = 1.329641
step2 = 1.34966
steprequired = 1.34093
# 120kN -> 1.34093

# ========================================= Internal Stiffeners =========================
X = []
Fx1 = []
Mz1 = []
LineCounter = 0

for line in f1:
    content = line.split()
    LineCounter += 1
    if LineCounter == 1:
        for obj in content:
            X.append(float(obj))
    if LineCounter == 2:
        for obj in content:
            Fx1.append(float(obj))
    if LineCounter == 3:
        for obj in content:
            Mz1.append(float(obj))

Fx2 = []
Mz2 = []
LineCounter = 0

for line in f2:
    content = line.split()
    LineCounter += 1
    if LineCounter == 2:
        for obj in content:
            Fx2.append(float(obj))
    if LineCounter == 3:
        for obj in content:
            Mz2.append(float(obj))

Fx = []
Mz = []

for i, obj in enumerate(X):
    X[i] = obj + 190

for i, obj in enumerate(Fx1):
    Fx.append(LinearInterpolation2D(step1, obj, step2, Fx2[i], steprequired)/1000.0)

for i, obj in enumerate(Mz1):
    Mz.append(LinearInterpolation2D(step1, obj, step2, Mz2[i], steprequired)/1000000.0)

ofile = open(Outfile, 'w')
for i, obj in enumerate(X):
    ofile.write("%d " % obj)
ofile.write('\n')
for obj in Fx:
    ofile.write("%f " % obj)
ofile.write('\n')
for obj in Mz:
    ofile.write("%f " % obj)
ofile.close()

X3 = []
Fx3 = []
Mz3 = []
LineCounter = 0

# ============================== Steel Rods =================================
for line in f3:
    content = line.split()
    LineCounter += 1
    if LineCounter == 1:
        for obj in content:
            X3.append(float(obj) - 198.0)
    if LineCounter == 2:
        for obj in content:
            Fx3.append(float(obj)/1000.0*2)
    if LineCounter == 3:
        for obj in content:
            Mz3.append(float(obj)/1000000.0*2)

# ========================================= Plot Figures ======================================

plt.figure(figsize=(11, 5))
plt.subplot(1, 2, 1)
plt.plot(X, Fx)
plt.plot(X3, Fx3)
plt.grid()
plt.ylim(0, 500)
plt.xlim(-250, 250)
plt.xticks([-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250], fontproperties=fontprop)
#plt.yticks([0, 30, 60, 90, 120, 150, 180], fontproperties=fontprop)

plt.subplot(1, 2, 2)
plt.plot(X, Mz)
plt.plot(X3,Mz3)
plt.grid()
plt.ylim(-5, 20)
plt.xlim(-250, 250)
plt.xticks([-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250], fontproperties=fontprop)
#plt.yticks([0, 30, 60, 90, 120, 150, 180], fontproperties=fontprop)


plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)
plt.show()