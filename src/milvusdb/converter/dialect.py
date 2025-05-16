from typing import ClassVar

from sqlglot import exp
from sqlglot.dialects.dialect import Dialect
from sqlglot.generator import Generator
from sqlglot.tokens import Tokenizer, TokenType


class MilvusDialect(Dialect):
    class Tokenizer(Tokenizer):
        QUOTES: ClassVar[list[str]] = ["'", '"']
        IDENTIFIERS: ClassVar[list[str]] = ["`"]
        KEYWORDS: ClassVar[dict[str, TokenType]] = {
            **Tokenizer.KEYWORDS,
            "FLOAT64": TokenType.DOUBLE,
        }

    class Generator(Generator):
        TRANSFORMS: ClassVar[dict[type, callable]] = {
            exp.Array: lambda self, expre: f"[{self.expressions(expre)}]",
        }
        TYPE_MAPPING: ClassVar[dict[type, str]] = {
            exp.DataType.Type.TINYINT: "INT64",
            exp.DataType.Type.SMALLINT: "INT64",
            exp.DataType.Type.INT: "INT64",
            exp.DataType.Type.BIGINT: "INT64",
            exp.DataType.Type.DECIMAL: "NUMERIC",
            exp.DataType.Type.FLOAT: "FLOAT64",
            exp.DataType.Type.DOUBLE: "FLOAT64",
            exp.DataType.Type.BOOLEAN: "BOOL",
            exp.DataType.Type.TEXT: "STRING",
        }
