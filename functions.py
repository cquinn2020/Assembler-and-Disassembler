import tables as table

# function to return of binary instruction is a hack A  instruction
def IsAInstruction(instruction):
    if instruction[0] == "0":
        return True
    return False

# function to return of binary instruction is a hack C  instruction
def IsCInstruction(instruction):
    if instruction[0] == "1":
        return True
    return False

# function to translate A instruction from binary to ASM
def translateAInstruction(instruction):
    num = 0
    instruction = instruction[1:]
    weights = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    for i in range(len(instruction)):
        if instruction[i] == "1":
            num += weights[i]
    return '@' + str(num)

# write a function to tokenize the C instruction
def getTokens(instr):
    cTokens = instr[3:10]
    dTokens = instr[10:13]
    jTokens = instr[13:]
    # return a list of the tokens
    return [cTokens, dTokens, jTokens]


def translateCInstruction(instruction):
    # tokenize the instructions
    tokens = getTokens(instruction)
    for line in tokens:
        line = line.strip()
    # get the values from the dictionary for each part
    comp = table.compTable.get(tokens[0])
    dest = table.destTable.get(tokens[1])
    jump = table.jumpTable.get(tokens[2])
    # if dest and jump are both null its comp only instruction
    if dest == "null" and jump == "null":
        return comp
    # if dest = null and jumps not null then its a comp;jump instruction
    elif dest == "null" and jump != "null":
        return comp + ";" + jump
    # if dest isnt null and jump is null then its a dest=comp instruction
    elif dest != "null" and jump == "null":
        return dest + "=" + comp
    # otherwise it should be a dest=comp;jump instruction
    else:
        return dest + "=" + comp + ";" + jump
 

 
def translateRecursiveAInstr(binaryInstr, i):
    if binaryInstr == "":
        return 0
    elif binaryInstr[i] == "1":
        print(i)
        binaryInstr = binaryInstr.replace(binaryInstr[i], "")
        return 2 ** i + translateRecursiveAInstr(binaryInstr, i - 1)
    else:
        print(i)
        binaryInstr = binaryInstr.replace(binaryInstr[i], "")
        return 0 + translateRecursiveAInstr(binaryInstr, i - 1)

