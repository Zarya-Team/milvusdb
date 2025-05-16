from enum import Enum

from pymilvus import DataType as TypePyMilvus
from sqlglot.expressions import DataType

TypeSqlGlot = DataType.Type
mapping_type = {
    TypeSqlGlot.INT: TypePyMilvus.INT32,
    TypeSqlGlot.BIGINT: TypePyMilvus.INT64,
    TypeSqlGlot.VARCHAR: TypePyMilvus.VARCHAR,
    TypeSqlGlot.ARRAY: TypePyMilvus.FLOAT_VECTOR,
}


class DialectKey(Enum):
    CREATE = "create"
    INSERT = "insert"
    SELECT = "select"
    DELETE = "delete"
    DROP = "drop"


class CreateKind(Enum):
    TABLE = "TABLE"
    INDEX = "INDEX"
