class DirectoryItem():
    def __init__(self, file_type, item_ID, item_string, item_index, parent_index):

        self.file_type = file_type
        self.item_ID = item_ID
        
        self.item_index = item_index
        self.parent_index = parent_index

        self.item_string = item_string
        self.selectable = False
        self.child_indices = []
        
    def isFile(self):
        if self.file_type == "FILE":
            return True
        return False
    
    def isFolder(self):
        if self.file_type == "FOLDER":
            return True
        return False
    
    def isSelectable(self):
        return self.selectable

