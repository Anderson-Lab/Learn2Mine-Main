#Dat-Aspen
from random import random
input=""
first = random()
second = random()
if first<.5:
    if second<.33:
        output = "S"
    elif .33<second<.66:
        output = "P"
    elif .66<second:
        output = "S"
elif first>.5:
    if .5<first<.75:
        output = "P"
    elif .75<first:
        output = "R"