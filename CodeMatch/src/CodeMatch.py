""" [CodeMatch.py Documentation] """
import os
import tkinter as tk
from functools import partial
from pathlib import Path
from tkinter import *
from tkinter import filedialog

from src.const.DIR import DIR
from src.const.UI import UI
from src.core.Comparator import Comparator
from src.core.comparators.CompareDML import CompareDML
from src.core.comparators.CompareHS import CompareHS
from src.core.Database import Database
from src.views.ComparisonWindow import ComparisonWindow
from src.views.DirectoryFrame import DirectoryFrame


class CodeMatch:
    """ [Class DocString] """

    def __init__(self):

        self.database = Database()
        self.comparator = Comparator(None, (), None, ())  # Empty Comparator

        available_comparators = [
            "Comparator",
            "CompareDML",
            "CompareHS"
        ]

        # # # # # # # # # # # #
        # CREATE MAIN WINDOW  #
        # # # # # # # # # # # #

        # Main Window
        self.root = Tk()
        self.root.title("Code Match")
        self.root.state("zoomed")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)

        imgicon = PhotoImage(file=DIR.app_directory + DIR.app_icon)
        self.root.iconphoto(True, imgicon)

        self.root.configure(bg=UI.background)

        # TODO [File]
        # TODO [Edit]
        # TODO [Database]
        # TODO [Help]

        # # # # # # # # # # # #
        # COMPARISON OPTIONS  #
        # # # # # # # # # # # #

        comparison_options = Frame(self.root, bg=UI.background)

        select_comparator_label = Label(comparison_options,
                                        text="Select Comparison Tool")

        self.selected_comparator = tk.StringVar()
        self.selected_comparator.set(available_comparators[0])
        self.select_comparator = OptionMenu(comparison_options,
                                            self.selected_comparator,
                                            *available_comparators)

        self.compare_btn = createCompareDirectoriesButton(comparison_options)
        self.compare_btn.configure(command=partial(self.compare))

        self.compare_btn.pack(side=RIGHT)
        select_comparator_label.pack(**UI.ipadding, side=LEFT)
        self.select_comparator.pack(UI.padding, side=LEFT)
        comparison_options.pack(UI.frame_arch_padding, fill=X, side=TOP)

        # # # # # # # # # # # # #
        # LEFT DIRECTORY FRAME  #
        # # # # # # # # # # # # #

        self.left_directory = DirectoryFrame(self.root) 
        self.left_directory.pack(UI.frame_bottomleft_padding, expand=True,
                                 fill=BOTH, side=LEFT)

        # # # # # # # # # # # # #
        # RIGHT DIRECTORY FRAME #
        # # # # # # # # # # # # #

        self.right_directory = DirectoryFrame(self.root)
        self.right_directory.pack(UI.frame_bottomright_padding, expand=True,
                                  fill=BOTH, side=RIGHT)

    # # # # # # # # # # #
    # RUNS THE PROGRAM  #
    # # # # # # # # # # #

    def run(self):
        """ Runs the developing program. """
        self.root.mainloop()

    # # # # # # # # # # #
    # COMPARE FUNCTIONS #
    # # # # # # # # # # #

    def compare(self):
        """ [Function DocString] """

        # LEFT DIRECTORY
        left_directory_ID = self.left_directory.directory_ID
        left_selected_files = self.left_directory.directory_listbox.getSelectedFileIDs()

        # RIGHT DIRECTORY
        right_directory_ID = self.right_directory.directory_ID
        right_selected_files = self.right_directory.directory_listbox.getSelectedFileIDs()

        match self.selected_comparator.get():
            case "CompareDML":
                self.comparator = CompareDML(left_directory_ID,
                                             left_selected_files,
                                             right_directory_ID,
                                             right_selected_files)
            case "CompareHS":
                self.comparator = CompareHS(left_directory_ID,
                                            left_selected_files,
                                            right_directory_ID,
                                            right_selected_files)
            case _:
                # Update default comparator with directory information
                self.comparator = Comparator(left_directory_ID,
                                             left_selected_files,
                                             right_directory_ID,
                                             right_selected_files)

        # RUN COMPARISON
        self.comparator.compare()

        # Create Comparison Window
        comparison_window = ComparisonWindow(self.comparator)
        comparison_window.root.protocol("WM_DELETE_WINDOW",
                                        comparison_window.root.destroy)

    # # # # # # # # # # #
    # QUITS THE PROGRAM #
    # # # # # # # # # # #

    def quit(self):
        self.left_directory.clickClearDirectory()
        self.right_directory.clickClearDirectory()
        self.root.quit()

# # # # # # # # # # # # #
# SINGLE USE FUNCTIONS  #
# # # # # # # # # # # # #


def createCompareDirectoriesButton(master) -> Button:
    """ [Function Docstring] """
    img_directory = DIR.app_directory + DIR.compare
    master.btn_img = PhotoImage(file=img_directory)
    return Button(master, image=master.btn_img)
