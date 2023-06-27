"""
All-Purpose SQL Database Handlers
    Select Statments
    Update Statements
    Delete Statements

AUTOMATED PROGRAM DATABASE HANDLERS
"""
import mysql.connector

from src.const.DB import DB
from src.dtos.ContentDTO import ContentDTO
from src.dtos.DirectoryDTO import DirectoryDTO
from src.dtos.FileDTO import FileDTO
from src.dtos.FolderDTO import FolderDTO


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(user=DB.db_username,
                                                  password=DB.db_password,
                                                  host=DB.db_host,
                                                  database=DB.db_schema,
                                                  charset="utf8mb4",
                                                  collation="utf8mb4_unicode_ci",
                                                  use_unicode=True,
                                                  buffered=True)
    
    # # # # # # # # # # # # # # # # #
    # GENERALIZED EXECUTE STATEMENT #
    # # # # # # # # # # # # # # # # #

    def EXECUTE(self, STATEMENT) -> list[tuple]:

        returned_rows = [()]

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            if cursor.rowcount:
                returned_rows = cursor.fetchall()
            else:
                returned_rows = None

        return returned_rows
    
    # # # # # # # # # # # # # # # # # # #
    # ALL-PURPOSE SQL DATABASE HANDLERS #
    # # # # # # # # # # # # # # # # # # #

    def DELETE(self, table, where_field, equals_value):

        STATEMENT = f"""\
            DELETE FROM {table}
            WHERE {where_field}='{equals_value}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            self.connection.commit()
    
    def SELECT(self, select_field, from_table, where_field, equals_value) -> tuple:

        returned_rows = []

        STATEMENT = f"""\
            SELECT {select_field} 
            FROM {from_table} 
            WHERE {from_table}.{where_field}='{equals_value}';"""

        is_executable = True

        # CHECK IF SELECT STATEMENT IS EXECUTABLE
        if from_table in DB.database_tables:
            if select_field not in DB.database_table_fields[from_table]:
                print(
                    f"Database field '{select_field}' does not exist in '{from_table}' database table.")
                is_executable = False
            if where_field not in DB.database_table_fields[from_table]:
                print(
                    f"Database field '{where_field}' does not exist in '{from_table}' database table.")
                is_executable = False
        else:
            print(f"Database table '{from_table}' does not exist.")
            is_executable = False

        if is_executable:
            with self.connection.cursor() as cursor:
                cursor.execute(STATEMENT)

                if cursor.rowcount:
                    for row in cursor.fetchall():
                        returned_rows.append(row[0])
                    returned_rows = tuple(returned_rows)
                else:
                    returned_rows = None

        return returned_rows

    def SELECT_ALL(self, from_table, where_field, equals_value) -> list[tuple]:

        returned_rows = [()]

        STATEMENT = f"""\
            SELECT * FROM {from_table} 
            WHERE {from_table}.{where_field}='{equals_value}';"""

        is_executable = True

        # CHECK IF SELECT STATEMENT IS EXECUTABLE
        if from_table in DB.database_tables:
            if where_field not in DB.database_table_fields[from_table]:
                print(
                    f"Database field '{where_field}' does not exist in '{from_table}' database table.")
                is_executable = False
        else:
            print(f"Database table '{from_table}' does not exist.")
            is_executable = False

        if is_executable:
            with self.connection.cursor() as cursor:
                cursor.execute(STATEMENT)
                if cursor.rowcount:
                    returned_rows = cursor.fetchall()
                    returned_rows = tuple(returned_rows)
                else:
                    returned_rows = None
        else:
            print("Statement NOT Executed: ", STATEMENT)

        return returned_rows

    def UPDATE(self, update_table, set_field, to_value, where_field, equals_value):

        STATEMENT = f"""\
            UPDATE {update_table} 
            SET {set_field}='{to_value}' 
            WHERE {where_field}='{equals_value}';"""

        is_executable = True

        # CHECK IF UPDATE STATEMENT IS EXECUTABLE
        if update_table in DB.database_tables:
            if set_field not in DB.database_table_fields[update_table]:
                print(
                    f"Database field '{set_field}' does not exist in '{update_table}' database table.")
                is_executable = False
            if where_field not in DB.database_table_fields[update_table]:
                print(
                    f"Database field '{where_field}' does not exist in '{update_table}' database table.")
                is_executable = False
        else:
            print(f"Database table '{update_table}' does not exist.")
            is_executable = False

        if is_executable:
            with self.connection.cursor as cursor:
                cursor.execute(STATEMENT)
        else:
            print("Statement NOT Executed: ", STATEMENT)
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # AUTOMATED PROGRAM DATABASE HANDLERS # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # #
    # INSERT DIRECTORY TABLES #
    # # # # # # # # # # # # # #

    def INSERT_DIRECTORY(self, directory_name, directory_path):

        STATEMENT = f"""\
            INSERT INTO Directory (directory_name, directory_path) 
            VALUES ('{directory_name}', '{directory_path}');"""
        
        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            self.connection.commit()
            directory_ID = cursor.lastrowid

        return directory_ID

    def INSERT_FOLDER(self, folder_name, folder_path, directory_ID):

        STATEMENT = f"""\
            INSERT INTO Folder (folder_name, folder_path, directory_ID) 
            VALUES ('{folder_name}', '{folder_path}', '{directory_ID}');"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            self.connection.commit()
            folder_ID = cursor.lastrowid

        return folder_ID

    def INSERT_FILE(self, file_name, file_ext, folder_ID, directory_ID):

        STATEMENT = f"""\
            INSERT INTO File (file_name, file_ext, folder_ID, directory_ID) 
            VALUES ('{file_name}','{file_ext}','{folder_ID}','{directory_ID}');"""
            
        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            self.connection.commit()
            file_ID = cursor.lastrowid

        return file_ID

    def INSERT_CONTENT(self, line_content, line_number, file_ID, folder_ID, directory_ID):
        """ [Function DocString] """

        STATEMENT = f"""\
            INSERT INTO Content (line_content, line_number, file_ID, folder_ID, directory_ID)
            VALUES ('{line_content}', '{line_number}', '{file_ID}', '{folder_ID}', '{directory_ID}');"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            self.connection.commit()
            content_ID = cursor.lastrowid

        return content_ID

    # # # # # # # # # # # # # # #
    # COMPLETE DIRECTORY TABLES #
    # # # # # # # # # # # # # # #

    def COMPLETE_DIRECTORY(self, directory_ID):
        """ [Function DocString] """

        # total_folders
        STATEMENT = f"""\
            SELECT COUNT(folder_ID) AS total_folders 
            FROM Folder 
            WHERE Folder.directory_ID='{directory_ID}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            returned_rows = cursor.fetchone()
            if returned_rows is not None:
                for total_folders in returned_rows:
                    self.UPDATE_DIRECTORY("total_folders", total_folders, directory_ID)

        # total_files
        STATEMENT = f"""\
            SELECT COUNT(file_ID) AS total_files 
            FROM File 
            WHERE File.directory_ID='{directory_ID}';"""
        
        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            returned_rows = cursor.fetchone()
            if returned_rows is not None:
                for total_files in returned_rows:
                    self.UPDATE_DIRECTORY("total_files", total_files, directory_ID)

        # root_folder_ID
        STATEMENT = f"""\
            SELECT Folder.folder_ID 
            FROM Folder INNER JOIN Directory 
            ON Folder.directory_ID = Directory.directory_ID 
            WHERE Folder.folder_path = Directory.directory_path 
            AND Folder.directory_ID='{directory_ID}' 
            LIMIT 1;"""
        
        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            returned_rows = cursor.fetchone()
            if returned_rows is not None:
                for root_folder_ID in returned_rows:
                    self.UPDATE_DIRECTORY("root_folder_ID", root_folder_ID, directory_ID)


    def COMPLETE_FOLDER(self, folder_ID, directory_ID):

        # parent_folder_ID
        STATEMENT = f"""\
            SELECT folder_path 
            FROM Folder 
            WHERE folder_ID='{folder_ID}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            if cursor.rowcount:
                folder_path = cursor.fetchone()[0]
                parent_folder_path = folder_path[:folder_path.rfind("/")]
                parent_folder_path = folder_path[:parent_folder_path.rfind("/")+1]

                STATEMENT = f"""\
                    SELECT folder_ID AS parent_folder_ID 
                    FROM Folder 
                    WHERE folder_path='{parent_folder_path}' 
                    AND directory_ID='{directory_ID}';"""

                cursor.execute(STATEMENT)
                if cursor.rowcount:
                    parent_folder_ID = cursor.fetchone()[0]
                    cursor.execute(
                        f"UPDATE Folder SET Folder.parent_folder_ID='{parent_folder_ID}' WHERE Folder.folder_ID='{folder_ID}';")
                    self.connection.commit()

        # num_folders
        # STATEMENT = f"""\
        #     SELECT COUNT(folder_ID) AS num_folders 
        #     FROM Folder 
        #     WHERE Folder.parent_folder_ID='{folder_ID}';"""
        
        # with self.connection.cursor() as cursor:
        #     cursor.execute(STATEMENT)
        #     if cursor.rowcount:
        #         num_folders = cursor.fetchone()[0]
        #         self.UPDATE_FOLDER("num_folders", num_folders, folder_ID)

        # num_files
        STATEMENT = f"""\
            SELECT COUNT(file_ID) AS num_files 
            FROM File 
            WHERE File.folder_ID='{folder_ID}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            returned_rows = cursor.fetchone()
            if returned_rows is not None:
                for num_files in returned_rows:
                    self.UPDATE_FOLDER("num_files", num_files, folder_ID)

        cursor.close()

    def COMPLETE_FILE(self, file_ID, folder_ID, directory_ID):

        # num_lines
        STATEMENT = f"""\
            SELECT COUNT(content_ID) AS num_lines 
            FROM Content 
            WHERE Content.file_ID='{file_ID}';"""
        
        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            if cursor.rowcount:
                num_lines = cursor.fetchone()[0]
                self.UPDATE_FILE("num_lines", num_lines, file_ID)

    def COMPLETE_CONTENT(self, content_ID, num_words, num_characters):

        # num_words
        self.UPDATE_CONTENT("num_words", num_words, content_ID)

        # num_characters
        self.UPDATE_CONTENT("num_characters", num_characters, content_ID)

    # # # # # # # # # # # # # #
    # UPDATE DIRECTORY TABLES #
    # # # # # # # # # # # # # #

    # UPDATE_DIRECTORY
    def UPDATE_DIRECTORY(self, field, value, directory_ID):

        STATEMENT = f"""\
            UPDATE Directory 
            SET Directory.{field}='{value}' 
            WHERE Directory.directory_ID='{directory_ID}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            self.connection.commit()

    # UPDATE_FOLDER
    def UPDATE_FOLDER(self, field, value, folder_ID):

        STATEMENT = f"""\
            UPDATE Folder 
            SET Folder.{field}='{value}' 
            WHERE Folder.folder_ID='{folder_ID}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            self.connection.commit()

    # UPDATE_FILE
    def UPDATE_FILE(self, field, value, file_ID):

        STATEMENT = f"""\
            UPDATE File 
            SET File.{field}='{value}' 
            WHERE File.file_ID='{file_ID}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            self.connection.commit()

    # UPDATE_CONTENT
    def UPDATE_CONTENT(self, field, value, content_ID):

        STATEMENT = f"""\
            UPDATE Content 
            SET Content.{field}='{value}' 
            WHERE Content.content_ID='{content_ID}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            self.connection.commit()

    # # # # # # # # # # # # # #
    # DELETE DIRECTORY TABLES #
    # # # # # # # # # # # # # #

    def DELETE_DIRECTORY(self, directory_ID):

        self.DELETE("Content", "directory_ID", directory_ID)
        self.DELETE("File", "directory_ID", directory_ID)
        self.DELETE("Folder", "directory_ID", directory_ID)
        self.DELETE("Directory", "directory_ID", directory_ID)

    def DELETE_FOLDER(self, folder_ID):

        self.DELETE("Content", "folder_ID", folder_ID)
        self.DELETE("File", "folder_ID", folder_ID)
        self.DELETE("Folder", "folder_ID", folder_ID)

    def DELETE_FILE(self, file_ID):

        self.DELETE("Content", "file_ID", file_ID)
        self.DELETE("File", "file_ID", file_ID)

    def DELETE_CONTENT(self, content_ID):

        self.DELETE("Content", "content_ID", content_ID)

    # # # # # # # # # # #
    # GET DATABASE DTOS #
    # # # # # # # # # # #

    # GET DIRECTORY DTO
    def GET_DIRECTORY(self, directory_ID) -> DirectoryDTO:

        directory = None
        
        STATEMENT = f"""\
            SELECT * 
            FROM Directory 
            WHERE Directory.directory_ID='{directory_ID}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            if cursor.rowcount:
                directory_row = cursor.fetchone()

                directory_ID = directory_row[0]
                directory_name = directory_row[1]
                directory_path = directory_row[2]
                total_folders = directory_row[3]
                total_files = directory_row[4]
                root_folder_ID = directory_row[5]

                directory = DirectoryDTO(directory_ID,
                                         directory_name,
                                         directory_path,
                                         total_folders,
                                         total_files,
                                         root_folder_ID)

        return directory

    # GET FOLDER DTO
    def GET_FOLDER(self, folder_ID) -> FolderDTO:

        folder = None

        STATEMENT = f"""\
            SELECT * 
            FROM Folder 
            WHERE Folder.folder_ID='{folder_ID}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            if cursor.rowcount:
                folder_row = cursor.fetchone()

                folder_ID = folder_row[0]
                folder_name = folder_row[1]
                folder_path = folder_row[2]
                num_folders = folder_row[3]
                num_files = folder_row[4]
                parent_folder_ID = folder_row[5]
                directory_ID = folder_row[6]

                folder = FolderDTO(folder_ID,
                                   folder_name,
                                   folder_path,
                                   num_folders,
                                   num_files,
                                   parent_folder_ID,
                                   directory_ID)

        return folder

    # GET FILE DTO
    def GET_FILE(self, file_ID) -> FileDTO:

        file = None

        STATEMENT = f"""\
            SELECT * 
            FROM File 
            WHERE File.file_ID='{file_ID}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            if cursor.rowcount:
                file_row = cursor.fetchone()

                file_ID = file_row[0]
                file_name = file_row[1]
                file_ext = file_row[2]
                file_size = file_row[3]
                num_lines = file_row[4]
                num_words = file_row[5]
                num_characters = file_row[6]
                folder_ID = file_row[7]
                directory_ID = file_row[8]
                
                file = FileDTO(file_ID,
                               file_name,
                               file_ext,
                               file_size,
                               num_lines,
                               num_words,
                               num_characters,
                               folder_ID,
                               directory_ID)

        return file

    # GET CONTENT DTO
    def GET_CONTENT(self, content_ID) -> ContentDTO:

        content = None

        STATEMENT = f"""\
            SELECT * 
            FROM Content 
            WHERE Content.content_ID='{content_ID}';"""

        with self.connection.cursor() as cursor:
            cursor.execute(STATEMENT)
            if cursor.rowcount:
                content_row = cursor.fetchone()
                
                content_ID = content_row[0]
                content_type = content_row[1]
                line_content = content_row[2]
                line_number = content_row[3]
                num_words = content_row[4]
                num_characters = content_row[5]
                file_ID = content_row[6]
                folder_ID = content_row[7]
                directory_ID = content_row[8]

                ContentDTO(content_ID,
                           content_type,
                           line_content,
                           line_number,
                           num_words,
                           num_characters,
                           file_ID,
                           folder_ID,
                           directory_ID)

        return content

    # QUERIES FOR SPECIFIC INFORMATION #

    # def SELECT_PARENT_FOLDER_ID():
