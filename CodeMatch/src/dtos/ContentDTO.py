""" [DTOS DocString] """


class ContentDTO:
    def __init__(self, content_ID, content_type, line_content, line_number, num_words, num_characters, file_ID, folder_ID, directory_ID):
        """ [Function DocString] """

        # # # # # # # # # #
        # SQL ATTRIBUTES  #
        # # # # # # # # # #

        self.content_ID = content_ID
        self.content_type = content_type
        self.line_content = line_content
        self.line_number = line_number
        self.num_words = num_words
        self.num_characters = num_characters
        self.file_ID = file_ID
        self.folder_ID = folder_ID
        self.directory_ID = directory_ID

        # # # # # # # # # # # #
        # PROGRAM ATTRIBUTES  #
        # # # # # # # # # # # #
