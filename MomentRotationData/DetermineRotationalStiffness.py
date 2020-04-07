from sympy import *
F1, D1, k = symbols('F1, D1, k')

L1 = 2.53
L2 = 1.41
I1 = 116256833.33333331e-12
E1 = 205e9
E2 = 205e9

# for SX1 & SX2
#I2 = 521816479.4e-12

# for SY1 & SY2
I2 = 1.6065E-04

C = F1*L1**2/k + F1*L1**3/(3*E1*I1)
eq = F1*L1**2*L2/(3*E2*I2) + C - D1

# For SX1
eq1 = eq.subs({F1:54782.463, D1:0.015882007*(1-0.074)})
sol1 = solve(eq1, k)

# For SY1
eq2 = eq.subs({F1:19695.21, D1:0.0049079986*(1-0.074)})
sol2 = solve(eq2, k)
print(eq2)

print(sol2[0]/1e6)

disp0 = F1*L1**2*L2/(3*E2*I2) + C
disp1 = disp0.subs({F1:150e3/2.22, k:1051e6})
print('disp = %f' % disp1)

