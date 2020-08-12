execfile('../MTSsetup.py')

drifts = [0.375, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 6]
cycles = [6, 6, 6, 4, 2, 2, 2, 2, 2, 2]

y = []
x = []
count = 0

for i, obj in enumerate(drifts):
	for j in range(0, cycles[i]):
		y.append(0)
		y.append(obj)
		y.append(0)
		y.append(-obj)
		x.append(count)
		x.append(count + 0.25)
		x.append(count + 0.5)
		x.append(count + 0.75)
		count += 1

print(count)
plt.figure(figsize=(6, 6))
ax1 = plt.subplot(1, 1, 1)
plt.plot(x, y, color='k', linestyle='-')
plt.ylim(-8, 8)
plt.yticks([-8, -6, -4, -2, 0, 2, 4, 6, 8], fontproperties=fontprop)
plt.xlim(0, 35)
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35], fontproperties=fontprop)
plt.grid(linestyle='--')
plt.xlabel('Cycle', fontproperties=fontprop)
plt.ylabel('Equivalent Story Drift Angle (%)', fontproperties=fontprop)

plt.subplots_adjust(left=0.1, right=0.98, wspace=0.22, hspace=0.22, bottom=0.12, top=0.95)
plt.show()
