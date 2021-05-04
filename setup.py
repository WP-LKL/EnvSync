import getpass
import os
import platform

USER_NAME = getpass.getuser()
OS = platform.system()    


# Windows
def add_to_startup(rfile):
    folderPath = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "envSync.bat", "w+") as bat_file:
        bat_file.write(r'start "" python %s' % (folderPath + "\\" + rfile))

if OS == "Windows":
    add_to_startup("sync.py")