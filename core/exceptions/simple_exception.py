class SimpleException(Exception):
    def __init__(self, message: str, status_code: int = 501):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return self.message


# class SimpleException(Exception):
#     def __init__(
#         self,
#         status_code: int,
#         message: str,
#         err_type: SimpleExceptionType = SimpleExceptionType.NOT_SPECIFIED,
#     ) -> None:
#         super().__init__()
#         self.status_code = status_code
#         self.message = message
#         self.err_type = err_type
