from fastapi import HTTPException, status


class BaseException(HTTPException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code=status_code, detail=message)


class NotFoundException(BaseException):
    def __init__(self, message: str = "Not Found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, message=message)


class InsertionException(BaseException):
    def __init__(self, message: str = "Error when entering data"):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=message
        )
