from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware


class UUIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        """
        A middleware that assigns a unique UUID to each request and logs the request and response.

        This middleware assigns a unique UUID to each request and stores it in the request state.
        It also logs the request method and URL, as well as the status code of the response.

        :param request: The incoming request
        :param call_next: The next middleware in the chain
        :return: The response to the request
        """

        request_id = str(uuid4())
        request.state.request_id = request_id
        print(f"Request - {request_id}: {request.method} {request.url}")
        response = await call_next(request)
        print(f"Response - {request_id}: status code {response.status_code}")
        return response
