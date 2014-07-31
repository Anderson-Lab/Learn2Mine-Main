import os
import sys
import subprocess
import random

key = str(sys.argv[1])
outfileLocation = sys.argv[2] #Output in keyMaker.xml
email = sys.argv[3].replace("__at__","@")#.split("@")[0]

os.chdir("../../../../tools/myTools/simulatedTrader")

os.system("mkdir -p "+email)
#subprocess.call("mkdir"+email)

lines = []
lines.append("# Fraction of our money that we will invest each time we open a new position\n")
p1 = random.randrange(1,9)/10.0
lines.append("frac.money.invest="+str(p1)+"\n")
lines.append("# Maximum loss we are willing to admit before we close the position\n")
p2 = random.randrange(1,10)/100.0
lines.append("max.loss.admit="+str(p2)+"\n")
lines.append("# Profit margin that we wish for our positions and is used when posting the limit orders\n")
p3 = random.randrange(1,10)/100.0
lines.append("profit.margin.positions="+str(p3)+"\n")

userFile = open(email+"/parameters.txt","w")
userFile.writelines(lines)
userFile.close()

os.chdir(email)

outfile = open(outfileLocation, "w")
outfile.writelines(lines)
outfile.close()

subprocess.call("Rscript '../simulatedTrader.R'", shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)

