# Code to READ a file if it exists
#Author : Satheesh Gopalan
from os.path import exists

print '#'*30
print 'PYTHON CODE TO READ A FILE'
print '#'*30


# INPUT THE FILE NAME
print ' ENTER THE FILE TO BE READ : '
file=raw_input(">>")

# CHECK IF FILE EXIST
if exists(file):
    # IF EXISTS , PRINT FILE
	txt = open(file)

	print ' Here is your file : ' 
	print '='*30
	print txt.read()
	print '='*30

else : 
	# PRINT THAT FILE DOESN'T EXISTS
	print '='*30
	print ' FILE DOESN\'T EXISTS! ' 
	print '='*30
