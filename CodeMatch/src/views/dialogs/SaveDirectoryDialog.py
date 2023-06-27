from tkinter import *

from src.const.DIR import DIR
from src.const.UI import UI
from src.core.Database import Database
from src.views.common.DirectoryLabelFrame import DirectoryLabelFrame
from src.views.common.FileLabelFrame import FileLabelFrame
from src.views.common.FolderLabelFrame import FolderLabelFrame


class SaveDirectoryDialog(Toplevel):
    """ [Class DocString] """

    def __init__(self, master):
        super().__init__(master)

        self.database = Database()

        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight()  # Height of the screen

        width = int(screen_width/3)  # Width
        height = int(screen_height/2)  # Height

        # Calculate Starting X and Y coordinates for Window
        geometry_x = (screen_width/2) - (width/2)
        geometry_y = (screen_height/2) - (height/2)

        self.geometry('%dx%d+%d+%d' % (width, height, geometry_x, geometry_y))

        #
        #
        #
        #
        #

        self.window_frame = Frame(self, bg=UI.background)

        self.save_directory_prompt_label = Label(self.window_frame, bg=UI.background, text="Directory Name:")
        self.directory_name_input = Entry(self.window_frame, bg=UI.background)
        # self.save_directory_btn = Button(self.window_frame, text="Save")
        self.save_directory_btn = createOpenDirectoryFromFileBtn(self)

        self.save_directory_prompt_label.pack(**UI.ipadding, anchor=W)
        self.directory_name_input.pack(**UI.ipadding, side=LEFT)
        self.save_directory_btn.pack(**UI.ipadding, side=RIGHT)

        self.window_frame.pack(expand=False, side=TOP)

# # # # # # # # # # # # #
# SINGLE USE FUNCTIONS  #
# # # # # # # # # # # # #

def createOpenDirectoryFromFileBtn(self) -> Button:
    """ [Function Docstring] """
    img_directory = DIR.app_directory + DIR.save
    self.save_dir_to_db = PhotoImage(file=img_directory)
    return Button(self.window_frame, image=self.save_dir_to_db)
