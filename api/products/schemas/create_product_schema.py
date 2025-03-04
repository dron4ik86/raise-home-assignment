"""
Schema for creating new products, requiring id, title, price, description, category, and image.
Rating is not required for product creation.
"""


create_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "title": {"type": "string", "maxLength": 300},
        "price": {"type": "number", "minimum": 0},
        "description": {"type": "string", "maxLength": 1000},
        "category": {
            "type": "string",
            "enum": [
                "men's clothing",
                "women's clothing",
                "jewelery",
                "electronics"
            ]
        },
        "image": {
            "type": "string",
            "format": "uri"
        },

    },
    "required": ["id", "title", "price", "description", "category", "image"],
    "additionalProperties": False
}
