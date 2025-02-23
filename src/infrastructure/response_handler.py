from typing import Any, Optional

from fastapi import status
from fastapi.responses import JSONResponse


class ResponseHandler:
    """
    Custom response handler for consistent API responses.
    """

    @staticmethod
    def success(
        status_code: int = status.HTTP_200_OK,
        message: str = "Success",
        data: Optional[Any] = None,
    ) -> JSONResponse:
        """
        Standardized success response.
        """
        return JSONResponse(
            status_code=status_code,
            content={
                "success": True,
                "message": message,
                "data": data,
            },
        )

    @staticmethod
    def error(
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        message: str = "Something went wrong",
        path: str = "",
    ) -> JSONResponse:
        """
        Standardized error response.
        """
        return JSONResponse(
            status_code=status_code,
            content={
                "success": False,
                "message": message,
            },
        )
