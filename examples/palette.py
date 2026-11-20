# Fictional library example — syntax palette comparison
from dataclasses import dataclass
from enum import Enum

class Status(Enum):
    READY = "ready"
    RESERVED = "reserved"

@dataclass
class Book:
    """A library book with a title and availability status."""
    title: str
    copies: int = 3
    available: bool = True

    def label(self, prefix: str = "Book") -> str:
        return f"{prefix}: {self.title} ({self.copies})"

    def reserve(self, reader: str, days: int = 7) -> dict[str, str | int]:
        if not self.available:
            raise ValueError("This book is unavailable")
        self.available = False
        return {"reader": reader, "days": days}


def make_report(book: Book, limit: int = 5) -> list[str]:
    labels = [book.label(prefix="Featured") for _ in range(limit)]
    return labels

book = Book(title="Ocean Stories", copies=12, available=True)
reservation = book.reserve(reader="Alex", days=14)
report = make_report(book=book, limit=2)
status = Status.RESERVED
ratio = 1.25
message = f"{book.title}: {len(report):02d} labels"
