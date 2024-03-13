
class DataBaseException(Exception):
    """
    Exception to catch database errors
    """

    def __init__(self, message: str | None = None) -> None:
        self.message = message

        super().__init__(self.message)