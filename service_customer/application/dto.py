from dataclasses import dataclass

from service_customer.domain.entities import Customer


@dataclass
class CustomerDto:
    name: str
    email: str
    document: str
    id: int = None

    def __iter__(self):
        if self.id is not None:
            yield "id", self.id

        yield "name", self.name
        yield "email", self.email
        yield "document", self.document

    def to_dict(self):
        return dict(self)

    def to_domain(self):
        return Customer(self.name, self.email, self.document)
