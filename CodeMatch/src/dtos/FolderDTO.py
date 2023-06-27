""" [DTOS DocString] """


class FolderDTO:
    """ [Class DocString] """

    def __init__(self, folder_ID, folder_name, folder_path, num_folders,
                 num_files, parent_folder_ID, directory_ID):
        """ [Function DocString] """

        # # # # # # # # # #
        # SQL ATTRIBUTES  #
        # # # # # # # # # #

        self.folder_ID = folder_ID
        self.folder_name = folder_name
        self.folder_path = folder_path
        self.num_folders = num_folders
        self.num_files = num_files
        self.parent_folder_ID = parent_folder_ID
        self.directory_ID = directory_ID

        # # # # # # # # # # # # #
        # CALCULATED ATTRIBUTES #
        # # # # # # # # # # # # #

        self.child_folders = []
        self.child_files = []

        # # # # # # # # # # # #
        # PROGRAM ATTRIBUTES  #
        # # # # # # # # # # # #

        self.selected = False
        self.listbox_index = 0
