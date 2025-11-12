from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response


class GlobalSuccessResponseMiddleware(MiddlewareMixin):
    """
    The middleware automatically wraps all DRF Response objects for successful requests
    in a consistent JSON structure.
    Return normal Response: return Response(serializer.data).
    Return DRF paginated response as usual: return paginator.get_paginated_response(serializer.data)
    """

    def process_response(self, request, response):
        # Only wrap DRF Response objects
        if isinstance(response, Response):
            # Do not wrap if already wrapped
            if getattr(response, "_is_wrapped", False):
                return response

            # Only wrap success responses (status code < 400)
            if response.status_code < 400:
                wrapped_data = {
                    "success": True,
                    "data": response.data,
                }

                # Include pagination keys if they exist
                if isinstance(response.data, dict):
                    if "count" in response.data:
                        wrapped_data["count"] = response.data.get("count")
                    if "next" in response.data:
                        wrapped_data["next"] = response.data.get("next")
                    if "previous" in response.data:
                        wrapped_data["previous"] = response.data.get("previous")

                response.data = wrapped_data
                response._is_wrapped = True

        return response
