from sys import argv
#Author : Satheesh Gopalan

# LIST TO TAKE IN ALL ARGUMENT INTO THE LIST 'S'
s = []
s = argv

# PRINT THE NUMBER OF ARGUMENTS
print 'Number of arugment were : ' + str(len(s))

# PRINT THE ARGUMENTS
for i in range(len(s)):
	print "Arg [" + str(i) + "]: " + str(s[i])
