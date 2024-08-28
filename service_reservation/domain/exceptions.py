class ReservationProductNotFoundException(Exception):
    def __init__(self, message):
        self.message = message


class ReservationCustomerNotFoundException(Exception):
    def __init__(self, message):
        self.message = message


class ReservationProductUnavailableException(Exception):
    def __init__(self, message):
        self.message = message


class ReservationAlreadyExists(Exception):
    def __init__(self, message):
        self.message = message
