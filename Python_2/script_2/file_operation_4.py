import sys
a1 = sys.argv[1]
a2 = sys.argv[2] 

f = open(f"{a1}", "r")
g = open(f"{a2}", "w")

for line in f:
	g.write(line)

f.close()
g.close()
print("Copied file contents of main.txt to duplicate.txt")