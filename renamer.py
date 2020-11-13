#!/usr/bin/env python3

# import libaries
from datetime import datetime # required to date, time manipulation
import os # to make change to files, folders, etc

#os.listdir # obtain list of files in directory
#os.rename # to rename files

def rename_dates():
    folder = os.listdir() # lists current files in folder
    print(folder)

    # loop through folder list
    # read in old time format (DD MMM YY - DD MMM YY)
    for file in folder:

        # read in file and separate extension
        f_name, f_ext = os.path.splitext(file) # prints results after
        if f_ext == '.pdf':
            olddate = f_name.split(' - ') # split period 1 and period 2
            
            # probably best to loop this, change later
            olddate_p1 = olddate[0]
            olddate_p2 = olddate[1]

            # Read string based on time format
            #%d = 01, %b - Jan, %m - 09
            #%y - YY, %Y - YYYY
            p1 = datetime.strptime(olddate_p1, '%d %b %y') # dont forget the whitespace...
            p2 = datetime.strptime(olddate_p2, '%d %b %y')

            # Convert
            newdate_p1 = datetime.strftime(p1, '%Y%m%d')
            newdate_p2 = datetime.strftime(p2, '%Y%m%d')
            
            # Concat new file name
            newdate = newdate_p1 + "-" + newdate_p2
            newfile = newdate + f_ext
            print(newfile)

            # Rename, (old file, new file)
            os.rename(file, newfile)
        else:
            continue

        return 0;


rename_dates()