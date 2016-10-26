__author__  = "Morten Bujordet"
from os import listdir
from os.path import isfile, join
import codecs


class Filereader:


    def file_reader(self, filepath):
        file = codecs.open(filepath, 'r', encoding = "utf-8")
        string = ""
        for line in file.readlines():
            string += line.strip() + " "
        file.close()
        return string.lower()


    def create_string(self, filepath):
        return " ".join(open(filepath, encoding = "utf-8").readlines()).split()


    def create_filepath_list(self, directory):
        liste = []
        for f in listdir(directory):
            if (isfile(join(directory, f))):
                liste.append(directory + f)
        return liste


class Lister:

    def __init__(self, name):
        self.name = name
        self.words = dict()



    def remove_nonealpha(string):
        clean = ""
        for char in string:
            if (char.isalnum() or char == ' '):
                clean += char
        return clean

    def make_wordlist_from_path(self, filepaths):
        for filepath in filepaths:
            word_list = self.remove_nonealpha(Filereader.file_reader(filepath)).split()
        return word_list
