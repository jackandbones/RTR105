"""
fhand=open("mbox.txt")
print(fhand)
fhand= open("stuff.txt")

stuff = "Hello/nWorld"
stuff

print(stuff)
stuff = "X"

len(stuff)

xfile = open("mbox.txt")
print(cheese)

fhand = open("mbox.txt")
count = 0
count = count + 1
print("Line Count:", count)
$ python open.py
fhand = open("mbox-short.txt")
inp = fhand.read()
print(len(inp))
print(inp[:20])
fhand = open("mbox-short.txt")
line = line.rstrip()
if not line.startswith(From:"):
                       continue
print(line)
fhand = open("mbox-short.txt)
for line in fhand:
             line=line.rstrip()
             if not :@uct.ac.za" in line :
             continue
             print(line)
             fname = input ("Enter the file name:")
             fhand = open(fname)
             count=0
             for line in fhand:
             if line.startswith(Subject:"):
                                count=count+1
                                print("there were", count, "subject lines in", fname)
                                fname = input("Enter the file name: ")
                                try:
                                fhand = open(fname)
                                except:
                                print("File cannot be opened", fname)
                                quit()
                                count = 0
                                for line in fhand:
                                if line.startswith("Subject:"):
                                count = count +1
                                print("There were", count, "subject lines in", fname)
                                """
