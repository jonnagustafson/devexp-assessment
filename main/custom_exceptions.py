class CustomError(Exception):
    """Base exception for SDK errors."""
    pass


class ClientError(CustomError):
    """Exception for 4xx client errors."""
    def __init__(self, status_code, message, response):
        super().__init__(f"Client error {status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.response = response


class ServerError(CustomError):
    """Exception for 5xx server errors."""
    def __init__(self, status_code, message, response):
        super().__init__(f"Server error {status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.response = response
