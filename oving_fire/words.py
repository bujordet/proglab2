__author__  = "Morten Bujordet"
from os import listdir
from os.path import isfile, join



class filereader:

    def file_reader(filepath):
        file = open(filename, encoding = ’utf-8’)
        string = ""
        for line in file.readlines():
            string += line.strip() + " "
        file.close()
        return string.lower()

    def 





class Words(object):
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def readFile():
        liste = []
        for line in stdin:
            line.strip([' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',\
                        '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',\
                        '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'])
            if line not in liste:
                liste.append(line)
        return liste

    def
