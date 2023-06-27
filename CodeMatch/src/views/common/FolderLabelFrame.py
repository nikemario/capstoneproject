from tkinter import *

from src.const.DIR import DIR
from src.const.UI import UI
from src.dtos.FolderDTO import FolderDTO


class FolderLabelFrame(LabelFrame):
    """ [Class DocString] """

    def __init__(self, master):
        super().__init__(master)

        # Configure
        self.configure(text="Folder")

        self.folder_name = Label(self, text="Folder Name")
        self.folder_name.pack(anchor="w")
        self.folder_path = Label(self, text="Path")
        self.folder_path.pack(anchor="w")
        self.num_folders = Label(self, text="Number of Folders")
        self.num_folders.pack(anchor="w")
        self.num_files = Label(self, text="Number of Files")
        self.num_files.pack(anchor="w")

        # Info
