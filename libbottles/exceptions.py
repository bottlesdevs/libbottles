class NoConnection(Exception):
    '''
    Raised when there is no internet connection.
    '''

    def __init__(self):
        self.message = f"Unable to establish an internet connection."
        super().__init__()
