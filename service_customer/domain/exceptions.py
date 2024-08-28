class CustomerNameCannotBeNoneOrBlankException(Exception):
    def __init__(self, message):
        self.message = message


class CustomerEmailCannotBeNoneOrBlankException(Exception):
    def __init__(self, message):
        self.message = message


class CustomerNameTooShortException(Exception):
    def __init__(self, message):
        self.message = message


class CustomerDocumentInvalidLength(Exception):
    def __init__(self, message):
        self.message = message
