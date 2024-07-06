import os
import shutil

path = "documents/removeTest.txt"
# path = "documents/Emptyfolder"    # rmdir()
# path = "documents/Datafolder"     # rmtree()


try:
    os.remove(path)     # delete a file
    # os.rmdir(path)      # delete an empty directory
    # shutil.rmtree(path) # delete a directory containing files | dangerous | be careful while use this
except FileNotFoundError:
    print("That file not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cann't delete that file useing that method")
else:
    print(path + " was deleted")