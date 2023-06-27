DROP USER IF EXISTS 'codematch'@'127.0.0.1'; 
CREATE USER 'codematch'@'127.0.0.1' IDENTIFIED BY 'codematchpassword'; 
FLUSH PRIVILEGES; 
GRANT ALL PRIVILEGES ON * . * TO 'codematch'@'127.0.0.1';

DROP DATABASE IF EXISTS CodeMatcher;
CREATE DATABASE CodeMatcher CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE CodeMatcher;

GRANT ALL PRIVILEGES ON `CodeMatcher` . * TO 'codematch'@'127.0.0.1';

CREATE TABLE Directory(
	directory_ID INT NOT NULL AUTO_INCREMENT,
    directory_name VARCHAR(500) NOT NULL,
    directory_path VARCHAR(500) NOT NULL,
    total_folders INT,
    total_files INT,
    root_folder_ID INT,
    PRIMARY KEY (directory_ID)
);

CREATE TABLE Folder(
	folder_ID INT NOT NULL AUTO_INCREMENT,
    folder_name VARCHAR(500) NOT NULL,
    folder_path VARCHAR(500) NOT NULL,
    num_folders INT,
    num_files INT,
    parent_folder_ID INT, 
    directory_ID INT NOT NULL,
    PRIMARY KEY (folder_ID),
    FOREIGN KEY (directory_ID) REFERENCES Directory(directory_ID)
);

CREATE TABLE File(
	file_ID INT NOT NULL AUTO_INCREMENT,
    file_name VARCHAR(500) NOT NULL,
    file_ext VARCHAR(500) NOT NULL,
    file_size INT, 
    num_lines INT, 
    num_words INT,
    num_characters INT,
    folder_ID INT NOT NULL,
    directory_ID INT NOT NULL,
    PRIMARY KEY (file_ID),
    FOREIGN KEY (folder_ID) REFERENCES Folder(folder_ID),
    FOREIGN KEY (directory_ID) REFERENCES Directory(directory_ID)
); 
 
CREATE TABLE Content(
	content_ID INT NOT NULL AUTO_INCREMENT,
    content_type VARCHAR(500),
    line_content LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    line_number INT, 
    num_words INT,
    num_characters INT, 
    file_ID INT NOT NULL,
    folder_ID INT NOT NULL,
    directory_ID INT NOT NULL,
    PRIMARY KEY (content_ID),
    FOREIGN KEY (file_ID) REFERENCES File(file_ID),
    FOREIGN KEY (folder_ID) REFERENCES Folder(folder_ID),
    FOREIGN KEY (directory_ID) REFERENCES Directory(directory_ID)
);
