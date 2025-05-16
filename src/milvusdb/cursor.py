from collections.abc import Iterator
from typing import Any

from milvusdb.converter.transform import MilvusTransform
from milvusdb.errors import ProgrammingError



class Cursor:
    def __init__(self, connection) -> None:
        self.connection = connection
        self._results = []
        self._index = 0
        self.description = [("column1", str, None, None, None, None, None)]

    def execute(self, query: str) -> None:
        get_dict_query_params = MilvusTransform().parameter_request(query)
        self._results = [("result1",), ("result2",)]
        self._index = 0

    def fetchone(self) -> list[Any] | None:
        if self._index >= len(self._results):
            return None
        row = self._results[self._index]
        self._index += 1
        return row

    def fetchall(self) -> list[Any]:
        return self._results[self._index:]

    def close(self) -> None:
        self._results = []

    @property
    def rowcount(self) -> int:
        return len(self._results)

    def __iter__(self) -> Iterator:
        return iter(self._results)
