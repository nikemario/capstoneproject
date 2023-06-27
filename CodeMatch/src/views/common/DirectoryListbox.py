from tkinter import *

from src.const.DIR import DIR
from src.const.UI import UI
from src.core.Database import Database
from src.views.common.DirectoryItem import DirectoryItem


class DirectoryListbox(Listbox):
    """ [Class DocString] """

    def __init__(self, master):
        super().__init__(master, bg=UI.background, exportselection=False,
                         fg=UI.foreground, selectmode="multiple")

        # self.configure()

        self.database = Database()

        self.directory_ID = 0
        self.directory_items = {}
        self.selected_file_IDs = None

        self.last_curselection = []

        self.bind("<<ListboxSelect>>", self.selectItem)

    # # # # # # # # # #
    # LOAD DIRECTORY  #
    # # # # # # # # # #

    def openDirectory(self, directory_ID, selected_file_IDs):
        self.directory_ID = directory_ID
        self.selected_file_IDs = selected_file_IDs

        returned_row = self.database.SELECT(select_field="root_folder_ID",
                                              from_table="Directory",
                                              where_field="directory_ID",
                                              equals_value=directory_ID)

        if returned_row is not None:
            root_folder_ID = returned_row[0]
            self.insertFolderItem(root_folder_ID, None, 0)

    def clearDirectory(self):
        self.directory_ID = 0
        self.directory_items = {}
        self.selected_file_IDs = None
        self.last_curselection = []
        self.delete(0, END)

    # # # # # # # # # # # # # #
    # INSERT DIRECTORY ITEMS  #
    # # # # # # # # # # # # # #

    def insertFolderItem(self, folder_ID, parent_index, level):
        item_index = None
        
        returned_row = self.database.SELECT(select_field="folder_name",
                                            from_table="Folder",
                                            where_field="folder_ID",
                                            equals_value=folder_ID)

        if returned_row is not None:
            folder_name = returned_row[0]
            string_indent = "    " * level
            item_string = string_indent + folder_name

            self.insert(END, item_string)
            self.itemconfigure(END, background=UI.shadow)

            item_index = self.size()-1

            folder_item = DirectoryItem("FOLDER", folder_ID, item_string, item_index, parent_index)
            self.itemconfigure(item_index, foreground=UI.overcast)

            child_folder_IDs = self.database.SELECT(select_field="folder_ID",
                                                    from_table="Folder",
                                                    where_field="parent_folder_ID",
                                                    equals_value=folder_ID)

            if child_folder_IDs is not None:
                for child_folder_ID in child_folder_IDs:
                    child_folder_index = self.insertFolderItem(child_folder_ID, item_index, level+1)
                    if child_folder_index is not None:
                        folder_item.child_indices.append(child_folder_index)

            child_file_IDs = self.database.SELECT(select_field="file_ID",
                                                  from_table="File",
                                                  where_field="folder_ID",
                                                  equals_value=folder_ID)

            if child_file_IDs is not None:
                for child_file_ID in child_file_IDs:
                    child_file_index = self.insertFileItem(child_file_ID, item_index, level+1)

                    if child_file_index is not None:
                        folder_item.child_indices.append(child_file_index)
                        
                        if(self.directory_items.get(child_file_index).selectable):
                            folder_item.selectable = True
                            self.itemconfigure(item_index, foreground=UI.foreground)

            self.directory_items.update({item_index: folder_item})

        return item_index 

    def insertFileItem(self, file_ID, parent_index, level):
        item_index = None

        returned_row = self.database.SELECT(select_field="file_name",
                                            from_table="File",
                                            where_field="file_ID",
                                            equals_value=file_ID)

        if returned_row is not None:
            file_name = returned_row[0]

            string_indent = "    " * level
            item_string = string_indent + file_name
            self.insert(END, item_string)

            item_index = self.size()-1
            file_item = DirectoryItem("FILE", file_ID, item_string, item_index, parent_index) 

            selectable = True
            if self.selected_file_IDs is not None:
                if file_ID not in self.selected_file_IDs:
                    selectable = False
                    self.itemconfigure(item_index, foreground=UI.overcast)
            file_item.selectable = selectable

            self.directory_items.update({item_index: file_item})

        return item_index

    # # # # # # # # # # # # # # 
    # SELECT EVENT FUNCTIONS  # 
    # # # # # # # # # # # # # #
    
    def selectItem(self, event):
        selection = event.widget.curselection()

        if selection:
            item_index = self.lastClickedItemIndex()
            item = self.directory_items.get(item_index)
            if item.selectable:
                if item.isFolder():
                    if self.isSelected(item_index):
                        self.selectFolderItem(item)
                    else:
                        self.deselectFolderItem(item)
                        self.deselectParentFolders(item)
                else:
                    if not self.isSelected(item_index):
                        self.deselectParentFolders(item)
            else:
                self.selection_clear(item_index)

        self.last_curselection = self.curselection()

    def selectFolderItem(self, item):
        self.selection_set(item.item_index)

        for child_index in item.child_indices:
            child_item = self.directory_items.get(child_index)

            if child_item.selectable:
                if child_item.isFolder():
                    self.selectFolderItem(child_item)
                else:
                    self.selection_set(child_index)
    
    def deselectFolderItem(self, item):
        self.selection_clear(item.item_index)
        
        for child_index in item.child_indices:
            child_item = self.directory_items.get(child_index)

            if child_item.isFolder():
                self.deselectFolderItem(child_item)
            else:
                self.selection_clear(child_index)
    
    def deselectParentFolders(self, item):
        self.selection_clear(item.item_index)

        if item.parent_index is not None:
            parent_item = self.directory_items.get(item.parent_index)
            self.deselectParentFolders(parent_item)

    # FUNCTIONS

    def lastClickedItemIndex(self):
        for item_index in self.curselection():
            if not item_index in self.last_curselection:
                return item_index

        for item_index in self.last_curselection:
            if not item_index in self.curselection():
                return item_index

    def isSelected(self, item_index):
        selection = self.curselection()

        if selection:
            if item_index in selection:
                return True

        return False

    # def setSelectedFileIDs(self, selected_file_IDs):
    #     self.selected_file_IDs = selected_file_IDs

    # def filterSelectedFileIDs(self):
    #     print()

    def getSelectedFileIDs(self):
        selected_file_IDs = []

        for item_index in self.curselection():
            item = self.directory_items.get(item_index)
            if item.isFile() and item.selectable:
                selected_file_IDs.append(item.item_ID)

        if not selected_file_IDs:
            for key, item in self.directory_items.items():
                if item.isFile() and item.selectable:
                    selected_file_IDs.append(item.item_ID)

        selected_file_IDs = tuple(selected_file_IDs)
        return selected_file_IDs
