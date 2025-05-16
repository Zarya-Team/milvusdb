from .connection import Connection

apilevel = "2.0"
threadsafety = 1
paramstyle = "format"

def connect(
    user: str,
    host: str | None ="localhost",
    database: str | None = None,
    port: int | None = 5432,
    password: str | None = None,
    timeout: int | None = None,
    ssl_context: bool = False,
    token: str | None = None,
):
    return Connection(
        user=user,
        uri=host,
        database=database,
        port=port,
        password=password,
        timeout=timeout,
        ssl_context=ssl_context,
        token= token,
    )

__all__ = ["connect"]
