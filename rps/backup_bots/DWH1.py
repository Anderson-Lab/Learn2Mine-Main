#DWH1
if input == "":
	RC = PC = SC = 0
	MRC = MPC = MSC = 0

if input == "R":
	output = "S"
	MSC++
	RC++
elif input == "P":
	output = "R"
	MRC++
	PC++
elif input == "S":
	output = "P"
	MPC++
	SC++