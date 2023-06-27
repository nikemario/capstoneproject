""" [MainWindow.py Documentation] """
import tkinter as tk
from tkinter import *

from src.const.DIR import DIR
from src.const.UI import UI
from src.core.Database import Database
from src.views.common.ComparisonItem import ComparisonItem
from src.views.common.DirectoryListbox import DirectoryListbox


class ComparisonWindow(Toplevel):
    """ [Class DocString] """

    def __init__(self, comparator):

        self.database = Database()
        self.comparator = comparator

        # # # # # # # # # # # # # # #
        # CREATE COMPARISON WINDOW  #
        # # # # # # # # # # # # # # #

        # Main Window
        self.root = Tk()
        self.root.title("Code Match")
        self.root.state("zoomed")
        self.root.configure(bg=UI.background)

        # # # # # # # # # # # # # #
        # ITEM INFORMATION PANEL  #
        # # # # # # # # # # # # # #
        # TODO

        # # # # # # # # # # # #
        # COMPARISON SUMMARY  #
        # # # # # # # # # # # #
        # TODO

        self.left_directory_IDs = {}
        self.right_directory_IDs = {}

        self.top_frame = Frame(self.root, bg=UI.background)
        # self.comparison_summary = LabelFrame(self.top_frame,
        #                                      text='Comparison Summary',
        #                                      bg=UI.background, fg=UI.foreground)

        # self.select_comparator_label = Label(self.comparison_summary, text="SUMMARY:")
        # self.select_comparator_label.pack(**UI.ipadding, side=LEFT)

        # self.comparison_summary.pack(UI.frame_padding, **UI.ipadding, fill=X)
        self.top_frame.pack(UI.frame_arch_padding, fill=X, side=TOP)

        self.comparison_listbox = Listbox(self.top_frame)
        self.comparison_listbox.configure(selectmode="single",
                                          exportselection=False)

        # self.the_list_test.insert(END, *self.comparator.thelist)
        self.comparison_listbox.pack(expand=True, fill=BOTH, side=TOP)

        # # # # # # # # # #
        # DIRECTORY VIEWS #
        # # # # # # # # # #

        # TODO EXPORT SELECTED ITEM

        # LEFT DIRECTORY #

        self.left_directory_listbox = DirectoryListbox(self.root)
        self.left_directory_listbox.openDirectory(self.comparator.left_directory_ID,
                                                  self.comparator.left_selected_files)
        
        self.left_directory_listbox.bind("<<ListboxSelect>>", self.filterLeftDirectory, "+")
        self.left_directory_listbox.pack(UI.frame_bottomleft_padding,
                                         expand=True, fill=BOTH, side=LEFT)
        
        
        # RIGHT DIRECTORY #

        self.right_directory_listbox = DirectoryListbox(self.root)
        self.right_directory_listbox.openDirectory(self.comparator.right_directory_ID,
                                                  self.comparator.right_selected_files)
        
        self.right_directory_listbox.bind("<<ListboxSelect>>", self.filterLeftDirectory, "+")
        self.right_directory_listbox.pack(UI.frame_bottomright_padding,
                                          expand=True, fill=BOTH, side=RIGHT)

        # TODO Create FileContentWindow for "open file button"

    def filterLeftDirectory(self, event):
        selection = event.widget.curselection()

        if selection:
            self.comparison_listbox.delete(0, END)
            left_selected_indices = self.left_directory_listbox.curselection()

            for selected_index in left_selected_indices:

                directory_item = self.left_directory_listbox.directory_items.get(selected_index)
                self.comparison_listbox.insert(END, directory_item.item_string)
                item_index = self.comparison_listbox.size()-1
                
                if directory_item.isFile():
                    indent = self.countIndent(directory_item.item_string)
                    self.insertLeftComparisons(directory_item.item_ID, indent)
                    # self.left_directory_IDs.update({directory_item.item_ID: item_index})

    def insertLeftComparisons(self, file_ID, indent):
        left_results = self.comparator.left_directory_results.get(file_ID)

        for content_ID, matched_content_IDs in left_results.items():

            content_strings = []
            content_string = f"{indent}        Content ID: {content_ID}"

            line_number = self.database.SELECT(select_field="line_number",
                                               from_table="Content",
                                               where_field="content_ID",
                                               equals_value=content_ID)
            
            if line_number is not None:
                line_number = line_number[0]
                content_string = f"{indent}    Line: {line_number}"

            for matched_content_ID in matched_content_IDs:
                right_file_ID = self.database.SELECT(select_field="line_number",
                                                        from_table="Content",
                                                        where_field="content_ID",
                                                        equals_value=content_ID)
                if right_file_ID is not None:
                    right_file_ID = right_file_ID[0]
                    if right_file_ID in self.right_directory_listbox.getSelectedFileIDs():

                        right_line_number = self.database.SELECT(select_field="line_number",
                                                                 from_table="Content",
                                                                 where_field="content_ID",
                                                                 equals_value=matched_content_ID)
                        
                        right_file_name = self.database.SELECT(select_field="file_name",
                                                                 from_table="File",
                                                                 where_field="file_ID",
                                                                 equals_value=right_file_ID)                        
                        
                        content_strings.append(f"{indent}                Line: {right_line_number[0]}    {right_file_name[0]}")

            if len(content_strings) > 0:
                self.comparison_listbox.insert(END, content_string)
                self.comparison_listbox.insert(END, *content_strings)
    
    def countIndent(self, item_string):
        indent = ""

        for character in range(0, len(item_string)):
            if item_string[character] == " ":
                indent = indent + " "
        
        return indent
