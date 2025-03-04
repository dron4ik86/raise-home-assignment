from requests.exceptions import RequestException
import os


class Products:
    """
    Provides methods to interact with the products endpoint for retrieving,
    creating and deleting products.
    """
    def __init__(self, context):
        """Initialize with Behave context containing session and base URL."""
        self.context = context
        self.base_url = os.getenv('BASE_URL')
        self.endpoint = '/products'

    def get_products(self):
        """Get all products and assert successful response"""
        try:
            response = self.context.session.get(f"{self.base_url}{self.endpoint}", timeout=5)
            return response
        except RequestException as req_err:
            raise RuntimeError(f"Can't get all products: {req_err}") from None

    def get_product(self, product_id):
        """Get a single product by ID"""
        try:
            response = self.context.session.get(f"{self.base_url}{self.endpoint}/{product_id}", timeout=5)
            return response
        except RequestException as req_err:
            raise RuntimeError(f"Can't get product: {req_err}") from None

    def create_new_product(self, new_product_payload):
        """Create a product with the provided payload"""
        try:
            response = self.context.session.post(f"{self.base_url}{self.endpoint}", json=new_product_payload, timeout=5)
            return response
        except RequestException as req_err:
            raise RuntimeError(f"Can't create new product: {req_err}") from None

    def delete_product(self, product_id):
        """Delete a product by ID"""
        try:
            response = self.context.session.delete(f"{self.base_url}{self.endpoint}/{product_id}", timeout=5)
            return response
        except RequestException as req_err:
            raise RuntimeError(f"Can't delete product: {req_err}") from None
