import enum


class SuccessCodes(enum.Enum):
    PRODUCT_RESERVED_WITH_SUCCESS: str = "This product was reserved with success"


class ErrorCodes(enum.Enum):
    RESERVATION_PRODUCT_NOT_FOUND: str = "This product was not found"
    RESERVATION_CUSTOMER_NOT_FOUND: str = "This customer was not found"
    RESERVATION_PRODUCT_UNAVAILABLE: str = "This product is unavailable"
    RESERVATION_UNDEFINED_ERROR: str = "An undefined error occurred"
    RESERVATION_ALREADY_EXISTS: str = "This reservation has already been registered"
