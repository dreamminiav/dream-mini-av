import os
import stat
import time
import hashlib


# C:\Users\Otimus\Desktop\KeygenMe.exe
class DataObject:
    def __init__(self, path):
        try:
            f = open(path, "rb")
        except IOError:
            print("Error: invalid file/path")
            exit(1)
        file_stats = os.stat(path)
        self.name = f.name.split("\\")[-1]
        self.path = f.name
        self.size = file_stats[stat.ST_SIZE]
        self.last_modified = time.strftime("%Y/%m/%d %I:%M:%S %p", time.localtime(file_stats[stat.ST_MTIME]))
        self.data = f.read()
        self.md5 = hashlib.md5(self.data).hexdigest()
        self.type = None
        f.close()

    def printDataObject(self):
        print("Name: ", self.name, "\nPath: ", self.path, "\nSize: ", self.size, "\nLast modified: ",
              self.last_modified, "\nData: ", self.data, "\nMD5: ", self.md5, "\nType: ",
              self.type, '\n', )


"""


def __main__():
    x = input("Enter path to file: ")
    o = DataObject(x)
    o.printDataObject()


__main__()
"""