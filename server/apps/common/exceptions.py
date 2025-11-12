from rest_framework.exceptions import APIException
from rest_framework import status

class NotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Entity not found."
    default_code = "not_found"

class BudgetAlreadyExists(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Data already exists for this user."
    default_code = "exists"