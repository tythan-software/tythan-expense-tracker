from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, ParseError, APIException


def custom_exception_handler(exc, context):
    """
    Global DRF exception handler for consistent error formatting.
    """
    # First, let DRF handle known exceptions (it sets the default response)
    response = exception_handler(exc, context)

    if response is not None:
        # Handle known DRF exceptions (ValidationError, ParseError, etc.)
        if isinstance(exc, ValidationError):
            error_detail = exc.detail if isinstance(exc.detail, (list, dict)) else {"message": str(exc.detail)}
            return Response(
                {"success": False, "error": error_detail},
                status=status.HTTP_400_BAD_REQUEST
            )

        elif isinstance(exc, ParseError):
            return Response(
                {"success": False, "error": str(exc.detail)},
                status=status.HTTP_400_BAD_REQUEST
            )

        elif isinstance(exc, APIException):
            return Response(
                {"success": False, "error": str(exc.detail)},
                status=response.status_code
            )

        else:
            # Fallback for other handled DRF exceptions
            return Response(
                {"success": False, "error": response.data},
                status=response.status_code
            )

    # Handle any unhandled server errors (e.g. RuntimeError, ValueError)
    return Response(
        {
            "success": False,
            "error": "Unexpected error occurred",
            "details": str(exc)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
