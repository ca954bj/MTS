execfile("/media/chenting/Work/ProgramCode/Tools/StiffnessMatrixFor3DBeam.py")

import matplotlib.pyplot as plt

filename = "/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/SR1Disp.txt"
NodeSequence = [1, 2, 3, 7, 8, 9, 10, 11, 4, 5, 6]
LengthSequence = [10, 12, 69.33333, 69.33333, 69.33333, 69.33333, 69.33333, 69.33333, 12, 10]

Dx = np.loadtxt(filename, usecols=tuple(range(1, 12)))
Dy = np.loadtxt(filename, usecols=tuple(range(12, 23)))
Dz = np.loadtxt(filename, usecols=tuple(range(23, 34)))
Rx = np.loadtxt(filename, usecols=tuple(range(34, 45)))
Ry = np.loadtxt(filename, usecols=tuple(range(45, 56)))
Rz = np.loadtxt(filename, usecols=tuple(range(56, 67)))

Fx = []
Fy = []
Mz = []


for i in range(0, Dx.shape[0]):
  Fx.append([])
  Fy.append([])
  Mz.append([])


ShearForce = np.loadtxt(filename, usecols=(67,))

for i in range(0, len(NodeSequence) - 1):
  U11 = Dx[:, NodeSequence[i] - 1]
  U12 = Dx[:, NodeSequence[i + 1] - 1]
  U21 = Dy[:, NodeSequence[i] - 1]
  U22 = Dy[:, NodeSequence[i + 1] - 1]
  U31 = Dz[:, NodeSequence[i] - 1]
  U32 = Dz[:, NodeSequence[i + 1] - 1]

  U41 = Rx[:, NodeSequence[i] - 1]
  U42 = Rx[:, NodeSequence[i + 1] - 1]
  U51 = Ry[:, NodeSequence[i] - 1]
  U52 = Ry[:, NodeSequence[i + 1] - 1]
  U61 = Rz[:, NodeSequence[i] - 1]
  U62 = Rz[:, NodeSequence[i + 1] - 1]

  DispVec = np.vstack((U11, U21, U31, U41, U51, U61, U12, U22, U32, U42, U52, U62))
  L = float(LengthSequence[i])/1000
  r = 12.5/1000
  I = 0.25*np.pi*r**4
  K = StiffnessMatrix3DBeam(L, 205000000000, 205000000000.0/2.0/(1 + 0.3), np.pi*r*r, I, I, 2*I)
  ForceVec = np.dot(K, DispVec)

  for i in range(0, Dx.shape[0]):
    Fx[i].append(-ForceVec[0, i])
    Fx[i].append(ForceVec[6, i])
    Fy[i].append(ForceVec[1, i])
    Fy[i].append(ForceVec[7, i])
    Mz[i].append(ForceVec[5, i])
    Mz[i].append(ForceVec[11, i])

print(Fx[-1])

AccumulatedDistance = [0]
for i, obj in enumerate(LengthSequence):
  if i != len(LengthSequence) - 1:
    AccumulatedDistance.append(AccumulatedDistance[-1] + LengthSequence[i])
    AccumulatedDistance.append(AccumulatedDistance[-1])
  else:
    AccumulatedDistance.append(AccumulatedDistance[-1] + LengthSequence[i])

#plt.plot(AccumulatedDistance[4:-4], Fx[-1][4:-4])
plt.plot(AccumulatedDistance[4:-4], Mz[-1][4:-4])
plt.show()








