# Your submission name here. This must be unique. If it is already taken, then you will have to choose another one.
if input == "":
    output = "P"
    move = "R"
lastMove =move
move = input

if move == "R":
    if lastMove == "R":
        output = "R"
    elif lastMove =="S":
        output = "P"   
    output = "P"
if input == "P":
    output = "P"
if input == "S":
    output = "S"