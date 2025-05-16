from typing import Any

from pymilvus import CollectionSchema, FieldSchema
from sqlglot.expressions import ColumnDef, Create

from milvusdb.converter.const import (
    TypePyMilvus,
)
from milvusdb.converter.parse.base import get_table_name
from milvusdb.converter.parse.create.field import (
    get_length,
    get_name_column,
    get_type_column,
    is_auto_increment,
    is_primary_key,
)
from milvusdb.converter.parse.create.type import CollectionSchemaDict

from .index import get_field_index


def parse_table_create(table: Create) -> CollectionSchemaDict:
    columns = _parse_field(table.this.expressions)
    return CollectionSchemaDict(
        collection_name=get_table_name(table),
        collection_schema=CollectionSchema(
            fields=columns,
        ),
    )

def parse_index_create(index: Create) -> dict[str, Any]:
    return {
        "table_name": get_table_name(index),
        **get_field_index(index),
    }


def _parse_field(list_column: list[ColumnDef]) -> list[FieldSchema]:
    milvus_list_column = []
    for column in list_column:
        milvus_list_column.append(
            FieldSchema(
                **get_params_field(column),
            )
        )

    return milvus_list_column


def get_params_field(
    column: ColumnDef,
) -> dict[str, str | TypePyMilvus | bool]:
    dict_field = {
        "name": get_name_column(column),
        "dtype": get_type_column(column),
        "is_primary": is_primary_key(column),
        "auto_id": is_auto_increment(column),
        **get_length(column),
    }
    return {
        name_args_field: value_args_field
        for name_args_field, value_args_field in dict_field.items()
        if value_args_field is not None
    }
