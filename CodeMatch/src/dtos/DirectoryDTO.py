"""" [DTOS DocString] """


class DirectoryDTO:
    """ [Class DocString] """

    def __init__(self, directory_ID, directory_name, directory_path, total_folders, total_files, root_folder_ID):
        """ [Function DocString] """

        # # # # # # # # # #
        # SQL ATTRIBUTES  #
        # # # # # # # # # #

        self.directory_ID = directory_ID
        self.directory_name = directory_name
        self.directory_path = directory_path
        self.total_folders = total_folders
        self.total_files = total_files
        self.root_folder_ID = root_folder_ID

        # # # # # # # # # # # #
        # PROGRAM ATTRIBUTES  #
        # # # # # # # # # # # #

        self.root_folder = None
