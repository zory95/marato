import os

import matplotlib.pyplot as plt
import numpy as np
from keras.engine.saving import model_from_json

from get_data import *

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

input_vars, output_var, data = get_data(file)
input_data = data[input_vars]

print("Making predictions")

model_name = "models/model.json"
h5_name = "models/model.h5"

# Load model
json_file = open(model_name, 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(h5_name)

# Make prediction
prediction = loaded_model.predict(input_data)
print("Done predicting ")

l = []
l2 = []
for i in [x * 0.01 for x in range(0, 100)]:
    frame = pd.DataFrame()
    func = np.vectorize(lambda x: x > i)
    prediction2 = func(prediction)
    frame.insert(0, "covid-real", data[output_var])
    frame.insert(0, "covid-pred2", prediction2)

    mismatch = len(frame.loc[frame["covid-pred2"] > frame["covid-real"]])
    l.append(mismatch)
    mismatch2 = len(frame.loc[frame["covid-pred2"] < frame["covid-real"]])
    l2.append(mismatch2)

    # pd.set_option('display.max_rows', 2000)
    # print(frame)

plt.plot(l, label="Falso positivo")
plt.plot(l2, label="Falso negativo")
plt.legend()
plt.show()

print("All done")