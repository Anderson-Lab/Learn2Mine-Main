#HehEH
import random

if input == "":
    Rc = Pc = Sc = 0
    history = []

if input == "R":
    Rc +=1

if input == "P":
    Pc +=1

if input == "S":
    Sc +=1

history.append(input)


if "RRRR" in history:
    output = "P"

if "SSSS" in history:
    output = "R"

if "PPPP" in history:
    output = "S"