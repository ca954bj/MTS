import matplotlib.pyplot as plt
execfile("/media/chenting/Work/ProgramCode/Tools/ExcelTools.py")
Straincopied = "226	232	236.7	251	283	545.5	1202"
EqSScopied = "136.466859	195.1322436	217.9	245.1	283.2	348.4	389.1"
Fxcopied = "22.74218518	23.34596001	23.81891696	25.25791363	28.47804605	54.89319476	120.9562238"

Strain = []
EqSS = []
Fx = []

NumberList(Straincopied, Strain)
NumberList(EqSScopied, EqSS)
NumberList(Fxcopied, Fx)

plt.figure(figsize=(6, 6))
ax1 = plt.subplot(1, 1, 1)
plt.plot(Strain, EqSS, color='k', linestyle='-', label='Equivalent Story Shear Force')
plt.show()

