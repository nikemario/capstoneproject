# # # # # # #
# BUILD DTO #
# # # # # # #

from src.core.Database import Database
from src.dtos.DirectoryDTO import DirectoryDTO
from src.dtos.FileDTO import FileDTO
from src.dtos.FolderDTO import FolderDTO

database = Database()


def buildDirectory(directory_ID) -> DirectoryDTO:
    directory = database.GET_DIRECTORY(directory_ID)

    if directory is not None:
        directory.root_folder = buildFolder(directory.root_folder_ID)

    return directory


def buildFolder(folder_ID) -> FolderDTO:
    folder = database.GET_FOLDER(folder_ID)

    selected_rows = database.SELECT(select_field="folder_ID",
                                    from_table="Folder",
                                    where_field="parent_folder_ID",
                                    equals_value=folder_ID)

    if selected_rows is not None:
        for child_folder_ID in selected_rows:
            folder.child_folders.append(buildFolder(child_folder_ID))

    selected_rows = database.SELECT(select_field="file_ID",
                                    from_table="File",
                                    where_field="folder_ID",
                                    equals_value=folder_ID)

    if selected_rows is not None:
        for child_file_ID in selected_rows:
            folder.child_files.append(buildFile(child_file_ID))

    return folder


def buildFile(file_ID) -> FileDTO:
    file = database.GET_FILE(file_ID)
    return file
