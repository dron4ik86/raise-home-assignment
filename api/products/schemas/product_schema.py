"""
Product validation schemas:
- schema: Single product validator (id, title, price, description, category, image, rating)
- product_schema: Accepts either single product or product array
"""

schema = {
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
        "rating": {
            "type": "object",
            "properties": {
                "rate": {"type": "number", "minimum": 0, "maximum": 5},
                "count": {"type": "integer", "minimum": 0}
            },
            "required": ["rate", "count"],
            "additionalProperties": False
        }
    },
    "required": ["id", "title", "price", "description", "category", "image", "rating"],
    "additionalProperties": False
}


product_schema = {
    "oneOf": [
        schema,
        {
            "type": "array",
            "items": schema
        }
    ]
}
