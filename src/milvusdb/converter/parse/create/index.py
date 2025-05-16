from typing import Any

from sqlglot.expressions import Anonymous, Create, Identifier, Ordered

from milvusdb.errors import NotSupportedError


def get_field_index(ast: Create) -> dict[str, Any]:
    orders = list(ast.find_all(Ordered))
    if len(orders) != 1:
        raise NotSupportedError(context="Many columns are not supported")

    order = orders[0]
    column_index = order.find(Anonymous)
    if column_index is None or column_index.this is None:
        raise NotSupportedError(context="Column is not supported")

    column = order.find(Identifier)
    if column is None or column.this is None:
        raise NotSupportedError(context="Column is not supported")

    return {
        "column_index": column_index.this,
        "column_name": column.this,
    }

