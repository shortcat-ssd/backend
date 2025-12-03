from rest_framework.exceptions import APIException


class NotFound(APIException):
    status_code = 404
    default_detail = "The requested resource was not found."
    default_code = "not_found"
