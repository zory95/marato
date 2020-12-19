import pandas as pd

output_var = "final_diagnosis_code"
file = "../data/covid-cleaned.csv"

model_name = "models/model.json"
h5_name = "models/model.h5"

train_file = "../data/train.csv"
test_file = "../data/test.csv"
val_file = "../data/val.csv"


def get_data(file):
    data = pd.read_csv(file).ffill().fillna(-1)
    input_vars = list(data)
    input_vars.remove(output_var)
    return input_vars, output_var, data


def split(data, index):
    return data[0:index], data[index:]


def split_data(file):
    data = pd.read_csv(file).ffill().fillna(-1)
    positivos = data[data[output_var] == 1]
    negativos = data[data[output_var] == 0]

    pos_train, pos_test = split(positivos, 120)
    # pos_val, pos_test  = split(pos_test, len(pos_test) // 2)
    pos_val, pos_test  = split(pos_test, 30)
    neg_train, neg_test = split(negativos, 120)
    # neg_val, neg_test  = split(neg_test, len(neg_test) // 2)
    neg_val, neg_test  = split(neg_test, 30)

    train = pos_train.append(neg_train, ignore_index=True)
    test = pos_test.append(neg_test, ignore_index=True)
    val = pos_val.append(neg_val, ignore_index=True)

    train.to_csv(train_file, index=False)
    test.to_csv(test_file, index=False)
    val.to_csv(val_file, index=False)


if __name__ == "__main__":
    split_data(file)
