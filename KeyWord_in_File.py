

# This can be used to verify if a file contains a word or phrase

import sys,os
import datetime
import gzip

total_count=0
found_count=0
gzipfile=0
regularfile=0

KeyWord=str(raw_input("Enter the Key-Word to search for: "))
DateAfter=raw_input("Enter the date [Logs before this date will beignored] in DD-MM-YYYY format : ")


Start_date=datetime.datetime.strptime(DateAfter, "%d-%m-%Y").date()
print "Given Date : " + str(Start_date)

today = datetime.date.today()
print "Current Date  " + str(today)

if Start_date > today :
        print "Check the date Entered. It is greater than today's date.Quitting!"
        sys.exit()

path = "/a/logs/netdeploy"
for path, subdirs, files in os.walk(path):
    for name in files:
        full_path = os.path.join(path, name)
        #print full_path
        #  THIS WILL GIVE UNIX TIME : print
        os.path.getmtime(os.path.join(path, name))
        time_stamp_of_file = datetime.datetime.utcfromtimestamp(os.path.getmtime(full_path)).strftime('%Y-%m-%d %H:%M:%S')
        File_Date=datetime.datetime.strptime(time_stamp_of_file,"%Y-%m-%d %H:%M:%S").date()
        if File_Date > Start_date :
                total_count=total_count+1
                #print File_Date
                #print full_path
                if full_path.endswith(".gz"):
                        f = gzip.open(full_path, 'r')
                        file_content = f.read()
                        if KeyWord in file_content:
                                print "Log File : " + str(full_path)
                                print "File_date :" + str(File_Date)
                                found_count=found_count+1
                                gzipfile=gzipfile+1
                        #print file_content
                        f.close()
                        #sys.exit()
                else :
                        f = open(full_path, 'r')
                        file_content = f.read()
                        if KeyWord in file_content:
                                print "Log File : " + str(full_path)
                                print "File_date :" + str(File_Date)
                                regularfile=regularfile+1
                                found_count=found_count+1
                        #print file_content
                        f.close()
                        #sys.exit()




print "Total Logs that were there after the given date : " + str(total_count)
print "Total number of Logs where Key-Word was found : " + str(found_count)

print "Gzipped Files :" + str(gzipfile)
print "Regular Files :" + str(regularfile)