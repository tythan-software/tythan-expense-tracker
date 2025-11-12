"""
Pagination module for the application.
"""

# Django Rest Framework imports
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class with default page size.
    Can also read `?page_size=` from query params.
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100
