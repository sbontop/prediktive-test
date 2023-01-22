import json

from src.util.constants import DATA_LOADER_MAPPING
from src.util.exceptions import (InvalidDataTypeException,
                                 InvalidYearException,
                                 QuantityNotFoundException)


class DataLoader:
    def __init__(self, id: str) -> None:
        self.id = id
        self.metadata = DATA_LOADER_MAPPING[self.id]

    def get_path(self) -> str:
        """Get the path of the data"""
        return self.metadata["path"]

    def get_schema(self) -> dict:
        """Get the schema of the data"""
        return self.metadata["schema"]

    def get_class(self) -> type:
        """Get the class of the data"""
        return self.metadata["class"]

    def load(self) -> list:
        """Load data from path"""
        try:
            path: str = self.get_path()
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File {path} not found") from e


class Calculator:
    def __init__(self, data: dict) -> None:
        self.data = data

    def _validate(self, model_id: str, year: str) -> None:
        if not isinstance(model_id, str):
            raise InvalidDataTypeException("model_id", model_id)
        if not isinstance(year, str):
            raise InvalidDataTypeException("year", year)
        if len(year) != 4 or int(year) < 0:
            raise InvalidYearException(year)
        if model_id not in self.data.keys():
            raise QuantityNotFoundException("model_id", model_id)
        if year not in self.data[model_id]["schedule"]["years"].keys():
            raise QuantityNotFoundException("year", year)

    def calculate(self, model_id: str, year: str) -> dict[str, float]:
        self._validate(model_id, year)
        cost: float = self.data[model_id]["saleDetails"]["cost"]
        return {
            "market_value": round(
                self.data[model_id]["schedule"]["years"][year]["marketRatio"] * cost, 2
            ),
            "auction_value": round(
                self.data[model_id]["schedule"]["years"][year]["auctionRatio"] * cost, 2
            ),
        }
