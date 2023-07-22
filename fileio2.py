# To reading the file and writing

fd=open('Hello.txt','r')
passFile=open('PassFile.txt','w')
failFile=open('FailFile.txt','w')

for line in fd:
    line_split=line.split()
    if line_split[2]=='P':
        passFile.write(line)
    else:
        failFile.write(line)

fd.close()
passFile.close()
failFile.close()