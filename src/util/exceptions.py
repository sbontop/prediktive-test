from src.util.constants import (EQUIPMENT_QUANTITY_MAPPING,
                                QUANTITY_TYPE_MAPPING)


class QuantityNotFoundException(Exception):
    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value

    def __str__(self):
        return repr(f"{EQUIPMENT_QUANTITY_MAPPING[self.key]}: {self.value} Not Found")


class InvalidYearException(Exception):
    def __init__(self, year: str):
        self.year = year

    def __str__(self):
        return repr(f"Invalid Year: {self.year}. Should be a 4 digits positive integer")


class InvalidDataTypeException(Exception):
    def __init__(self, key: str, value):
        self.key = key
        self.value = value

    def __str__(self):
        return repr(
            f"Invalid {self.key}: {self.value}. Should be {QUANTITY_TYPE_MAPPING[self.key]}"
        )
