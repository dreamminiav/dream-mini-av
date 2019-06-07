import os
'''
   Pentru un path dat, extrage o lista cu toate fisierele din directorul resprectiv.
'''
def getListOfFiles(dirName):
    # creez o listă de fișiere și subdirectoare
    listOfFile = os.listdir(dirName) #Return a list of the entries in the directory given by path.
    allFiles = list()
    # Iterez peste toate intrările
    for entry in listOfFile:
        # Creez un path complet
        fullPath = os.path.join(dirName, entry)
        # Dacă intrarea este un director, obțin lista fișierelor din acest director 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


def getListOfFilesForDirectory(dirName):
    # Obțin lista tuturor fișierelor din arborele de directoare la un anumit path dat
    list_of_files = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        list_of_files += [os.path.join(dirpath, file) for file in filenames]

    return list_of_files