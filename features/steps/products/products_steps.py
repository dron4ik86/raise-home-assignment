from behave import step
from api.products.products import Products
from jsonschema import ValidationError, validate
from api.products.schemas.product_schema import product_schema
from api.products.schemas.create_product_schema import create_schema



@step('I send a GET request to fetch all products')
def step_impl(context):
    context.response = Products(context).get_products()


@step("the response should match the expected product schema")
def step_impl(context):
    try:
        validate(instance=context.response.json(), schema=product_schema)
    except ValidationError as e:
        raise ValidationError(f"Validation failed: {e}")


@step("I send a GET request to fetch product with ID {product_id}")
def step_impl(context, product_id):
    context.response = Products(context).get_product(product_id)


@step("the response status should be {status_code:d}")
def step_impl(context, status_code):
    assert context.response.status_code == status_code, f"Expected {status_code}, but got {context.response.status_code}"


@step('I send a POST request with valid product data')
def step_impl(context):
    new_product = {
        "id": 0,
        "title": context.fake.paragraph(),
        "price": 0.1,
        "description": context.fake.text(max_nb_chars=300),
        "category": "jewelery",
        "image": "https://picsum.photos/200/300"
    }
    context.response = Products(context).create_new_product(new_product)


@step("the response should match the expected create product schema")
def step_impl(context):
    try:
        validate(instance=context.response.json(), schema=create_schema)
    except ValidationError as e:
        raise ValidationError(f"Validation failed: {e}")


@step('I send a POST request with invalid data')
def step_impl(context):
    invalid_data = {}
    context.response = Products(context).create_new_product(invalid_data)


@step('I send a DELETE request to delete product with ID {product_id}')
def step_impl(context, product_id):
    context.response = Products(context).delete_product(product_id)
