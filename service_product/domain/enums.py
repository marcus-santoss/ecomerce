import enum


class ProductStatusCodes(enum.Enum):
    PRODUCT_AVAILABLE = "AVAILABLE"
    PRODUCT_RESERVED = "RESERVED"
    PRODUCT_UNAVAILABLE = "UNAVAILABLE"


class SuccessCodes(enum.Enum):
    SUCCESS: str = "Success"


class ErrorCodes(enum.Enum):
    PRODUCT_NAME_CANNOT_BE_BLANK_OR_NONE: str = "Product name is required"
    PRODUCT_WITH_INVALID_PRICE: str = "This product has invalid price"
    PRODUCT_WITH_INVALID_STATUS_FOR_SAVE: str = (
        "This product has an invalid status for saving in the database"
    )
    PRODUCT_UNDEFINED_ERROR: str = "An undefined error occurred"
    PRODUCT_ALREADY_EXISTS: str = "This product has already been registered"
