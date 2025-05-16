from pymilvus import MilvusClient

from .cursor import Cursor
from .errors import DatabaseError


class Connection:
    def __init__(
            self,
            user: str,
            uri: str | None = "localhost",
            database: str | None = None,
            port: int | None = 5432,
            password: str | None = None,
            timeout: int | None = None,
            ssl_context: bool = False,
            token: str | None = None,
    ) -> None:
        self.client = MilvusClient(
            user=user,
            uri=uri,
            database=database,
            port=port,
            password=password,
            timeout=timeout,
            token=token,
        )
        self.closed = False
        self._committed = True

    def __check_valid(self) -> None:
        pass

    def cursor(self) -> Cursor:
        if self.closed:
            raise DatabaseError(context="Connection is closed")
        return Cursor(self)

    def commit(self) -> None:
        if self.closed:
            raise DatabaseError(context="Connection is closed")
        self._committed = True

    def rollback(self) -> None:
        if self.closed:
            raise DatabaseError(context="Connection is closed")
        self._committed = False

    def close(self) -> None:
        self.closed = True
