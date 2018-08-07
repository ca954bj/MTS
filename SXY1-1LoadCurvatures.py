import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.lines as mlines

SectionMy = 229.192042857143
SectionMu = 255.76575
SectionMyX = [1e-6*i for i in range(0, 30)]

SY1ExpLoadCurvatureData = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SY1-1ExpLoadCurvatureData.txt"

SY1FELoadCurvatureData = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/BeamSectionMomentCurvature.txt"

SX1ExpLoadCurvatureData = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SX1-1ExpLoadCurvatureData.txt"

SX1FELoadCurvatureData = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/BeamSectionMomentCurvature.txt"

fontpath = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
fontprop = fm.FontProperties(family='Arial', fname=fontpath, size=16)
mpl.rcParams.update({'font.size': 16, 'font.family': 'Arial'})
plt.figure(figsize=(11, 5))

FESYx = []
FESYy = []
FESY = open(SY1FELoadCurvatureData)
for line in FESY:
    nums = line.split()
    if len(nums) > 1:
        FESYx.append(float(nums[0]))
        FESYy.append(float(nums[1]))

ExpSYx = []
ExpSYy = []
ExpSY = open(SY1ExpLoadCurvatureData)
for line in ExpSY:
    nums = line.split()
    if len(nums) > 1:
        ExpSYx.append(float(nums[0]))
        ExpSYy.append(float(nums[1])*1.95)
        print(float(nums[1]), float(nums[1])*1.95)

FESXx = []
FESXy = []
FESX = open(SX1FELoadCurvatureData)
for line in FESX:
    nums = line.split()
    if len(nums) > 1:
        FESXx.append(float(nums[0]))
        FESXy.append(float(nums[1]))


ExpSXx = []
ExpSXy = []
ExpSX = open(SX1ExpLoadCurvatureData)
for line in ExpSX:
    nums = line.split()
    if len(nums) > 1:
        ExpSXx.append(float(nums[0]))
        ExpSXy.append(float(nums[1])*1.84)

#Uy1[0:-100]

# ======================= Plot SY1-1 Experimental Data ============
ax1 = plt.subplot(1, 2, 1)
#plt.plot(ExpSYx[0:-2], ExpSYy[0:-2], color='black', linestyle='-', marker='^', label='Experiment', markersize=10, markevery=(26, 10))
#p1 = mlines.Line2D([], [], color='black', linestyle='-', marker='^', markersize=10, label='Experiment')
plt.plot(ExpSYx[0:-2], ExpSYy[0:-2], color='black', linestyle='-')
plt.text(3.1e-5, 281, 'SY1 Experiment')

# ======================= Plot SY1-1 FE Data ==============
#plt.plot(FESYx, FESYy, color='black', linestyle='-', label='Theoretical', marker='o', markersize=10, markevery=(30, 10))
#p2 = mlines.Line2D([], [], color='black', linestyle='-', marker='o', markersize=10, label='Theoretical')
plt.plot(FESYx, FESYy, color='black', linestyle='-')
plt.text(3.7e-5, 243, 'Theoretical')

# ======================= Plot SX1-1 FE Data ============
#plt.plot(ExpSXx, ExpSXy, color='black', linestyle='-', label='Experiment', marker='v', markersize=10, markevery=(26, 10))
#p3 = mlines.Line2D([], [], color='black', linestyle='-', marker='v', markersize=10, label='Experiment')
plt.plot(ExpSXx, ExpSXy, color='black', linestyle='-')
plt.text(1.8e-5, 160, 'SX1 Experiment')

# ======================= Plot legend ==================
#plt.legend(handles=[p1, p2], loc=1, bbox_to_anchor=(0.99, 0.3), frameon=False, prop=fontprop)
plt.plot(SectionMyX, [SectionMu]*len(SectionMyX), linestyle='--')
plt.plot(SectionMyX, [SectionMy]*len(SectionMyX), linestyle='-.')

# Adjust the plot
plt.ylim(0, 320)
plt.xlim(0, 0.00005)
plt.xticks([0, 0.00001, 0.00002, 0.00003, 0.00004, 0.00005], fontproperties=fontprop)
plt.yticks([0, 40, 80, 120, 160, 200, 240, 280, 320], fontproperties=fontprop)
plt.ticklabel_format(style='sci')
a1 = ax1.get_xticks().tolist()
a1[0] = '0'
ax1.set_xticklabels(a1)
plt.xlabel('Curvature (mm$^-$$^1$)', fontproperties=fontprop)
plt.ylabel('Bending Moment (kN*m)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.1, 0.5)

# ==================================================================================================
# Plot SX1-1 Experiment Data
ax2 = plt.subplot(1, 2, 2)
plt.plot(ExpSXx, ExpSXy, color='black', linestyle='-', label='Experiment',  markersize=10, markevery=(1, 1))
p1 = mlines.Line2D([], [], color='black', linestyle='-', markersize=10, label='Experiment')

# Plot SX1-1 FE Data
plt.plot(FESXx, FESXy, color='black', linestyle='--', label='Theoretical', markersize=10, markevery=(40, 35))
p2 = mlines.Line2D([], [], color='black', linestyle='--', markersize=10, label='Theoretical')

# Plot legend
plt.legend(handles=[p1, p2], loc=1, bbox_to_anchor=(0.99, 0.3), frameon=False, prop=fontprop)

# Adjust the plot
plt.grid()
plt.ylim(0, 320)
plt.xlim(0, 0.00001)
plt.xticks([0, 0.0000025, 0.000005, 0.0000075, 0.00001], fontproperties=fontprop)
plt.yticks([0, 40, 80, 120, 160, 200, 240, 280, 320], fontproperties=fontprop)
plt.ticklabel_format(style='sci')
a1 = ax2.get_xticks().tolist()
a1[0] = '0'
ax2.set_xticklabels(a1)
plt.xlabel('Curvature (mm$^-$$^1$)', fontproperties=fontprop)
plt.ylabel('Bending Moment (kN*m)', fontproperties=fontprop)
ax2.yaxis.set_label_coords(-0.1, 0.5)

plt.subplots_adjust(left=0.08, right=0.97, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)

plt.show()

