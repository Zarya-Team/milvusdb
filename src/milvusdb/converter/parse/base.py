from sqlglot.expressions import Create, Identifier, Insert, Table

from milvusdb.errors import DBSyntaxError


def get_table_name(query: Create | Insert) -> str:
    table = query.find(Table)
    if table is None:
        raise DBSyntaxError(context="Query does not contain the table name")

    table_name = table.find(Identifier)

    if table_name is None:
        raise DBSyntaxError(context="Table has no table name")

    if table_name.this is None:
        raise DBSyntaxError(context="Table has no table name")

    return table_name.this
