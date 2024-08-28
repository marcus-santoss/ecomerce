import enum


class Constraints(enum.Enum):
    CUSTOMER_NAME_MIN_LENGTH: int = 6
    CUSTOMER_DOCUMENT_LENGTH: int = 11


class SuccessCodes(enum.Enum):
    SUCCESS: str = "Success"


class ErrorCodes(enum.Enum):
    CUSTOMER_NAME_CANNOT_BE_NONE_OR_BLANK: str = "Customer Name is required"
    CUSTOMER_EMAIL_CANNOT_BE_NONE_OR_BLANK: str = "Customer Email is required"
    CUSTOMER_DOCUMENT_HAS_INVALID_LEN: str = "Customer Document has invalid len"
    CUSTOMER_NAME_TOO_SHORT: str = "Customer name is too short"
    CUSTOMER_ALREADY_EXISTS: str = "Customer already exists"
    CUSTOMER_UNDEFINED_ERROR: str = "An undefined error occurred"
