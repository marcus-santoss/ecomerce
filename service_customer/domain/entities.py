from dataclasses import dataclass

from service_customer.domain.enums import Constraints
from service_customer.domain.exceptions import (
    CustomerDocumentInvalidLength,
    CustomerEmailCannotBeNoneOrBlankException,
    CustomerNameCannotBeNoneOrBlankException,
    CustomerNameTooShortException,
)


@dataclass
class Customer:
    name: str
    email: str
    document: str
    id: int = None

    def is_valid(self):
        if self.name is None:
            raise CustomerNameCannotBeNoneOrBlankException(
                "Customer name cannot be blank or None"
            )

        if self.email is None:
            raise CustomerEmailCannotBeNoneOrBlankException(
                "Customer email cannot be blank or None"
            )

        if len(self.name) < Constraints.CUSTOMER_NAME_MIN_LENGTH.value:
            raise CustomerNameTooShortException("Customer name is too short")

        if len(self.document) != Constraints.CUSTOMER_DOCUMENT_LENGTH.value:
            raise CustomerDocumentInvalidLength("Customer document has invalid length")

        return True
