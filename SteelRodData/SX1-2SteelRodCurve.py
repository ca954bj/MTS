import matplotlib.pyplot as plt
execfile("/media/chenting/Work/ProgramCode/Tools/ExcelTools.py")
Straincopied = "226	232	236.7	251	283	545.5	1202"
EqSScopied = "136.466859	195.1322436	217.9	245.1	283.2	348.4	389.1"
Fxcopied = "22.74218518	23.34596001	23.81891696	25.25791363	28.47804605	54.89319476	120.9562238"

BeamStrainCopied = "0.0446	0.0565	0.0838	0.0923	0.1093	0.1332	0.169	0.2113	0.2707	0.3091"
LoadForBeamCopied = "125	150.6	200.7	219.5	244.5	284.6	348.4	389.2	423.5	440.3"

Strain = []
EqSS = []
Fx = []

BeamStrain = []
LoadForBeam = []

NumberList(Straincopied, Strain)
NumberList(EqSScopied, EqSS)
NumberList(Fxcopied, Fx)

NumberList(BeamStrainCopied, BeamStrain)
NumberList(LoadForBeamCopied, LoadForBeam)

plt.figure(figsize=(6, 6))
ax1 = plt.subplot(1, 1, 1)
plt.plot(Strain, EqSS, color='k', linestyle='-', label='Threaded Steel Rod')
plt.plot(BeamStrain, LoadForBeam, color='k', linestyle='-', label='Beam End')
plt.show()

