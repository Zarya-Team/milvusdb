from typing import Any, TypeVar

from sqlglot import Dialect, Expression, parse_one
from sqlglot.expressions import Command, Create, Delete, Drop, Insert, Select

from milvusdb.converter.const import CreateKind
from milvusdb.converter.dialect import MilvusDialect
from milvusdb.converter.parse import parse_index_create, parse_table_create
from milvusdb.converter.parse.create.type import CollectionSchemaDict
from milvusdb.converter.parse.insert import parse_table_insert
from milvusdb.converter.validation import is_transform_supported
from milvusdb.errors import NotSupportedError

AST_LIMIT = TypeVar("AST_LIMIT", Select, Delete, Drop, Create, Insert, Command)


class MilvusTransform:
    dialect: type[Dialect]

    def __init__(self) -> None:
        self.dialect = MilvusDialect

    def parameter_request(self, sql_string: str) -> dict[str, Any]:
        ast_transform: Expression = parse_one(sql_string, dialect=self.dialect)

        is_transform = is_transform_supported(ast_transform)

        if not is_transform.is_valid:
            raise NotSupportedError(context=is_transform.message)

        return self._transform(ast_transform)

    def _transform(self, ast: AST_LIMIT) -> dict[str, Any]:
        match ast:
            case ast if isinstance(ast, Delete):
                return self._parse_delete(ast)
            case ast if isinstance(ast, Drop):
                return self._parse_drop(ast)
            case ast if isinstance(ast, Create):
                return self._parse_create(ast)
            case ast if isinstance(ast, Insert):
                return parse_table_insert(ast)
            case _:
                return self._parse_select(ast)

    def _parse_create(self, ast: Create) -> CollectionSchemaDict:
        match ast.kind:
            case CreateKind.TABLE.value:
                return parse_table_create(ast)
            case CreateKind.INDEX.value:
                return parse_index_create(ast)
            case _:
                raise NotSupportedError(
                    context=f"Unknown create kind: {ast.kind}"
                )

    def _parse_delete(self, _: Delete) -> dict[str, Any]:
        return {}

    def _parse_select(self, _: Select) -> dict[str, Any]:
        return {}

    def _parse_drop(self, _: Drop) -> dict[str, Any]:
        return {}
