execfile('../MTSsetup.py')

# SX1-2 Data
ShearSX1 = [0.003652, 0.004889, 0.0074, 0.009942, 0.01496, 0.01996, 0.02995, 0.03995, 0.04997, 0.05998]
StiffnessSX1 = [33683.63587, 30960.92708, 27209.31807, 21957.11265, 15347.82609, 12806.31421, 10966.77242, 9455.501314, 8198.919352, 7141.180416]

# SY1-2 Data
ShearSY1 = [0.003672, 0.004904, 0.007409, 0.009951, 0.01496, 0.01996, 0.02995, 0.03998, 0.04998, 0.05791]
StiffnessSY1 = [25244.71711, 22938.11805, 21344.67396, 19893.44592, 15741.97861, 13003.50701, 10160.18688, 9149.574787, 8117.246899, 5910.594622]

# SX2-2 Data
ShearSX2 = [0.003683, 0.004904, 0.007403, 0.009949, 0.01497, 0.01995, 0.02968, 0.03998, 0.04998, 0.05998]
StiffnessSX2 = [19024.55569, 17879.99185, 15339.45202, 13332.66149, 8794.255177, 6911.322645, 5534.696614, 4563.531766, 3855.542217, 3317.772591]

# SY2-2 Data
ShearSY2 = [0.003696, 0.004937, 0.007437, 0.009917, 0.01498, 0.01998, 0.02997, 0.03997, 0.04997, 0.05997]
StiffnessSY2 = [15952.44529, 13636.08748, 12523.85432, 10019.11853, 7656.875834, 6601.601602, 6026.688907, 5437.828371, 4805.88353, 4077.038519]

plt.figure(figsize=(8, 6))

plt.plot(ShearSX1, StiffnessSX1, color='k', linestyle='-', label='SX1-2', marker='^', markersize=10)
p1 = mlines.Line2D([], [], color='black', marker='^', markersize=10, label='SX1-2')
plt.plot(ShearSY1, StiffnessSY1, color='k', linestyle='-', label='SY1-2', marker='v', markersize=10)
p2 = mlines.Line2D([], [], color='black', marker='v', markersize=10, label='SY1-2')
plt.plot(ShearSX2, StiffnessSX2, color='k', linestyle='-', label='SX2-2', marker='*', markersize=10)
p3 = mlines.Line2D([], [], color='black', marker='*', markersize=10, label='SX2-2')
plt.plot(ShearSY2, StiffnessSY2, color='k', linestyle='-', label='SY2-2', marker='o', markersize=10)
p4 = mlines.Line2D([], [], color='black', marker='o', markersize=10, label='SY2-2')

plt.grid(linestyle='--')
plt.ylim(0, 35000)
plt.xlim(0, 0.065)

plt.xticks([0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06], ['0', '1', '2', '3', '4', '5', '6'], fontproperties=fontprop)
plt.yticks([0, 5000, 10000, 15000, 20000, 25000, 30000, 35000], fontproperties=fontprop)

plt.xlabel('Equivalent Story Drift Ratio (%)', fontproperties=fontprop)
plt.ylabel('Secant Stiffness (kN)', fontproperties=fontprop)

plt.legend(handles=[p1, p2, p3, p4], loc=1, bbox_to_anchor=(0.99, 0.95), prop=fontprop)
plt.subplots_adjust(left=0.15, right=0.98, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)

plt.show()
