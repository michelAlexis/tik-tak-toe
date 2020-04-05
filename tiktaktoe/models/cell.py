class Cell:
    EMPTY = 'E'

    def __init__(self, value = EMPTY):
        self.value = value

    def __eq__(self, other):
        return other is not None and self.value == other.value

    def __str__(self) -> str:
        return str(self.value)