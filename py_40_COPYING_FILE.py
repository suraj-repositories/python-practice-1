# copyfile()  = copies contents of a File
# copy()      = copyfile() + permission mode + destination can be a directory
# copy2()     = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('documents/test.txt', 'documents/copy.txt')
                # (source, destination)

# copy() & copy2() have same arguments
# depending on your use in project
