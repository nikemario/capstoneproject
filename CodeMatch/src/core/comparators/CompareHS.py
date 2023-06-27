""" [CompareHS.py Documentation] """
from src.core.Comparator import Comparator
from src.core.Database import Database


class CompareHS(Comparator):
    """ [Class DocString] """

    def __init__(self, left_directory, left_selected_files, right_directory, right_selected_files):
        super().__init__(left_directory, left_selected_files,
                         right_directory, right_selected_files)

        # self.thelist = None
        # self.listOfLineNumbers1 = None
        # self.listOfLineNumbers2 = None
        # self.listOfLineMatches = None
        # self.listOfFileNames1 = None
        # self.listOfFileNames2 = None

    def compare(self):
        """ [Function DocString] """
        # TODO Default Comparison Code

        # Queries all lines associated with the left and right directories
        query1 = f"select Content.line_content from Content where Content.directory_ID = '{self.left_directory_ID}'"
        query2 = f"select content.line_content from codematcher.content where content.directory_ID = '{self.right_directory_ID}'"

        # Queries the file names associated with the content from the left and right directories
        query3 = f"select file_name from `file` join content on content.file_ID = `file`.file_ID where content.directory_ID = '{self.left_directory_ID}'"
        query4 = f"select file_name from `file` join content on content.file_ID = `file`.file_ID where content.directory_ID = '{self.right_directory_ID}'"

        # Executes the first two queries and inserts the data into two lists
        tableData1 = self.database.EXECUTE(query1)
        tableData2 = self.database.EXECUTE(query2)

        # Executes the 3rd and 4th queries and inserts the data into two lists
        file_names_one = self.database.EXECUTE(query3)
        file_names_two = self.database.EXECUTE(query4)

        # Changes each line in the list to a string and inserts it into a new list
        tableData1_list_str = []
        for item in tableData1:
            tableData1_list_str.append(str(item))

        tableData2_list_str = []
        for item in tableData2:
            tableData2_list_str.append(str(item))

        # Removes unnecessary data from the list and inserts it into a new list
        tableData1_r = []
        for x in tableData1_list_str:
            x = x.removeprefix("(\'")
            x = x.removesuffix("\',)")
            x = x.replace("\\n", "").replace("\\\\n", "").replace("\\r", "").replace("\\\\r", "").replace(
                "\\t", "").replace("\\\\t", "").replace("\\f", "").replace("\\\\f", "").replace("\\\\", "")
            tableData1_r.append(x)

        tableData2_r = []
        for x in tableData2_list_str:
            x = x.removeprefix("(\'")
            x = x.removesuffix("\',)")
            x = x.replace("\\n", "").replace("\\\\n", "").replace("\\r", "").replace("\\\\r", "").replace(
                "\\t", "").replace("\\\\t", "").replace("\\f", "").replace("\\\\f", "").replace("\\\\", "")
            tableData2_r.append(x)

        # Comparison algorithm

        # Flag is used when there are no matches found
        flag = 1

        # the_list is used to hold all matches found
        the_list = []
        list_ofLineNumbers1 = []
        list_ofLineNumbers2 = []
        list_ofLineMatches = []
        list_ofFileNames1 = []
        list_ofFileNames2 = []

        # Outside if/elif/else is used to check the length of the lists to prevent input mismatch
        if len(tableData1_r) > len(tableData2_r):

            # Two for loops are used to index the lists
            for i in range(len(tableData1_r)):
                for j in range(len(tableData2_r)):

                    # If statement checks if there is a match
                    if tableData1_r[i] == tableData2_r[j]:

                        # If the match is an empty space, it skips the line
                        if tableData1_r[i] == "":
                            break

                        # The nonempty line is put into a string and then inserted into the_list
                        strr = f"Line {i+1} in {file_names_one[i][0]} matches line {j+1} in {file_names_two[j][0]} : {tableData1_r[i]}"
                        the_list.append(strr)
                        list_ofLineNumbers1.append(i+1)
                        list_ofLineNumbers2.append(j+1)
                        list_ofLineMatches.append(tableData1_r[i])
                        list_ofFileNames1.append(file_names_one[i][0])
                        list_ofFileNames2.append(file_names_two[j][0])

                        # Flag is set to 0 because there was at least one match
                        flag = 0

            # If no matches are found, then the_list reflects that
            if flag == 1:
                strr = "No matches found."
                the_list.append(strr)

        elif len(tableData1_r) < len(tableData2_r):

            # Two for loops are used to index the lists
            for i in range(len(tableData1_r)):
                for j in range(len(tableData2_r)):

                    # If statement checks if there is a match
                    if tableData2_r[j] == tableData1_r[i]:

                        # If the match is an empty space, it skips the line
                        if tableData1_r[i] == "":
                            break

                        # The nonempty line is put into a string and then inserted into the_list
                        strr = f"Line {i+1} in {file_names_one[i][0]} matches line {j+1} in {file_names_two[j][0]} : {tableData1_r[i]}"
                        the_list.append(strr)
                        list_ofLineNumbers1.append(i+1)
                        list_ofLineNumbers2.append(j+1)
                        list_ofLineMatches.append(tableData1_r[i])
                        list_ofFileNames1.append(file_names_one[i][0])
                        list_ofFileNames2.append(file_names_two[j][0])

                        # Flag is set to 0 because there was at least one match
                        flag = 0

            # If no matches are found, then the_list reflects that
            if flag == 1:
                strr = "No matches found."
                the_list.append(strr)

        elif len(tableData1_r) == len(tableData2_r):

            # Two for loops are used to index the lists
            for i in range(len(tableData1_r)):
                for j in range(len(tableData2_r)):

                    # If statement checks if there is a match
                    if tableData1_r[i] == tableData2_r[j]:

                        # If the match is an empty space, it skips the line
                        if tableData1_r[i] == "":
                            break

                        # The nonempty line is put into a string and then inserted into the_list
                        strr = f"Line {i+1} in {file_names_one[i][0]} matches line {j+1} in {file_names_two[j][0]} : {tableData1_r[i]}"
                        the_list.append(strr)
                        list_ofLineNumbers1.append(i+1)
                        list_ofLineNumbers2.append(j+1)
                        list_ofLineMatches.append(tableData1_r[i])
                        list_ofFileNames1.append(file_names_one[i][0])
                        list_ofFileNames2.append(file_names_two[j][0])

                        # Flag is set to 0 because there was at least one match
                        flag = 0

            # If no matches are found, then the_list reflects that
            if flag == 1:
                strr = "No matches found."
                the_list.append(strr)

        # This else statement should never execute because all possible list lengths are checked
        # If this executes, something is severely wrong
        else:
            print("You should not be here.")

        self.thelist = the_list
        self.listOfLineNumbers1 = list_ofLineNumbers1
        self.listOfLineNumbers2 = list_ofLineNumbers2
        self.listOfLineMatches = list_ofLineMatches
        self.listOfFileNames1 = list_ofFileNames1
        self.listOfFileNames2 = list_ofFileNames2

        print("[Comparison Results: HS]")
