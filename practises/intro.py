import sys
#sys.path.append("/home/supremo/Desktop/python notes/mymodule.py")#it finds our modules in our directory

from mymodule import find_index , test
coursea=["english","kiswahili","social"]

#calling my function
index=find_index(coursea,"math")
print(index)
print (test)


import datetime
import calendar
today=datetime.date.today()
print(today)
print(calendar.isleap(2024))

import os
print (os.getcwd())