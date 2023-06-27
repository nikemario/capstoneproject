class DB:

    # CONNECT
    db_username = "codematch"
    db_password = "codematchpassword"
    db_host = "127.0.0.1"
    db_schema = "CodeMatcher"

    # # # # # # # # # # # # # # #
    # Database String Constants #
    # # # # # # # # # # # # # # #

    # Directory Table
    directory_table = "Directory"
    directory_fields = (
        "directory_ID",
        "directory_name",
        "directory_path",
        "total_folders",
        "total_files",
        "root_folder_ID"
    )

    # Folder Table
    folder_table = "Folder"
    folder_fields = (
        "folder_ID",
        "folder_name",
        "folder_path",
        "num_folders",
        "num_files",
        "parent_folder_ID",
        "directory_ID"
    )

    # File Table
    file_table = "File"
    file_fields = (
        "file_ID",
        "file_name",
        "file_ext",
        "file_size",
        "num_lines",
        "num_words",
        "num_characters",
        "folder_ID",
        "directory_ID"
    )

    # Content Table
    content_table = "Content"
    content_fields = (
        "content_ID",
        "content_type",
        "line_content",
        "line_number",
        "num_words",
        "num_characters",
        "file_ID",
        "folder_ID",
        "directory_ID"
    )

    # Database Tables
    database_tables = (
        directory_table,
        folder_table,
        file_table,
        content_table
    )

    # Database Table Fields
    database_table_fields = {
        directory_table: directory_fields,
        folder_table: folder_fields,
        file_table: file_fields,
        content_table: content_fields
    }
