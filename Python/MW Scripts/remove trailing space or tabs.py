OFile = input("What File? ")
OpenFile = open(OFile)
print("Please be patient while the file is being processed")

writelist = []
for line in OpenFile:
    writelist.append(line.strip())

OpenFile.close()

WFile = input("what is the return file: ")
WriteFile = open(WFile, "w")

for i in writelist:
    WriteFile.write(i)
    WriteFile.write("\n")
    
WriteFile.close()

print("Thanks for waiting, file has been processed :)")
