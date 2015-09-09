#1337-RaNdOm
from random import random
input=""
first = random()
second = random()
if first<.5:
    if second<.33:
        output = "S"
    elif .33<second<.66:
        output = "R"
    elif .66<second:
        output = "P"
elif first>.5:
    if .5<first<.75:
        output = "R"
    elif .75<first:
        output = "S"