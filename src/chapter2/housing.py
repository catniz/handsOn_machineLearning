import os
import pandas as pd

HOUSING_PATH = os.path.join("..", "datasets", "housing")


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


pd.options.display.max_columns = None
pd.options.display.width = None

housing = load_housing_data()
print(housing.head())

print("....")
