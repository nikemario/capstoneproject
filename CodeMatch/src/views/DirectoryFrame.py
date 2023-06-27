""" [DirectoryView.py Documentation] """
import os
from functools import partial
from tkinter import *
from tkinter import filedialog

from src.const.DIR import DIR
from src.const.UI import UI
from src.core.Database import Database
from src.dtos.DirectoryDTO import DirectoryDTO
from src.dtos.FileDTO import FileDTO
from src.dtos.FolderDTO import FolderDTO
from src.views.common.DirectoryListbox import DirectoryListbox
from src.views.dialogs.SaveDirectoryDialog import SaveDirectoryDialog


class DirectoryFrame(Frame):

    def __init__(self, master):
        super().__init__(master)

        # DIRECTORY INFORMATION
        self.directory_ID = 0
        self.save_to_database = False

        self.database = Database()
        self.directory = None

        # DIRECTORY VIEW UI

        self.directory_toolbar = Label(self, text="", bg=UI.background,
                                       fg=UI.foreground)
        self.directory_toolbar.pack(fill=X, side=TOP, anchor=W)

        # Directory Toolbar Buttons
        self.upload_directory = UploadDirectoryButton(self)
        self.open_directory = OpenDirectoryButton(self)
        self.directory_information = DirectoryInformationButton(self)
        self.save_directory = SaveDirectoryButton(self)
        self.delete_directory = DeleteDirectoryButton(self)
        self.clear_directory = ClearDirectoryButton(self)

        self.upload_directory.configure(
            command=partial(self.clickUploadDirectory))
        self.open_directory.configure(
            command=partial(self.clickOpenDirectory))
        self.save_directory.configure(
            command=partial(self.clickSaveDirectory))
        self.delete_directory.configure(
            command=partial(self.clickDeleteDirectory))
        self.clear_directory.configure(
            command=partial(self.clickClearDirectory))

        self.directory_listbox = DirectoryListbox(self)
        self.directory_listbox.configure(selectmode="multiple",
                                         exportselection=False)
        self.directory_listbox.pack(expand=True, fill=BOTH, side=BOTTOM)

        # Dialogs
        self.save_directory_dialog = None
        self.select_directory_dialog = None

    # DIRECTOTY TOOLBAR BUTTON FUNCTIONS #

    def clickUploadDirectory(self):
        self.directory_ID = self.insertFileDirectory()
        self.clickOpenDirectory(self.directory_ID)

        self.save_to_database = False  # Set after running clickOpenDirectory

        # Update GUI Elements LAST
        self.save_directory.configure(state=NORMAL)
        self.delete_directory.configure(state=DISABLED)
        self.clear_directory.configure(state=NORMAL)

    def clickOpenDirectory(self, directory_ID):
        # Update GUI Elements
        self.save_directory.configure(state=DISABLED)
        self.delete_directory.configure(state=NORMAL)
        self.clear_directory.configure(state=NORMAL)

        self.directory_ID = directory_ID
        self.save_to_database = True
        self.directory_listbox.openDirectory(directory_ID, None)

    def clickSaveDirectory(self):
        # Update GUI Elements FIRST
        self.save_directory.configure(state=DISABLED)
        self.delete_directory.configure(state=NORMAL)

        self.save_to_database = True

        self.save_directory_dialog = SaveDirectoryDialog(self)
        self.save_directory_dialog.protocol("WM_DELETE_WINDOW",
                                            self.quitSaveDirectoryDialog)

    def clickDeleteDirectory(self):
        # Update GUI Elements
        self.save_directory.configure(state=NORMAL)
        self.delete_directory.configure(state=DISABLED)

        self.save_to_database = False

    def clickClearDirectory(self):
        # Update GUI Elements
        self.save_directory.configure(state=DISABLED)
        self.clear_directory.configure(state=DISABLED)
        self.delete_directory.configure(state=DISABLED)

        # Delete Directory from DB if not saved by user
        if not self.save_to_database and not self.directory is None:
            self.database.DELETE_DIRECTORY(self.directory.directory_ID)

        self.directory = None
        self.directory_listbox.clearDirectory()

    # SUPPORTING FUNCTIONS #

    def quitSaveDirectoryDialog(self):
        self.clickDeleteDirectory()
        self.save_directory_dialog.destroy()

    #
    # DIRECTORY FUNCTIONS
    #

    def insertFileDirectory(self):
        # DIRECTORY DTO #
        os_path = filedialog.askdirectory(initialdir="C:/",
                                          title="Select Directory TEST")
        directory_path_start = os_path.rfind("/")

        directory_name = "Uploaded Directory"
        directory_path = os_path[directory_path_start:] + "/"
        directory_ID = self.database.INSERT_DIRECTORY(
            directory_name, directory_path)

        for current_file, dirs, files in os.walk(os_path):

            # FOLDER DTO
            folder_name = os.path.basename(current_file)
            folder_path = current_file[directory_path_start:].replace(
                "\\", "/") + "/"

            folder_ID = self.database.INSERT_FOLDER(
                folder_name, folder_path, directory_ID)

            for file_name in files:
                file_path = current_file + "/" + file_name
                file_path = file_path.replace("\\", "/")

                # FILE DTO
                file_ext = file_name[file_name.rfind(".")+1:].upper()

                file_ID = self.database.INSERT_FILE(
                    file_name, file_ext, folder_ID, directory_ID)

                file_contents = open(file_path, "rb").read().splitlines()

                line_number = 0
                for line_binary in file_contents:
                    # CONTENT DTO
                    line_content = line_binary.hex()
                    content_ID = self.database.INSERT_CONTENT(
                        line_content, line_number, file_ID, folder_ID, directory_ID)

                    try:
                        line_string = line_binary.decode("utf-8")

                        num_words = len(line_string.split())
                        num_characters = len(line_string)

                        self.database.COMPLETE_CONTENT(
                            content_ID, num_words, num_characters)

                    except UnicodeDecodeError:
                        pass

                    line_number += 1

                #  COMPLETE FILE INFORMATION
                self.database.COMPLETE_FILE(file_ID, folder_ID, directory_ID)
            # COMPLETE FOLDER INFORMATION
            self.database.COMPLETE_FOLDER(folder_ID, directory_ID)
        # COMPLETE DIRECTORY INFORMATION
        self.database.COMPLETE_DIRECTORY(directory_ID)

        return directory_ID

