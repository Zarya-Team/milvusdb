from sqlglot.expressions import (
    ColumnDef,
    DataType,
    GeneratedAsIdentityColumnConstraint,
    Identifier,
    Literal,
    PrimaryKeyColumnConstraint,
)

from milvusdb.converter.const import (
    TypePyMilvus,
    TypeSqlGlot,
    mapping_type,
)
from milvusdb.errors import DBSyntaxError


def get_type_column(column: ColumnDef) -> TypePyMilvus:
    column_type: DataType | None = column.find(DataType)
    if column_type is None:
        raise DBSyntaxError(context="Column has no type")

    return convert_type(column_type.this)


def convert_type(sql_glot_type: TypeSqlGlot) -> TypePyMilvus:
    return mapping_type[sql_glot_type]


def is_primary_key(column: ColumnDef) -> bool:
    return column.find(PrimaryKeyColumnConstraint) is not None


def get_name_column(column: ColumnDef) -> str:
    name: Identifier | None = column.find(Identifier)
    if name is None:
        raise DBSyntaxError(context="No find name column")

    return name.this


def is_auto_increment(column: ColumnDef) -> bool:
    is_auto = column.find(GeneratedAsIdentityColumnConstraint)
    if is_auto is None:
        return False

    return is_auto.this


def get_length(column: ColumnDef) -> dict[str, int]:
    length: Literal | None = column.find(Literal)
    if length is None:
        return {}

    column_type: DataType | None = column.find(DataType)
    if column_type is None:
        raise DBSyntaxError(context="Column has no type")

    length_number: int = int(length.this)
    if length_number < 0:
        raise DBSyntaxError(context="Column length not valid")

    match column_type.this:
        case TypeSqlGlot.VARCHAR:
            return {"max_length": length_number}

        case TypeSqlGlot.ARRAY:
            return {"dim": length_number}

        case _:
            raise DBSyntaxError(context="Column type not supported")
