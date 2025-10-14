"""Custom pagination class for DRF."""

from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    """Custom pagination class."""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
