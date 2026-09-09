'''
09-09-push_a_box.py

this is an example calculation that shows how you can 
write python pgrams that will run the numbers for you
in homework problems.  Having a written record of the 
math you're doing is very useful when things go wrong 
and you're trying to find your errors.

Nathan Moore
2026-09-08
'''

# this is also a comment

# I need the math library
import math

# defining constants
mu_k = 0.6 # static friction between box and floor
mg = 200 # (lbs) box weight in 
theta = 10 # (degrees) the angle below the horizontal 
#that the box is being pushed by a person

pi_over_180 = math.pi/180.0 # convert degrees to radians with this

Fp = mg/((1.0/mu_k)*math.cos(theta*pi_over_180) - math.sin(theta*pi_over_180) )

print("mu_k = ",mu_k)
print("mg = ",mg)
print("theta = ",theta)
print("Fp = ",Fp)

''' expected results are:
mu_k =  0.6
mg =  200
theta =  10
Fp =  136.26780813165888
'''
