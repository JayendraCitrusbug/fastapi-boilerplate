from dataclasses import dataclass

from fastapi import HTTPException, status


@dataclass(frozen=True)
class BaseHTTPException(HTTPException):
    """
    Custom exception class to handle HTTP errors in a structured way.
    """

    def __init__(
        self,
        message: str = "Bad Request",
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ):
        super().__init__(
            status_code=status_code,
            detail={
                "success": False,
                "message": message,
            },
        )
