import assemFuncs as func

# prompt the user for file to process
fileName = input("Please enter the file name that you wish to assemble (include .asm): ")
# create the rest of the symbol table from the file
func.symbolTable = func.createSymbolTable(fileName, func.symbolTable)
# open the file for reading and verify 
try:
    file = open(fileName, 'r')
except IOError:
    print("Unable to open file.")

# remove extension to create the outfile
index = fileName.find('.')
binaryFilename = fileName[:index]

# open binary file for writing
binaryFileOut = open(binaryFilename + ".hack", 'w')

# get the contents of the .asm file
Lines = file.readlines()
# loop thru line by line and process
for line in Lines:
    # remove comments and whitespace
    line = func.removeSpaces(line)
    line = func.removeComments(line)
    # if line is empty, continue
    if line == "":
        continue
    
    # check if it is an A instruction
    if line[0] == "@":
        # print("found A instruction\n")
        binary = func.convertAInstruction(line)
        binaryFileOut.write(binary + "\n")
        continue
    
    # check if its C instruction (not label)
    elif not func.isLabel(line):
        binary = func.convertCInstruction(line)
        binaryFileOut.write(binary + "\n") 
        continue
    else:
        continue

# close the files
file.close()
binaryFileOut.close()