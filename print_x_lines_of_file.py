# PRINT X LINE OF A FILE [GIVEN AS ARGUMENT]
#Author : Satheesh Gopalan
from sys import argv

script, file = argv

# TAKE THE NUMBER OF LINES TO BE READ
n = raw_input("Enter the number of lines you want read :")
n = int(n)

f=open(file)

# PRINT THE NUMBER OF LINES
for i in range(n):
	print f.readline(),
