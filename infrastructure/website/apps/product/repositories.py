from apps.product.models import Product as ProductModel

from service_product.application.dto import ProductDto
from service_product.application.storage import ProductStorage


# ProductStorage: Contrato de dados com a camada superior
class ProductRepository(ProductStorage):

    @staticmethod
    def _model_to_dto(product: ProductModel):
        """Parse from model to dto format"""
        return ProductDto(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            status=product.status,
        )

    def list_all_products(self) -> list[ProductDto]:
        """List all products."""
        products = ProductModel.objects.all()
        products_dto: list[ProductDto] = []
        for product in products:
            products_dto.append(self._model_to_dto(product))
        return products_dto

    @staticmethod
    def _product_dto_to_model(product_dto: ProductDto) -> ProductModel:
        """Convert a product model into a product model."""
        return ProductModel(**product_dto.to_dict())

    def save_product(self, product_dto: ProductDto):
        """Save a product."""
        product = self._product_dto_to_model(product_dto)
        product.save()
