from sqlglot.expressions import (
    Create,
    Delete,
    Drop,
    Expression,
    Insert,
    Select,
)

from milvusdb.converter.const import CreateKind, DialectKey
from milvusdb.converter.type import IsValid

ALLOWED_AST = (Select, Delete, Drop, Create, Insert)


def is_transform_supported(ast: Expression) -> IsValid:
    if not isinstance(ast, ALLOWED_AST) or ast.key not in DialectKey:
        return IsValid(is_valid=False, message="Unsupported SQL statement")

    if isinstance(ast, Create) and ast.kind not in CreateKind:
        return IsValid(is_valid=False, message="Unsupported CREATE statement")

    return IsValid(is_valid=True, message="Supported method")
