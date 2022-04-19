# create symbol table
symbolTable = {}
symbolTable["SP"] = 0
symbolTable["LCL"] = 1
symbolTable["ARG"] = 2
symbolTable["THIS"] = 3
symbolTable["THAT"] = 4

for i in range(16):
    symbolTable["R" + str(i)] = i

symbolTable["SCREEN"] = 16384
symbolTable["KBD"] = 24576

# create comp table
compTable = {}
compTable["0"] = "0101010"
compTable["1"] = "0111111"
compTable["-1"] = "0111010"
compTable["D"] = "0001100"
compTable["A"] = "0110000"
compTable["!D"] = "0001101"
compTable["!A"] = "0110001"
compTable["-D"] = "0001111"
compTable["-A"] = "0110011"
compTable["D+1"] = "0011111"
compTable["A+1"] = "0110111"
compTable["D-1"] = "0001110"
compTable["A-1"] = "0110010"
compTable["D+A"] = "0000010"
compTable["D-A"] = "0010011"
compTable["A-D"] = "0000111"
compTable["D&A"] = "0000000"
compTable["D|A"] = "0010101"
compTable["M"] = "1110000"
compTable["!M"] = "1110001"
compTable["-M"] = "1110011"
compTable["M+1"] = "1110111"
compTable["M-1"] = "1110010"
compTable["D+M"] = "1000010"
compTable["D-M"] = "1010011"
compTable["M-D"] = "1000111"
compTable["D&M"] = "1000000"
compTable["D|M"] = "1010101"

# create destination table
destTable = {}
destTable[""] = "000"
destTable["M"] = "001"
destTable["D"] = "010"
destTable["MD"] = "011"
destTable["A"] = "100"
destTable["AM"] = "101"
destTable["AD"] = "110"
destTable["AMD"] = "111"

# create jump table
jumpTable = {}
jumpTable[""] = "000"
jumpTable["JGT"] = "001"
jumpTable["JEQ"] = "010"
jumpTable["JGE"] = "011"
jumpTable["JLT"] = "100"
jumpTable["JNE"] = "101"
jumpTable["JLE"] = "110"
jumpTable["JMP"] = "111"