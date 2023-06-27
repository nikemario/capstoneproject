""" [CompareDML.py Documentation] """
from src.core.Comparator import Comparator
from src.core.Database import Database
from src.dtos.ContentDTO import ContentDTO
from src.dtos.DirectoryDTO import DirectoryDTO
from src.dtos.FileDTO import FileDTO
from src.dtos.FolderDTO import FolderDTO


class CompareDML(Comparator):
    """ [Class DocString] """

    def compare(self):
        """ [Function DocString] """

        print("[Comparison Results: DML]")

        for file_ID in self.left_selected_files:
            file_content_IDs = {}
            content_IDs = self.database.SELECT(select_field="content_ID",
                                                    from_table="Content",
                                                    where_field="file_ID",
                                                    equals_value=file_ID)
            
            if content_IDs is not None:
                
                for content_ID in content_IDs:
                    matched_content_IDs = []
                    line_content = self.database.SELECT(select_field="line_content",
                                                        from_table="Content",
                                                        where_field="content_ID",
                                                        equals_value=content_ID)
                    if line_content is not None:
                        line_content = line_content[0]

                        for right_file_ID in self.right_selected_files:
                            STATEMENT = f"""\
                                SELECT content_ID
                                FROM Content
                                WHERE Content.line_content='{line_content}'
                                AND Content.file_ID='{right_file_ID}';"""
                            
                            right_content_IDs = self.database.EXECUTE(STATEMENT)

                            if right_content_IDs is not None:
                                for right_content_ID in right_content_IDs:
                                    matched_content_IDs.append(right_content_ID[0])
                    
                    file_content_IDs.update({content_ID: tuple(matched_content_IDs)})
            self.left_directory_results.update({file_ID: file_content_IDs})

    # FUNCTIONS

    # def compareDirectory(self, directory, selected_files, compare_to_files):
    #     # compare code here
    #     self.compareFolder(directory.root_folder,
    #                        selected_files, compare_to_files)

    # def compareFolder(self, folder, selected_files, compare_to_files):

    #     # for child_folder in folder.child_folders:
    #     # code

    #     for child_file in folder.child_files:
    #         self.compareFile(child_file, selected_files, compare_to_files)

    # def compareFile(self, file, selected_files, compare_to_files):

    #     if file.file_ID in selected_files:

    #         if len(compare_to_files) == 1:
    #             compare_to_files = f"({compare_to_files[0]})"

    #         STATEMENT = f"SELECT COUNT(DISTINCT C1.content_ID) FROM Content C1, Content C2 WHERE C1.line_content=C2.line_content AND C1.file_ID={file.file_ID} AND C2.content_ID IN {compare_to_files};"
    #         selected_rows = self.database.EXECUTE(STATEMENT)

    #         if selected_rows is not None:
    #             matched_lines = selected_rows[0][0]
    #             file.unique_lines = int(file.num_lines)-int(matched_lines)
