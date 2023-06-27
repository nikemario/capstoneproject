from tkinter import *

from src.const.DIR import DIR
from src.const.UI import UI
from src.dtos.FileDTO import FileDTO


class FileLabelFrame(LabelFrame):
    """ [Class DocString] """

    def __init__(self, master):
        super().__init__(master)

        # Configure
        self.configure(text="File")

        self.file_name = Label(self, text="File Name")
        self.file_name.pack(anchor="w")
        self.file_ext = Label(self, text="File Extension")
        self.file_ext.pack(anchor="w")
        self.file_size = Label(self, text="File Size")
        self.file_size.pack(anchor="w")
        self.num_lines = Label(self, text="Number of Lines")
        self.num_lines.pack(anchor="w")
        self.num_words = Label(self, text="Number of Words")
        self.num_words.pack(anchor="w")
        self.num_characters = Label(self, text="Number of Characters")
        self.num_characters.pack(anchor="w")

        # Info
