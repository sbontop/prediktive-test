from src.util.util import Calculator, DataLoader

data_loader: DataLoader = DataLoader("equipment")
data: dict = data_loader.load()
c: Calculator = Calculator(data)

# model_id, year = "67352", "2006" # Model ID Found, Year Found
# values: dict[str, float] = c.calculate(model_id, year)
# print(f"Values: {values}")

# model_id, year = "67352", "1" # Model ID Found, Year Not Found
# values: dict[str, float] = c.calculate(model_id, year)
# print(f"Values: {values}")

# model_id, year = "1", "2006" # Model ID Not Found, Year Found
# values: dict[str, float] = c.calculate(model_id, year)
# print(f"Values: {values}")

# model_id, year = "67352", "1" # Model ID Found, Invalid Year should fail
# values: dict[str, float] = c.calculate(model_id, year)
# print(f"Values: {values}")

# model_id, year = "67352", 1 # Model ID Found, Year Not Valid
# values: dict[str, float] = c.calculate(model_id, year)
# print(f"Values: {values}")

# model_id, year = 67352, "1"  # Model ID Found, Model ID Not Valid
# values: dict[str, float] = c.calculate(model_id, year)
# print(f"Values: {values}")

model_id, year = "67352", "2007"
values: dict[str, float] = c.calculate(model_id, year)
print(f"Values: {values}")

model_id, year = "87964", "2011"
values: dict[str, float] = c.calculate(model_id, year)
print(f"Values: {values}")
