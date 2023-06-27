""" [DTOS DocString] """


class FileDTO:
    """ [Class DocString] """

    def __init__(self, file_ID, file_name, file_ext, file_size, num_lines, num_words, num_characters, folder_ID, directory_ID):
        """ [Function DocString] """

        # # # # # # # # # #
        # SQL ATTRIBUTES  #
        # # # # # # # # # #

        self.file_ID = file_ID
        self.file_name = file_name
        self.file_ext = file_ext
        self.file_size = file_size
        self.num_lines = num_lines
        self.num_words = num_words
        self.num_characters = num_characters
        self.folder_ID = folder_ID
        self.directory_ID = directory_ID

        # # # # # # # # # # # # #
        # CALCULATED ATTRIBUTES #
        # # # # # # # # # # # # #

        self.unique_lines = 0

        # # # # # # # # # # # #
        # PROGRAM ATTRIBUTES  #
        # # # # # # # # # # # #
        
        self.selected = False
        self.listbox_index = 0
