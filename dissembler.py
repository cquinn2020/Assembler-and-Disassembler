import functions as func

# prompt the user for the name of the file
fileName = input("Please enter the file name that you wish to disassemble (include .hack): ")

# verified = False
# while not verified:
#     # open the file for reading and verify 
#     try:
#         file = open(fileName, 'r')
#         verified = True
#     except IOError:
#         print("Unable to open file.")
#         # prompt the user for the name of the file
#         fileName = input("Please enter the file name that you wish to disassemble (include .hack): ")
try:
    file = open(fileName, 'r')
except IOError:
    print("Unable to open file.\n")
# remove extension to create the outfile
index = fileName.find('.')
asmFileName = fileName[:index]

# open binary file for writing
asmFileOut = open(asmFileName + ".asm", 'w')

# get the contents of the .asm file
Lines = file.readlines()
# loop thru line by line and process
for line in Lines:
    line = line.strip()
    if func.IsAInstruction(line):
        asmFileOut.write(func.translateAInstruction(line) + '\n')
    if func.IsCInstruction(line):
        asmFileOut.write(func.translateCInstruction(line) + '\n')


# close the files
file.close()
asmFileOut.close()