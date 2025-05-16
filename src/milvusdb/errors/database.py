from typing import Any

from milvusdb.errors.base import DatabaseError


class DataError(DatabaseError):
    def __init__(
        self,
        message: str = "Invalid data encountered",
        code: dict[str, Any] | None = None,
        context: str | None = None,
    ) -> None:
        super().__init__(message, code, context)


class DBSyntaxError(DatabaseError):
    def __init__(
        self,
        message: str = "Invalid SQL or query syntax",
        code: dict[str, Any] | None = None,
        context: str | None = None,
    ) -> None:
        super().__init__(message, code, context)


class OperationalError(DatabaseError):
    def __init__(
        self,
        message: str = "Operational error (e.g., lost connection)",
        code: dict[str, Any] | None = None,
        context: str | None = None,
    ) -> None:
        super().__init__(message, code, context)


class IntegrityError(DatabaseError):
    def __init__(
        self,
        message: str = "Integrity constraint violation",
        code: dict[str, Any] | None = None,
        context: str | None = None,
    ) -> None:
        super().__init__(message, code, context)


class InternalError(DatabaseError):
    def __init__(
        self,
        message: str = "Internal database or driver error",
        code: dict[str, Any] | None = None,
        context: str | None = None,
    ) -> None:
        super().__init__(message, code, context)


class ProgrammingError(DatabaseError):
    def __init__(
        self,
        message: str = "Programming error (e.g., bad SQL syntax)",
        code: dict[str, Any] | None = None,
        context: str | None = None,
    ) -> None:
        super().__init__(message, code, context)


class NotSupportedError(DatabaseError):
    def __init__(
        self,
        message: str = "Operation not supported by the database",
        code: dict[str, Any] | None = None,
        context: str | None = None,
    ) -> None:
        super().__init__(message, code, context)
