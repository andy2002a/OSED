import re

badChars = '00-09-0A-0B-0C-0D-20'.split('-')

file = open('rop.txt','r')
fileContents = file.readlines()

regexArray = []

for char in badChars:
    regex = (r'''^0x''' + re.escape(char) + r'''|'''
            r'''^0x[a-fA-F0-9]{2}''' + re.escape(char) + r'''|'''
            r'''^0x[a-fA-F0-9]{4}''' + re.escape(char) + r'''|'''
            r'''^0x[a-fA-F0-9]{6}''' + re.escape(char)
        )
    
    regexArray.append(format(regex))

badCharsRegex = r'|'.join(regexArray)

#use set so that there are only qunique values
newFileContent = set()

for line in fileContents:
    if re.match(badCharsRegex, line):
        a = 1 #dummy code
    elif ' call ' in line:
        a = 1 #dummy code
    else:
        newFileContent.add(line)

newFileContentStr = ''.join(newFileContent)

outFile = open('out.txt', "w")
outFile.write(str(newFileContentStr))
outFile.close()