# # # # # # # # # # # # #
# SINGLE USE FUNCTIONS  #
# # # # # # # # # # # # #


def UploadDirectoryButton(self) -> Button:
    img_directory = DIR.app_directory + DIR.folder_search
    self.open_dir_from_file = PhotoImage(file=img_directory)
    created_button = Button(self.directory_toolbar,
                            image=self.open_dir_from_file)
    created_button.pack(side=LEFT)
    return created_button


def OpenDirectoryButton(self) -> Button:
    img_directory = DIR.app_directory + DIR.database_upload
    self.open_dir_from_db = PhotoImage(file=img_directory)
    created_button = Button(self.directory_toolbar,
                            image=self.open_dir_from_db, state=DISABLED)
    created_button.pack(side=LEFT)
    return created_button


def DirectoryInformationButton(self) -> Button:
    img_directory = DIR.app_directory + DIR.database_information
    self.db_info_btn = PhotoImage(file=img_directory)
    created_button = Button(self.directory_toolbar,
                            image=self.db_info_btn, state=DISABLED)
    created_button.pack(side=LEFT)
    return created_button


def SaveDirectoryButton(self) -> Button:
    img_directory = DIR.app_directory + DIR.database_save
    self.save_dir_to_db = PhotoImage(file=img_directory)
    created_button = Button(self.directory_toolbar,
                            image=self.save_dir_to_db, state=DISABLED)
    created_button.pack(side=LEFT)
    return created_button


def DeleteDirectoryButton(self) -> Button:
    img_directory = DIR.app_directory + DIR.database_delete
    self.delete_dir_from_db = PhotoImage(file=img_directory)
    created_button = Button(self.directory_toolbar,
                            image=self.delete_dir_from_db,
                            state=DISABLED)
    created_button.pack(side=LEFT)
    return created_button


def ClearDirectoryButton(self) -> Button:
    img_directory = DIR.app_directory + DIR.database_clear
    self.clear_dir = PhotoImage(file=img_directory)
    created_button = Button(self.directory_toolbar,
                            image=self.clear_dir, state=DISABLED)
    created_button.pack(side=RIGHT)
    return created_button
