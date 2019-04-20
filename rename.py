
# -*- coding: utf8 -*-
from mobi import Mobi
from save_file import Files
import os


class ListEbook():
    def __init__(self, path_to_folder):
        self.path = path_to_folder
        files = []
        for r, d, f in os.walk(self.path):
            for file in f:
                if '.mobi' in file:
                    files.append(os.path.join(r, file))


        for f in files:
            book = Mobi(f)
            book.parse()
            try:
                title = book.title()
                author = book.author()

                author = author.decode()
                title = title.decode()

                new_name = str("Kindle/"+author+" - "+title+".mobi")
                os.rename(f, new_name)

            except:
                print("pass", f)

l = ListEbook("Kindle/")


