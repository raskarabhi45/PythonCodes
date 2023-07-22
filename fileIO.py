# To reading the file and writing

f=open('hello.txt','r')
for line in f:
    line_split=line.split()
    if line_split[2]=='P':
        print(line)

f.close()

