import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.lines as mlines


S1UFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1UU.txt"

S1MFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1UM.txt"

S1BFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1UD.txt"

S2UFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1DU.txt"
S2MFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1DM.txt"
S2BFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1DD.txt"

T1UFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY1UpperISUpperPoint.txt"
T1DFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY1LowerISUpperPoint.txt"

MTSLoadFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1TimeLoad.txt"

fontpath = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
fontprop = fm.FontProperties(family='Arial', fname=fontpath, size=16)
mpl.rcParams.update({'font.size': 16, 'font.family': 'Arial'})
plt.figure(figsize=(11, 5))

S1UStress = []
S1UStep = []
fn = open(S1UFile, 'r')
for line in fn:
    content = line.split()
    if len(content) > 1:
        S1UStep.append(float(content[0]))
        S1UStress.append(float(content[1]))
fn.close()

S1MStress = []
S1MStep = []
fn = open(S1MFile, 'r')
for line in fn:
    content = line.split()
    if len(content) > 1:
        S1MStep.append(float(content[0]))
        S1MStress.append(float(content[1]))
fn.close()

S1BStress = []
S1BStep = []
fn = open(S1BFile, 'r')
for line in fn:
    content = line.split()
    if len(content) > 1:
        S1BStep.append(float(content[0]))
        S1BStress.append(float(content[1]))
fn.close()

S2UStress = []
S2UStep = []
fn = open(S2UFile, 'r')
for line in fn:
    content = line.split()
    if len(content) > 1:
        S2UStep.append(float(content[0]))
        S2UStress.append(float(content[1]))
fn.close()

S2MStress = []
S2MStep = []
fn = open(S2MFile, 'r')
for line in fn:
    content = line.split()
    if len(content) > 1:
        S2MStep.append(float(content[0]))
        S2MStress.append(float(content[1]))
fn.close()

S2BStress = []
S2BStep = []
fn = open(S2BFile, 'r')
for line in fn:
    content = line.split()
    if len(content) > 1:
        S2BStep.append(float(content[0]))
        S2BStress.append(float(content[1]))
fn.close()

MTSStep = []
MTSForce = []
fn = open(MTSLoadFile, 'r')
for line in fn:
    content = line.split()
    if len(content) > 1:
        MTSStep.append(float(content[0]))
        MTSForce.append(float(content[1]))
fn.close()

### ===================================================================================================================
# ============================= S1U

S1ULength = len(S1UStress)

cstep = S1UStep[0]
Avglist = []
S1UStressg = []
S1UStepg = []
for i in range(0, S1ULength):
    if S1UStep[i] == cstep:
        Avglist.append(S1UStress[i])
        cstep = S1UStep[i]
    else:
        S1UStressg.append(sum(Avglist)/len(Avglist))
        S1UStepg.append(cstep)
        Avglist = []
        cstep = S1UStep[i]

S1UStressg.append(sum(Avglist)/len(Avglist))
S1UStepg.append(cstep)

# ============================= S1M
S1MLength = len(S1MStress)

cstep = S1MStep[0]
Avglist = []
S1MStressg = []
S1MStepg = []
for i in range(0, S1MLength):
    if S1MStep[i] == cstep:
        Avglist.append(S1MStress[i])
        cstep = S1MStep[i]
    else:
        S1MStressg.append(sum(Avglist)/len(Avglist))
        S1MStepg.append(cstep)
        Avglist = []
        cstep = S1MStep[i]

S1MStressg.append(sum(Avglist)/len(Avglist))
S1MStepg.append(cstep)

# ============================= S1B
S1BLength = len(S1BStress)

cstep = S1BStep[0]
Avglist = []
S1BStressg = []
S1BStepg = []
for i in range(0, S1BLength):
    if S1BStep[i] == cstep:
        Avglist.append(S1BStress[i])
        cstep = S1BStep[i]
    else:
        S1BStressg.append(sum(Avglist)/len(Avglist))
        S1BStepg.append(cstep)
        Avglist = []
        cstep = S1BStep[i]

S1BStressg.append(sum(Avglist)/len(Avglist))
S1BStepg.append(cstep)

# ============================= S2U

S2ULength = len(S2UStress)

cstep = S2UStep[0]
Avglist = []
S2UStressg = []
S2UStepg = []
for i in range(0, S2ULength):
    if S2UStep[i] == cstep:
        Avglist.append(S2UStress[i])
        cstep = S2UStep[i]
    else:
        S2UStressg.append(sum(Avglist)/len(Avglist))
        S2UStepg.append(cstep)
        Avglist = []
        cstep = S2UStep[i]

S2UStressg.append(sum(Avglist)/len(Avglist))
S2UStepg.append(cstep)

# ============================= S2M
S2MLength = len(S2MStress)

cstep = S2MStep[0]
Avglist = []
S2MStressg = []
S2MStepg = []
for i in range(0, S2MLength):
    if S2MStep[i] == cstep:
        Avglist.append(S2MStress[i])
        cstep = S2MStep[i]
    else:
        S2MStressg.append(sum(Avglist)/len(Avglist))
        S2MStepg.append(cstep)
        Avglist = []
        cstep = S2MStep[i]

S2MStressg.append(sum(Avglist)/len(Avglist))
S2MStepg.append(cstep)

# ============================= S2B
S2BLength = len(S2BStress)

