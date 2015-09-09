# ratios.1
import random

if input == "":
   rps = ['R','P','S']
   ratios = [0,0,0]
else:
   if input == "R":
      ratios[0] += 1
   elif input == "P":
      ratios[1] += 1
   else:
      ratios[2] += 1
   maxRatio = max(ratios]
   index = ratios.index(maxRatio)
   output = rps[(index+1)%3]