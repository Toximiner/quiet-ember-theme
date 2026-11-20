# QUIET EMBER — a fictional recipe example
# Sand types · cyan parameters · slate-blue attributes
from dataclasses import dataclass
from enum import Enum

class Portion(Enum):
    SMALL = "small"
    LARGE = "large"

@dataclass
class Ingredient:
    """A fictional ingredient used only to demonstrate syntax colors."""
    name: str
    grams: float
    organic: bool = False

    @property
    def label(self) -> str:
        # Purple self; slate-blue attributes after the dot
        return f"{self.name}: {self.grams:.1f} g"

    def scaled(self, factor: float = 1.0) -> "Ingredient":
        if factor <= 0:
            raise ValueError("The scale must be positive")
        return Ingredient(
            name=self.name,
            grams=self.grams * factor,
            organic=self.organic,
        )


def make_recipe(portion: Portion, servings: int = 2) -> list[Ingredient]:
    ingredients = [
        Ingredient(name="Oats", grams=80.0, organic=True),
        Ingredient(name="Berries", grams=120.0),
    ]
    multiplier = 1.5 if portion is Portion.LARGE else 1.0
    return [item.scaled(factor=multiplier * servings) for item in ingredients]


class RecipeBook:
    def __init__(self, title: str) -> None:
        self.title = title
        self.pages: list[str] = []

book = RecipeBook(title="Weekend cooking")  # Class and keyword argument
recipe = make_recipe(portion=Portion.SMALL, servings=2)
book.pages.append("Berry bowl")
message = f"{book.title}: {len(recipe):02d} ingredients"
# Strings, numbers, booleans, defaults and type annotations
options = {"temperature": 180, "timer": 12.5, "covered": False}
