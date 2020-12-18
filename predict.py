import pandas as pd
import numpy as np
from keras.engine.saving import model_from_json
from get_data import get_data, input_vars, output_var
import os
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Read data and download from AEMET
data = get_data("data/COPEDICATClinicSympt_DATA_2020-12-17_1642.csv")
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
for i in [x * 0.001 for x in range(0, 1000)]:
    frame = pd.DataFrame()
    func = np.vectorize(lambda x: x > i)
    prediction2 = func(prediction)
    frame.insert(0, "covid-real", data["covid"])
    frame.insert(0, "covid-pred2", prediction2)

    mismatch = len(frame.loc[frame["covid-pred2"] > frame["covid-real"]])
    l.append(mismatch)
    mismatch2 = len(frame.loc[frame["covid-pred2"] < frame["covid-real"]])
    l2.append(mismatch2)

    # pd.set_option('display.max_rows', 2000)
    # print(input_data)

print(np.argmin(l)/1000)
print(min(l))
print(np.argmin(l2)/1000)
print(min(l2))
plt.plot(l)
plt.plot(l2)
plt.show()

print("All done")
