# create comp table
compTable = {}
compTable["0101010"] = "0"
compTable["0111111"] = "1"
compTable["0111010"] = "-1"
compTable["0001100"] = "D"
compTable["0110000"] = "A"
compTable["0001101"] = "!D"
compTable["0110001"] = "!A"
compTable["0001111"] = "-D"
compTable["0110011"] = "-A"
compTable["0011111"] = "D+1"
compTable["0110111"] = "A+1"
compTable["0001110"] = "D-1"
compTable["0110010"] = "A-1"
compTable["0000010"] = "D+A"
compTable["0010011"] = "D-A"
compTable["0000111"] = "A-D"
compTable["0000000"] = "D&A"
compTable["0010101"] = "D|A"
compTable["1110000"] = "M"
compTable["1110001"] = "!M"
compTable["1110011"] = "-M"
compTable["1110111"] = "M+1"
compTable["1110010"] = "M-1"
compTable["1000010"] = "D+M"
compTable["1010011"] = "D-M"
compTable["1000111"] = "M-D"
compTable["1000000"] = "D&M"
compTable["1010101"] = "D|M"


# create dest table
destTable = {}
destTable["000"] = "null"
destTable["001"] = "M"
destTable["010"] = "D"
destTable["011"] = "MD"
destTable["100"] = "A"
destTable["101"] = "AM"
destTable["110"] = "AD"
destTable["111"] = "AMD"


# create jump table
jumpTable = {}
jumpTable["000"] = "null"
jumpTable["001"] = "JGT"
jumpTable["010"] = "JEQ"
jumpTable["011"] = "JGE"
jumpTable["100"] = "JLT"
jumpTable["101"] = "JNE"
jumpTable["110"] = "JLE"
jumpTable["111"] = "JMP"