# WARNING #
#=========#

# This is JUST template for XML parsing! It needs modification according to the file that needs to be parsed. 




import sys
import os
import xml.etree.ElementTree as ET

xmlfile=filename # Take filename as argument before this!


# ACTUAL PARSING BEGINS BELOW :
#num_lines is length of file ie, number of lines in region.xml file.
num_lines = sum(1 for line in open(xmlfile))

#To reach the root of tree

tree = ET.parse(xmlfile)
root = tree.getroot()

#To get the number of "KEYWORD" in the file
from xml.dom.minidom import parseString
file = open(xmlfile,'r')
data = file.read() #open
file.close()
dom = parseString(data)
x = len(dom.getElementsByTagName('KEYWORD')) # get count and saves to variable x


for v in range(len()): # LOOP for number of commandline arugments 
       
        for i in range(x):   # LOOP for number of count of vc_volumes

                if str(''.join(root[i].attrib['KEYWORD_attrib'])) ==  "KEYWORD" :
                        print "Volume Name : " + root[i].attrib['KEYWORD_attrib']

