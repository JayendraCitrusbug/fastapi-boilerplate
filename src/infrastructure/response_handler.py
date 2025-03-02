from typing import Any, Optional

from fastapi import status
from fastapi.responses import JSONResponse

from src.infrastructure.exception_handler import BaseHTTPException


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
                "status_code": status_code,
                "message": message,
                "data": data,
            },
        )

    @staticmethod
    def error(
        exception: Exception,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        message: str = "Something went wrong",
    ) -> JSONResponse:
        """
        Standardized error response.
        """

        if isinstance(exception, BaseHTTPException):
            raise exception

        print(
            "******************************************************************** EXCEPTION STARTED ********************************************************************"
        )
        print(f"Exception: {str(exception)}")
        print(
            f"File path: {exception.__traceback__.tb_frame.f_code.co_filename}: {exception.__traceback__.tb_lineno}"
        )
        print(
            "******************************************************************** EXCEPTION ENDED ********************************************************************"
        )

        raise BaseHTTPException(status_code=status_code, message=message)
