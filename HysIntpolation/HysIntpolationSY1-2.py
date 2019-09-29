import numpy as np

data1 = np.loadtxt('/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/New1213.txt')
data2 = np.loadtxt('/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/HysIntpolation/Beam-CFSSY1-2.txt')

lens = data1.shape[0]
Force = np.zeros((lens, 1))
switch1 = [0]
switchsub = []
subtractset = []
counterp = 0
countern = 0

for i in range(1, lens):
    subtract = data1[i, 1] - data1[i - 1, 1]
    if subtract > 0:
        subtractset.append(0)
        counterp += 1
    else:
        subtractset.append(1)
        countern += 1
    if i > 3:
        if subtractset[-1] == 0 and subtractset[-2] == 1:
            switch1.append(i)
        elif subtractset[-1] == 1 and subtractset[-2] == 0:
            switch1.append(i)

dellist = []
for i in range(1, len(switch1)):
    if switch1[i] - switch1[i - 1] < 10 and i > 10 and i <= 1000:
        if switch1[i-1] not in dellist:
            dellist.append(switch1[i-1])
        if switch1[i] not in dellist:
            dellist.append(switch1[i])
    if switch1[i] - switch1[i - 1] < 100 and i > 1000:
        if switch1[i-1] not in dellist:
            dellist.append(switch1[i-1])
        if switch1[i] not in dellist:
            dellist.append(switch1[i])

switch1.append(87)
switch1.append(102)
switch1.append(150)
switch1.append(1188)
switch1.append(2879)
switch1.append(3342)
switch1 = sorted(switch1)

dellist.append(63)
dellist.append(66)
dellist.append(70)
dellist.append(72)
dellist.append(3025)


for i in range(0, len(dellist)):
    switch1.remove(dellist[i])

print('switch1 = ', switch1)


lens = data2.shape[0]
switch2 = [0]
switchsub = []

for i in range(1, lens - 1):
    if data2[i] - data2[i - 1] > 0 and data2[i + 1] - data2[i] < 0:
        switch2.append(i)
    elif data2[i] - data2[i - 1] < 0 and data2[i + 1] - data2[i] > 0:
        switch2.append(i)

print('switch2 = ', switch2)

print(len(switch1), len(switch2))

for i in range(1, len(switch2)):
    ToBeInt = data2[switch2[i - 1]: switch2[i]]
    ToBeRef = data1[switch1[i - 1]: switch1[i], 1]
    j = 0
    for obj in ToBeInt:
        if obj < data1[switch1[i - 1], 1] and data1[switch1[i - 1], 1] < data1[switch1[i], 1]:
            x1 = data1[switch1[i - 1], 1]
            x2 = data1[switch1[i - 1] + 1, 1]
            y1 = data1[switch1[i - 1], 0]
            y2 = data1[switch1[i - 1] + 1, 0]

        elif obj > data1[switch1[i - 1], 1] and data1[switch1[i - 1], 1] > data1[switch1[i], 1]:
            x1 = data1[switch1[i - 1], 1]
            x2 = data1[switch1[i - 1] + 1, 1]
            y1 = data1[switch1[i - 1], 0]
            y2 = data1[switch1[i - 1] + 1, 0]

        elif obj < data1[switch1[i], 1] and data1[switch1[i - 1], 1] > data1[switch1[i], 1]:
            x1 = data1[switch1[i], 1]
            x2 = data1[switch1[i] - 1, 1]
            y1 = data1[switch1[i], 0]
            y2 = data1[switch1[i] - 1, 0]

        elif obj > data1[switch1[i], 1] and data1[switch1[i - 1], 1] < data1[switch1[i], 1]:
            x1 = data1[switch1[i], 1]
            x2 = data1[switch1[i] - 1, 1]
            y1 = data1[switch1[i], 0]
            y2 = data1[switch1[i] - 1, 0]

        else:
            for k in range(0, len(ToBeRef) - 1):
                if ToBeRef[k] <= obj and ToBeRef[k + 1] >= obj:
                    x1 = data1[switch1[i - 1] + k, 1]
                    x2 = data1[switch1[i - 1] + k + 1, 1]
                    y1 = data1[switch1[i - 1] + k, 0]
                    y2 = data1[switch1[i - 1] + k + 1, 0]
                elif ToBeRef[k] >= obj and ToBeRef[k + 1] <= obj:
                    x1 = data1[switch1[i - 1] + k, 1]
                    x2 = data1[switch1[i - 1] + k + 1, 1]
                    y1 = data1[switch1[i - 1] + k, 0]
                    y2 = data1[switch1[i - 1] + k + 1, 0]


        Force[switch2[i - 1] + j, 0] = y1 + (obj - x1)*(y2 - y1)/(x2 - x1)
        print('i=%d' % i, 'obj=%f' % obj, 'x1 = %f' % x1, 'x2 = %f' % x2, 'y1 = %f' % y1, 'y2 = %f' % y2,
              'Force = %f' % Force[switch2[i - 1] + j, 0])
        j = j + 1

        np.savetxt('/media/chenting/Work/Structural Engineering/Beam-CFSConnection/MTS Data/HysIntpolation/Beam-CFSSY1-2-Load.txt', Force)

