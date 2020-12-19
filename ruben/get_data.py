import pandas as pd

output_var = "final_diagnosis_code"
file = "../data/covid-cleaned.csv"

model_name = "models/model.json"
h5_name = "models/model.h5"


def get_data(file):
    data = pd.read_csv(file).ffill().fillna(-1)
    input_vars = list(data)
    input_vars.remove(output_var)
    return input_vars, output_var, data


if __name__ == "__main__":
    data = get_data(file)
