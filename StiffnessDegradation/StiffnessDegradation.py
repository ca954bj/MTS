execfile('../MTSsetup.py')

# SX1-2 Data
ShearSX1 = [0.003652, 0.004889, 0.0074, 0.009942, 0.01496, 0.01996, 0.02995, 0.03995, 0.04997, 0.05998]
StiffnessSX1 = [18632.9288, 17602.3301, 15353.6797, 14050.9595, 13812.3843, 13920.6861, 13630.5602, 12625.8098, 11778.0358, 11446.9964]

# SY1-2 Data
ShearSY1 = [0.003672, 0.004904, 0.007409, 0.009951, 0.01496, 0.01996, 0.02995, 0.03998, 0.04998, 0.05791]
StiffnessSY1 = [15981.36, 15098.41, 12978.95, 11692.11, 11240.38, 10910.8, 10410.89, 9964.724, 9774.227, 9178.26]

# SX2-2 Data
ShearSX2 = [0.003685, 0.004915, 0.007416, 0.009897, 0.01497, 0.019966, 0.029983, 0.039981, 0.04998, 0.05998]
StiffnessSX2 = [13890.91396, 12283.75112, 12030.77844, 11141.22642, 9913.48702, 9698.736756, 8664.884484, 8222.449358, 8152.470079, 7549.437557]

# SY2-2 Data
ShearSY2 = [0.003706, 0.004937, 0.007445, 0.009972, 0.014979, 0.019977, 0.029977, 0.039974, 0.049973, 0.059973]
StiffnessSY2 = [9452.738695, 8378.192191, 8032.558236, 7492.523096, 7087.205409, 6840.853029, 6559.598508, 6389.409985, 6489.711894, 6002.245332]

plt.figure(figsize=(8, 6))

plt.plot(ShearSX1, StiffnessSX1, color='k', linestyle='-', label='SX1', marker='^', markersize=10)
p1 = mlines.Line2D([], [], color='black', marker='^', markersize=10, label='SX1')
plt.plot(ShearSY1, StiffnessSY1, color='k', linestyle='-', label='SY1', marker='v', markersize=10)
p2 = mlines.Line2D([], [], color='black', marker='v', markersize=10, label='SY1')
plt.plot(ShearSX2, StiffnessSX2, color='k', linestyle='-', label='SX2', marker='*', markersize=10)
p3 = mlines.Line2D([], [], color='black', marker='*', markersize=10, label='SX2')
plt.plot(ShearSY2, StiffnessSY2, color='k', linestyle='-', label='SY2', marker='o', markersize=10)
p4 = mlines.Line2D([], [], color='black', marker='o', markersize=10, label='SY2')

plt.grid(linestyle='--')
plt.ylim(0, 20000)
plt.xlim(0, 0.065)

plt.xticks([0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06], ['0', '1', '2', '3', '4', '5', '6'], fontproperties=fontprop)
plt.yticks([0, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000], fontproperties=fontprop)

plt.xlabel('Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Shear Stiffness (kN/rad)', fontproperties=fontprop)

plt.legend(handles=[p1, p2, p3, p4], loc=1, bbox_to_anchor=(0.99, 0.99), prop=fontprop)
plt.subplots_adjust(left=0.15, right=0.98, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)

plt.show()
