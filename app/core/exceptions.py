class AppException(Exception):
    """Base exception class untuk aplikasi."""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class BadRequestException(AppException):
    def __init__(self, message: str = "Bad Request"):
        super().__init__(message=message, status_code=400)

class NotFoundException(AppException):
    def __init__(self, message: str = "Resource Not Found"):
        super().__init__(message=message, status_code=404)

class ForbiddenException(AppException):
    def __init__(self, message: str = "Access Forbidden"):
        super().__init__(message=message, status_code=403)