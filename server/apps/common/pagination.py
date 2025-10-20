"""
Pagination module for the application.
"""

# Django Rest Framework imports
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    """
    Custom pagination class with adjustable page size.
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100
