ary: list[str] = []
with open("D:\\Download\\actionListInput.txt", "r") as file_object: ##example


    for line in file_object:

        line = line.strip("\n")
        if len(line) < 5 :
            continue
        
        action = line[line.index("ACTION::")+8:]
        id = line[line.index("ID:")+3:line.index("Name")-1]
        string = action + id
        ary.append("public const int " + action + " = " + id + ";")
    
for string in ary :
    print(string)

## actionListInput.txt uses https://github.com/AsteriskAmpersand/Leviathon/blob/main/common/ActionDumps/
## make sure every line in the input has consistent format