cstep = S2BStep[0]
Avglist = []
S2BStressg = []
S2BStepg = []
for i in range(0, S2BLength):
    if S2BStep[i] == cstep:
        Avglist.append(S2BStress[i])
        cstep = S2BStep[i]
    else:
        S2BStressg.append(sum(Avglist)/len(Avglist))
        S2BStepg.append(cstep)
        Avglist = []
        cstep = S2BStep[i]

S2BStressg.append(sum(Avglist)/len(Avglist))
S2BStepg.append(cstep)

# ===================================================== Extract Data for SY1 ===========================================
fn = open(T1UFile)
T1Load = []
T1UU = []
T1UM = []
T1UD = []
T1DU = []
T1DM = []
T1DD = []
for line in fn:
    content = line.split()
    if len(content) > 3:
        T1Load.append(content[0])
        T1UU.append(content[1])
        T1UM.append(content[2])
        T1UD.append(content[3])
fn.close()

fn = open(T1DFile)
for line in fn:
    content = line.split()
    if len(content) > 3:
        T1DU.append(content[1])
        T1DM.append(content[2])
        T1DD.append(content[3])
fn.close()

T1Load = [float(i) for i in T1Load[1:-1]]
T1UU = [float(i) for i in T1UU[1:-1]]
T1UM = [float(i) for i in T1UM[1:-1]]
T1UD = [float(i) for i in T1UD[1:-1]]
T1DU = [float(i) for i in T1DU[1:-1]]
T1DM = [float(i) for i in T1DM[1:-1]]
T1DD = [float(i) for i in T1DD[1:-1]]

# ===================================================== Search for Points for SX1-1 ==============================================
Positions = [12.5, 0, -12.5]
LoadLevels = [25, 50, 75, 100]
ForceByLevels = []
IndexByLevels = []
StressForPositions = []

for obj in LoadLevels:
    StressForPositions.append([])
    TempForce = min(MTSForce, key=lambda x: abs(x - obj))
    TempIndex = MTSForce.index(TempForce)
    ForceByLevels.append(TempForce)
    IndexByLevels.append(TempIndex)
    StressForPositions[-1].append(S1UStressg[TempIndex])
    StressForPositions[-1].append(S1MStressg[TempIndex])
    StressForPositions[-1].append(S1BStressg[TempIndex])
    StressForPositions[-1].append(S2UStressg[TempIndex])
    StressForPositions[-1].append(S2MStressg[TempIndex])
    StressForPositions[-1].append(S2BStressg[TempIndex])


print(IndexByLevels)
print(ForceByLevels)
print(StressForPositions)

# ===================================================== Plot Curves ====================================================
# ======= First Plot =============
ax1 = plt.subplot(1, 2, 1)

for i in range(0, len(LoadLevels)):
    plt.plot(StressForPositions[i][0:3], Positions, color='black', linestyle='-', label='S1U', marker='o', markersize=10)
    plt.plot(StressForPositions[i][3:6], Positions, color='black', linestyle='--', label='S1U', marker='o', markersize=10)

#p1 = mlines.Line2D([], [], color='black', marker='^', markersize=10)

plt.xlim(-50, 300)
plt.ylim(-15, 15)
plt.xlabel('Stress (MPa)', fontproperties=fontprop)
plt.ylabel('Position in the Section of Steel Rod (mm)', fontproperties=fontprop)

#legend1 = plt.legend(handles=[p1, p2, p3], loc=1, bbox_to_anchor=(0.25, 1.02), prop=fontprop, frameon=False)
#legend2 = plt.legend(handles=[p4, p5, p6], loc=1, bbox_to_anchor=(0.25, 0.75), prop=fontprop, frameon=False)

#plt.gca().add_artist(legend1)
#plt.gca().add_artist(legend2)
#ax1.yaxis.set_label_coords(-0.1, 0.5)

plt.grid()

# ================================================== Search for Points for SY1-1 ==============================================
Positions = [50, 0, -50]
LoadLevels = [25, 50, 75, 100]
ForceByLevels = []
IndexByLevels = []
StressForPositions = []

for obj in LoadLevels:
    StressForPositions.append([])
    TempForce = min(T1Load, key=lambda x: abs(x - obj))
    TempIndex = T1Load.index(TempForce)
    ForceByLevels.append(TempForce)
    IndexByLevels.append(TempIndex)
    StressForPositions[-1].append(T1UU[TempIndex])
    StressForPositions[-1].append(T1UM[TempIndex])
    StressForPositions[-1].append(T1UD[TempIndex])
    StressForPositions[-1].append(T1DU[TempIndex])
    StressForPositions[-1].append(T1DM[TempIndex])
    StressForPositions[-1].append(T1DD[TempIndex])


print(IndexByLevels)
print(ForceByLevels)
print(StressForPositions)

# ================================================== The second plot for SY1-1
ax2 = plt.subplot(1, 2, 2)

for i in range(0, len(LoadLevels)):
    plt.plot(StressForPositions[i][0:3], Positions, color='black', linestyle='-', label='S1U', marker='o', markersize=10)
    plt.plot(StressForPositions[i][3:6], Positions, color='black', linestyle='--', label='S1U', marker='o', markersize=10)

#p1 = mlines.Line2D([], [], color='black', marker='^', markersize=10)

plt.xlim(-50, 300)
#plt.ylim(-15, 15)
plt.xlabel('Stress (MPa)', fontproperties=fontprop)
plt.ylabel('Position in the Section of Internal Stiffener (mm)', fontproperties=fontprop)
plt.grid()
plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)

plt.show()


