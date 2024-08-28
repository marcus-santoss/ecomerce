class ProductNameCannotBeBlankOrNoneException(Exception):
    def __init__(self, message):
        self.message = message


class ProductWithInvalidPriceException(Exception):
    def __init__(self, message):
        self.message = message


class ProductWithInvalidStatusOnSavingException(Exception):
    def __init__(self, message):
        self.message = message
