import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.lines as mlines


S1UFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SteelRodStress1u.txt"

S1MFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SteelRodStress1m.txt"

S1BFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SteelRodStress1b.txt"

S2UFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/NB1.txt"
S2MFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/NB2.txt"
S2BFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/NB3.txt"

T1UFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY1UpperISUpperPoint.txt"
T1DFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY1LowerISUpperPoint.txt"

MTSLoadFile = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SteelRodStressMTSForce.txt"

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
        MTSForce.append(float(content[1])/1000)
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

# ===================================================== Plot Curves ====================================================
# ======= First Plot =============
ax1 = plt.subplot(1, 2, 1)

plt.plot(MTSForce, S1UStressg, color='black', linestyle='-', label='S1U', marker='^', markersize=10, markevery=(325, 400))
p1 = mlines.Line2D([], [], color='black', marker='^', markersize=10)

plt.plot(MTSForce, S1MStressg, color='black', linestyle='-', label='S1M', marker='v', markersize=10, markevery=(325, 400))
p2 = mlines.Line2D([], [], color='black', marker='v', markersize=10)

plt.plot(MTSForce, S1BStressg, color='black', linestyle='-', label='S1B', marker='o', markersize=10, markevery=(325, 400))
p3 = mlines.Line2D([], [], color='black', marker='o', markersize=10)

for i in range(162, 327):
    S2UStressg[i] = S2UStressg[161] + S1UStressg[i] - S1UStressg[161]
    S2MStressg[i] = S2MStressg[161] + S1MStressg[i] - S1MStressg[161]
    S2BStressg[i] = S2BStressg[161] + S1BStressg[i] - S1BStressg[161]

plt.plot(MTSForce, S2UStressg, color='black', linestyle='--', label='S2U', dashes=(10, 10))
p4 = mlines.Line2D([], [], color='black', linestyle='--')

dash2 = plt.plot(MTSForce, S2MStressg, color='black', linestyle='--', label='S2M')
dash2[0].set_dashes([10, 6, 3, 6])
p5 = mlines.Line2D([], [], color='black', linestyle='-.')

dash3 = plt.plot(MTSForce, S2BStressg, color='black', linestyle=':', label='S2B')
dash3[0].set_dashes([3, 5, 3, 5])
p6 = mlines.Line2D([], [], color='black', linestyle=':')

plt.xlim(0, 140)
plt.ylim(-50, 400)
plt.xlabel('MTS Load (kN)', fontproperties=fontprop)
plt.ylabel('Stress of the Steel Rod (MPa)', fontproperties=fontprop)

legend1 = plt.legend(handles=[p1, p2, p3], loc=1, bbox_to_anchor=(0.25, 1.02), prop=fontprop, frameon=False)
legend2 = plt.legend(handles=[p4, p5, p6], loc=1, bbox_to_anchor=(0.25, 0.75), prop=fontprop, frameon=False)

plt.gca().add_artist(legend1)
plt.gca().add_artist(legend2)
ax1.yaxis.set_label_coords(-0.1, 0.5)

plt.grid()

# ================================================== The second plot for SY1-1
ax2 = plt.subplot(1, 2, 2)
plt.plot(T1Load[1:-1], T1UU[1:-1], color='black', linestyle='-', label='S1U', marker='v', markersize=10, markevery=(20, 20))
p1 = mlines.Line2D([], [], color='black', marker='^', markersize=10)

plt.plot(T1Load[1:-1], T1UM[1:-1], color='black', linestyle='-', label='S1M', marker='o', markersize=10, markevery=(20, 20))
p2 = mlines.Line2D([], [], color='black', marker='v', markersize=10)

plt.plot(T1Load[1:-1], T1UD[1:-1], color='black', linestyle='-', label='S1B', marker='^', markersize=10, markevery=(20, 20))
p3 = mlines.Line2D([], [], color='black', marker='o', markersize=10)

plt.plot(T1Load[1:-1], T1DU[1:-1], color='black', linestyle=':', label='S1U')
p4 = mlines.Line2D([], [], color='black', marker='^', markersize=10)

plt.plot(T1Load[1:-1], T1DM[1:-1], color='black', linestyle='-.', label='S1M')
p5 = mlines.Line2D([], [], color='black', marker='v', markersize=10)

plt.plot(T1Load[1:-1], T1DD[1:-1], color='black', linestyle='--', label='S1B')
p6 = mlines.Line2D([], [], color='black', marker='o', markersize=10)

plt.subplots_adjust(left=0.08, right=0.97, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)
plt.grid()
plt.xlim(0, 140)
plt.ylim(-50, 400)
plt.xlabel('MTS Load (kN)', fontproperties=fontprop)
plt.ylabel('Stress of the Internal Stiffener (MPa)', fontproperties=fontprop)

plt.show()


