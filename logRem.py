import shutil
import os
import time




global prosentage_left # percentage of disk space left
global prosentage_used # percentage of disk space used
global x # loop variable
x = 1

global redstart # red color code
global redend # end of red color code
global greenstart # green color code
global greenend # end of green color code
global yellowstart # yellow color code
global yellowend # end of yellow color code
global dir_path # directory of log files 
dir_path = "C:\\ANC2010\\Data\\LoggingManager\\" # Directory of log files: C:\ANC2010\Data\LoggingManager\
# If you want to change the directory, change the path in the line above

#by default, the script will run once a day. If you want to change this, change the time.sleep() function in the while loop at the bottom of the script(it is in seconds)

# Color codes

redstart = "\033[91m"
redend = "\033[0m"
greenstart = "\033[92m"
greenend = "\033[0m"
yellowstart = "\033[93m"
yellowend = "\033[0m"


print(yellowstart + "Logrem starts..." + yellowend)


print(""" 
To run Loggrem, you need to accept the terms and conditions.
This is just an abbreviation of the terms and conditions of Loggrem.
You can read the full agreement at https://pastebin.com/jen5XQBE""")

print("Do you accept the terms and conditions?")
svar = input("Write yes or no: ")
if svar == "yes":
    print("Accepted")
    pass
else:
    print(yellowstart + "You have not accepted the terms and conditions" + yellowend)
    print(yellowstart + "Loggrem terminates" + yellowend)
    x = 0
    exit()


def prosentage_calculator():
    global prosentage_left
    global prosentage_used
    hdd = shutil.disk_usage('c:/')
    print(hdd)
    prosentage_left = hdd.free / hdd.total * 100
    prosentage_used = hdd.used / hdd.total * 100


def logg_delete():
    if prosentage_used > 80:
        print(yellowstart + "The disk is now over 80% full" + yellowend)
        print("Do you want to delete the log files in C:\ANC2010\Data\LoggingManager\ ?")
        svar = input("Write yes or no: ")
        if svar == "yes":
            print(yellowstart + "Deleting log files" + yellowend)
            
            
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f"Error deleting file: {file_path} - {e}")
            
        else:
            print(redstart + "Log files are not deleted" + redend)
            print(yellowstart +"You will be reminded of this again in 1 day" + yellowend)

        print(redstart + "Log files are deleted" + redend)    


print(greenstart + "Loggrem is running" + greenend)

while x == 1:
    prosentage_calculator()
    if prosentage_used > 80:
        logg_delete()
    else:
        pass
    time.sleep(86400)
