from DataObject import DataObject
import pefile


class PESection():
    def __init__(self, name, address, virtual_size, raw_size):
        self.Name = name
        self.VirtualAddress = address
        self.VirtualSize = virtual_size
        self.RawSize = raw_size

    def printSection(self):
        print("Section Name: {}\n\tVirtual Address: {}\n\tVirtual Size: {}\n\tRaw Size: {} ".format(self.Name,
                                                                                                    self.VirtualAddress,
                                                                                                    self.VirtualSize,
                                                                                                    self.RawSize))


class PEDataObject(DataObject):

    def __init__(self, path):
        DataObject.__init__(self, path)
        self.pe = pefile.PE(path)
        self.signature = hex(self.pe.NT_HEADERS.Signature)
        self.magic = hex(self.pe.DOS_HEADER.e_magic)

        self.dlls = []
        for entry in self.pe.DIRECTORY_ENTRY_IMPORT:
            self.dlls.append(entry.dll.decode('utf-8'))
        self.sections = []
        for section in self.pe.sections:
            self.sections.append(
                PESection(section.Name.decode('utf-8'), hex(section.VirtualAddress), hex(section.Misc_VirtualSize),
                          hex(section.SizeOfRawData)))

    def printPEDataObject(self):
        print(self.magic)
        print(self.signature)
        print(self.dlls)
        for section in self.sections:
            section.printSection()

"""
def __main__():
    path = input("Enter path to file: ")
    o = PEDataObject(path)
    o.printDataObject()
    o.printPEDataObject()


__main__()

"""