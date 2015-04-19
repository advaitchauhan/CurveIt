depts = {}
print "yo"
f = open("curves/depts.txt", "r")
line = f.readline()
names = line.split(" ")
name = ""
for i in range(1, len(names)):
	name += names[i]
depts[(names[0])] = name
line = f.readline()
while len(line) > 0:
	name = ""
	names = line.split(" ")
	for i in range(1, len(names)):
		name += " " + names[i]
	depts[(names[0])] = name
	line = f.readline()