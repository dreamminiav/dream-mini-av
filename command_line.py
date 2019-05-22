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

def main():
    
    dirName = '//';
    
    # Obțin lista tuturor fișierelor din arborele de directoare la un anumit path dat
    listOfFiles = getListOfFiles(dirName)
    
    # Afisez fisierele
    for elem in listOfFiles:
        print(elem)
 
    print ("****************")
    
    # Obțin lista tuturor fișierelor din arborele de directoare la un anumit path dat
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
          
    for elem in listOfFiles:
        print(elem)    
               
        
if __name__ == '__main__':
    main()




"""
BASE_DIRECTORY="C:\"

for dirpath, dirnames, filenames in os.walk(BASE_DIRECTORY):
        for filename in filenames:

        #defining file type
        txtfile=open(filename,"r")
        txtfile_full_path = os.path.join(dirpath, filename)
        try:
            for line in txtfile:

                if line.startswidth('Start Date:'): # You do not need regular expressions. You can use basic string functions: 'break' if you have all information collected.
                start_date = line.split()[-1]

                elif line.startswidth('Format:'):
                data_format = line.split()[-1]
                
                print(
                    txtfile_full_path,
                    start_date,
                    data_format,
                    resolution)

        except Exception as e:
        	print(str(e))
"""
               
"""
Modulul OS din Python oferă o modalitate de a utiliza funcționalitatea dependentă de sistemul de operare.
