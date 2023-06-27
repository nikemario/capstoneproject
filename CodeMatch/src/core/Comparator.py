""" [Comparator.py Documentation] """

from src.core.Database import Database
from src.dtos.ContentDTO import ContentDTO
from src.dtos.DirectoryDTO import DirectoryDTO
from src.dtos.FileDTO import FileDTO
from src.dtos.FolderDTO import FolderDTO


class Comparator:
    """ [Class DocString] """

    def __init__(self, left_directory_ID, left_selected_files, right_directory_ID, right_selected_files):
        """ [Function DocString] """

        self.database = Database()

        # LEFT DIRECTORY
        self.left_directory_ID = left_directory_ID
        self.left_selected_files = left_selected_files

        # RIGHT DIRECTORY
        self.right_directory_ID = right_directory_ID
        self.right_selected_files = right_selected_files

        # COMPARISON RESULTS
        self.left_directory_results = {}
        self.right_directory_results = {}

    def compare(self):
        """ [Function DocString] """
        # TODO Default Comparison Code
        print("[Comparison Results: ]")
