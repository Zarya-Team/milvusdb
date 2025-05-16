from typing import Any

from sqlglot.expressions import Array, Insert, Schema, Values

from milvusdb.converter.parse.base import get_table_name
from milvusdb.errors import DBSyntaxError


def _get_parse_column_name(ast: Insert) -> tuple[str, ...]:
    schema = ast.find(Schema)
    if (
            schema is None
            or schema.expressions is None
            or len(schema.expressions) == 0
    ):
        raise DBSyntaxError(context="Schema cannot be None")

    try:
        return tuple([
            column.this
            for column in schema.expressions
        ])
    except AttributeError as ex:
        raise DBSyntaxError(context="Schema cannot be None") from ex

def _get_parse_value_insert(ast: Insert) -> list[list[Any]]:
    values_insert_ast = ast.find(Values)
    if (
            values_insert_ast is None
            or values_insert_ast.expressions is None
            or len(values_insert_ast.expressions) == 0
    ):
        raise DBSyntaxError(context="Values cannot be None")

    list_row_insert_ast = [
        tuple_value.expressions
        for tuple_value in values_insert_ast.expressions
        if tuple_value.expressions is not None
    ]
    if len(list_row_insert_ast) == 0:
        raise DBSyntaxError(context="Values cannot be None")

    values_insert_ast = [[] for _ in range(len(list_row_insert_ast[0]))]

    for tuple_value in list_row_insert_ast:
        if len(tuple_value) == 0:
            raise DBSyntaxError(context="Values cannot be None")

        for row_num, column in enumerate(tuple_value):
            if not isinstance(column, Array):
                values_insert_ast[row_num].append(column.this)
                continue

            if len(column.expressions) == 0:
                raise DBSyntaxError(context="Values cannot be None")

            data_array = [
                array_value.this
                for array_value in column.expressions
                if array_value.this
            ]

            if len(data_array) == 0:
                raise DBSyntaxError(context="Values cannot be None")

            values_insert_ast[row_num].append(
                data_array
            )


    return values_insert_ast



def parse_table_insert(ast: Insert) -> dict[str, Any]:
    collection_name = get_table_name(ast)
    name_column = _get_parse_column_name(ast)
    value_column = _get_parse_value_insert(ast)
    return {
        "collection_name": collection_name,
        "name_column": name_column,
        "value_column": value_column,
    }
