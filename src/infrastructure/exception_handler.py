import json

from fastapi import status
from starlette.exceptions import HTTPException as StarletteHTTPException


class BaseHTTPException(StarletteHTTPException):
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
            detail=json.dumps(
                {
                    "success": False,
                    "status_code": status_code,
                    "message": message,
                    "data": None,
                }
            ),
        )
