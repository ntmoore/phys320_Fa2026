'''

Modifying first box-pushing example to repeat the calculation 
for a list of angles

Nathan Moore
2026-09-08
'''

# I need the math library
import math

# defining constants
mu_k = 0.6 # static friction between box and floor
mg = 200 # (lbs) box weight in 

# convert degrees to radians with this
pi_over_180 = math.pi/180.0 


print("mu_k = ",mu_k)
print("mg = ",mg," (lbs)")

print("theta(degrees) Fp(lbs)")
# print out results for a list of angles
for theta in [0,10,20,30,40]:
    theta_rad = theta*pi_over_180
    Fp = mg/((1.0/mu_k)*math.cos(theta_rad) - math.sin(theta_rad))
    print(theta,Fp)

''' expected results
mu_k =  0.6
mg =  200  (lbs)
theta(degrees) Fp(lbs)
0 120.0
10 136.26780813165888
20 163.3807763662887
30 212.0046188698979
40 315.4807365086305
'''
