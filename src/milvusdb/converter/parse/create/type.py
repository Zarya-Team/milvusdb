from typing import NamedTuple, TypedDict

from pymilvus import CollectionSchema


class CollectionSchemaAdnName(NamedTuple):
    collection_name: str
    collection_schema: CollectionSchema


class CollectionSchemaDict(TypedDict):
    collection_name: str
    collection_schema: CollectionSchema
