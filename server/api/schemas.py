from typing import List, Optional

from ninja import ModelSchema, Schema

from api.models import Media, Product


class BaseResponseSchema(Schema):
    status: str = "success"
    count: Optional[int] = 1


class MediaSchema(ModelSchema):
    class Config:
        model = Media
        model_fields = ["id", "image", "alt_text"]


class ProductSchema(ModelSchema):
    image: MediaSchema

    class Config:
        model = Product
        model_fields = [
            "id",
            "name",
            "price",
            "description",
            "category",
            "amount",
            "is_featured",
            "rating",
            "ratings_count",
        ]


class ProductsListResponseSchema(BaseResponseSchema):
    data: List[ProductSchema]


class NotFoundSchema(Schema):
    message: str
