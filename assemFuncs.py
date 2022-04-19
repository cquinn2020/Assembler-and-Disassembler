from unicodedata import decimal
from assemblyTables import symbolTable
from assemblyTables import destTable
from assemblyTables import compTable
from assemblyTables import jumpTable


# remove white space from a string
def removeSpaces(line):
    line = line.strip()
    line = line.replace(" ", "")
    return line

# function to remove comments
# -> search for / and remove everything after
def removeComments(line):
    index = line.find("//")
    if index == -1:
        return line
    else:
        line = line[0:index]
        return line

# function to see if a line is a label
def isLabel(line):
    if len(line) > 1 and line[0] == "(" and line[ len(line) - 1] == ")":
        return True
    else:
        return False

# function to remove parantheses
def removeParantheses(line):
    return line[1:len(line)-1]

# function to check for valid A instruction
def isValidAInstruction(instruction):
    # define valid characters
    validChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # check for a instruction signifier
    if instruction == ""  or instruction[0] != "@":
        return False
    # drop first character
    if len(instruction) > 2:
        dropAt = instruction[1: len(instruction) - 1]
    else:
        dropAt = instruction[1]
    # check if its a positive integer
    if dropAt.isdigit():
        return True
    # if its not a positive integer, check if first char is a digit
    # -> if so return false because cannot have variable start with a digit
    if dropAt[0].isdigit():
        return False 
    # check that are the characters are valid
    invalid = False
    # loop thru characters and check to see if each is valid
    for char in dropAt:
        if char not in validChars:
            invalid = True
    # return properly if made it this far
    if  not invalid:
        return True
    else:
        return False
    

# do the labels
def createSymbolTable(fileName, table):
    # predefined symbols have already been inserted
    # open file for reading
    file = open(fileName, 'r')
    # use function to get all lines from file and put into a list
    Lines = file.readlines()
    # instantiate counter
    pc = 0
    # iterate thru the lines in the list and parse
    for line in Lines:
        line = line.strip()
        # remove spaces and comments
        clean = removeSpaces(line)
        clean = removeComments(clean)

        # check if the line is a label
        if isLabel(clean):
            # if it is a label strip the parantheses
            label = removeParantheses(clean)
            # check if label is already in the symbol table or not
            val = symbolTable.get(label, -1)
            if val == -1:
                table[label] = pc
            
        # if not a label, then check if it is an instruction (not empty string)
        if len(clean) > 0 and clean != "" and not isLabel(clean):
            pc += 1
    file.close()
    # get variables
    # create another file object
    file2 = open(fileName, 'r')
    # starting address is 16
    address = 16
    Lines = file2.readlines()
    # iterate thru the lines and parse again
    for line in Lines:
        # remove comments and whitespace
        clean = removeSpaces(line)
        clean = removeComments(clean)
        # check if valid A instruction
        # if isValidAInstruction(clean):
        if len(clean) >= 1 and clean[0] == '@':
            # remove @ char
            AInstructionVal = clean.replace("@", "")
            # if val is 0 then clean is not in the symbol table
            val = table.get(AInstructionVal, -1)
            # if clean is not a number and is not in the symbol table then add to table
            if not AInstructionVal.isdigit() and val == -1:
                # add to table
                table[AInstructionVal] = address
                # increment address to the next spot
                address += 1
    return table

# function to convert decimal number to binary: max number should be 32767
# which is the last register in the ROM
def decimalToBinary(number):
    # weights for powers of 2 from 2^0 to 2^14
    weights = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    index = 0
    binaryString = "0"
    # loop through the weights and append 1 or 0 to string based on weight
    # - if weight is greater, append 0
    # - if weight is <= to num, append 1 and subtract weight from number
    for i in range(len(weights)):
        if weights[index] > number:
            binaryString += "0"
        else:
            binaryString += "1"
            number -= weights[index]
        index += 1
    
    return binaryString

# function to convert an A instruction to binary
def convertAInstruction(val):
    # remove the @ char
    dropAt = val[1:]
    # check if instruction is positive number, if so convert
    # to binary and return
    if dropAt.isdigit():
        dropAt = int(dropAt)
        bin = decimalToBinary(dropAt)

    # if not positive int, then look up var in table and convert 
    # address to binary
    else:
        addr = symbolTable.get(dropAt)
        # print("address: ", addr)
        bin = decimalToBinary(addr)
    return bin
        


def getTokens(instruction):
    # if "=" and ";" are not present, then it is an op only instruction
    if instruction.count('=') == 0 and instruction.count(';') == 0:
        tokens = instruction.split()
    # check if only "=" is present
    elif instruction.count('=') == 1 and instruction.count(';') == 0:
        tokens = instruction.split('=')
    # check if only ";" is present 
    elif instruction.count('=') == 0 and instruction.count(';') == 1:
        tokens = instruction.split(';')
    # else both are present
    else:
        # locate indices of the characters and then split the string 
        index1 = instruction.find('=')
        index2 = instruction.find(';')
        token1 = instruction[:index1]
        token2 = instruction[index1+1:index2]
        token3 = instruction[index2+1:]
        string = token1 + " " + token2 + " " + token3
        
        tokens = string.split()
        
    return tokens

def convertCInstruction(instruction):
    # get the tokens for the string
    tokens = getTokens(instruction)
    # intialize each token
    prefix = "111"
    dest = ""
    comp = ""
    jump = ""

    # if size of tokens list is 1 then its Op only
    if len(tokens) == 1:
        # get comp bits from table
        comp = compTable.get(tokens[0])
        dest = "000"
        jump = "000"

    elif len(tokens) == 2:
        # check instruction type
        if instruction.count('=') == 1:
            # dest and comp
            dest = destTable.get(tokens[0])
            comp = compTable.get(tokens[1])
            jump = "000"
        else:
            # comp and jump
            dest = "000"
            comp = compTable.get(tokens[0])
            jump = jumpTable.get(tokens[1])

    # else the number of tokens is 3 and we have type dest=comp;jmp instr        
    else:
        dest = destTable.get(tokens[0])
        comp = compTable.get(tokens[1])
        jump = jumpTable.get(tokens[2])
        
    # return binary of C instruction
    return (prefix + comp + dest + jump)



