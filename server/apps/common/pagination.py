"""
Pagination module for the application.
"""

# Django Rest Framework imports
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class StandardResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class with default page size.
    Can also read `?page_size=` from query params.
    """

    # Default settings
    page_size = 10               # Default items per page
    page_query_param = "page"    # Query param for page number
    page_size_query_param = "page_size"  # Allow clients to set page size dynamically
    max_page_size = 100          # Prevent abuse by setting an upper limit

    def get_paginated_response(self, data):
        """
        Custom paginated response structure.
        """
        return Response({
            "success": True,
            "count": self.page.paginator.count,
            "total_pages": self.page.paginator.num_pages,
            "current_page": self.page.number,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data
        })
