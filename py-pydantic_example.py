from os import path
import pydantic
import json
from typing import Optional, List


path = r"C:\Users\pauld\Nextcloud\Documents\Scripts\Gitlab\test-project\py-pydantic_example.json"


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10 doesn't have the right format."""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbd_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

    @pydantic.validator("isbn_10", check_fields=False)
    @classmethod
    def isbn_10_valid(cls, value) -> None:
        """Validator to check whether ISBN10 is valid"""
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        if sum((10 - i) * char_to_int(x) for i, x in enumerate(chars)) % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11."
            )
        return value


def main() -> None:
    with open(path, "r") as f:
        data = json.load(f)
        books: List[Book] = [Book(**item) for item in data]
        print(books[0].title)


if __name__ == "__main__":
    main()
