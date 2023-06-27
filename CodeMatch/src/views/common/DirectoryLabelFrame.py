from tkinter import *

from src.const.DIR import DIR
from src.const.UI import UI
from src.dtos.DirectoryDTO import DirectoryDTO


class DirectoryLabelFrame(LabelFrame):
    """ [Class DocString] """

    def __init__(self, master):
        super().__init__(master)

        self.directory = None

        # Configure
        self.configure(text="Directory")

        # self.saved_to_database = Label(self, text="")
        directory_name = Label(self)
        self.directory_name = Label(
            directory_name, text="Directory Name", width=50)
        self.directory_name.pack(anchor=NW, side=LEFT)
        test_answer = Message(
            directory_name, text="Test test test test test test.")
        test_answer.pack(anchor=NW, side=RIGHT)
        directory_name.pack(fill=X, side=TOP)

        self.directory_path = Label(self, text="Path")
        self.directory_path.pack(anchor="w")
        self.total_folders = Label(self, text="Total Folders")
        self.total_folders.pack(anchor="w")
        self.total_files = Label(self, text="Total Files")
        self.total_files.pack(anchor="w")

        # Info
