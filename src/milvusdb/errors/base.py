from typing import Any


class Error(Exception):
    def __init__(
        self,
        message: str = "Unknown database error",
        code: dict[str, Any] | None = None,
        context: str | None = None,
    ) -> None:
        self.message = message
        self.code = code
        self.context = context
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.message}: {self.context}"


class InterfaceError(Error):
    def __init__(
        self,
        message: str = "Interface error or connection failure",
        code: dict[str, Any] | None = None,
        context: str | None = None,
    ) -> None:
        super().__init__(message, code, context)


class DatabaseError(Error):
    def __init__(
        self,
        message: str = "General database error",
        code: dict[str, Any] | None = None,
        context: str | None = None,
    ) -> None:
        super().__init__(message, code, context)
