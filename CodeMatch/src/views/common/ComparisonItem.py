class ComparisonItem():
    def __init__(self, file_ID, matched_lines):

        self.file_ID = file_ID
        self.matched_lines = matched_lines # tuple of fileIDs
        # Dictionary {"content_ID: (content_ID, content_ID, ..., content_ID)"}
