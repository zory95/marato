"""
This file is part of aguathon.

aguathon is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

aguathon is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with aguathon.  If not,
see <https://www.gnu.org/licenses/>.
"""
import os
from shutil import copyfile
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from keras.layers import Dense, GRU
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from get_data import get_data,input_vars,output_var

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

data = get_data("data/COPEDICATClinicSympt_DATA_2020-12-17_1642.csv")

best_models = {}
best_losses = {}

# Split train set and validation set
data_train, data_valid = train_test_split(data, test_size=0.2, shuffle=False)
data_test, data_valid = train_test_split(data_valid, test_size=0.5, shuffle=False)

input_train = data_train[input_vars]
input_valid = data_valid[input_vars]
input_test = data_test[input_vars]

topologies = [[40, 30, 20]]
# for layers in range(2, 5):
#     topologies.extend([p for p in itertools.product([20, 30, 40], repeat=layers) if
#                        all([p[i] >= p[i + 1] for i in range(len(p) - 1)])])

best_loss = 7
print("Creating model...")

model_name = "models/model.json"
h5_name_aux = "models/modelaux.h5"
h5_name = "models/model.h5"

output_train = data_train[output_var]
output_valid = data_valid[output_var]
output_test = data_test[output_var]

for topology in topologies:
    print("Trying topology " + str(topology))
    # Build model
    model = Sequential()
    for i, neurons in enumerate(topology):
        if i == 0:
            model.add(Dense(units=neurons, input_dim=len(input_vars)))
        else:
            model.add(Dense(units=neurons))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='mean_squared_error', optimizer='adam')

    earlyStopping = EarlyStopping(monitor='val_loss', patience=10,
                                  verbose=0, mode='min')
    mcp_save = ModelCheckpoint(h5_name_aux, save_best_only=True,
                               monitor='val_loss', mode='min', verbose=0)
    reduce_lr_loss = ReduceLROnPlateau(monitor='val_loss',
                                       factor=0.1, patience=1, verbose=0,
                                       min_delta=0.05, mode='min')

    # Train model
    model.fit(input_train, output_train, epochs=1000, batch_size=1, shuffle=False,
              validation_data=(input_valid, output_valid), verbose=0,
              callbacks=[earlyStopping, mcp_save, reduce_lr_loss])

    test_loss = model.evaluate(input_test, output_test, verbose=0)
    print()
    print("Mean square error of test set:")
    print(test_loss)
    if test_loss < best_loss:
        print("Model improved with topology " + str(topology))
        model_json = model.to_json()
        with open(model_name, "w") as json_file:
            json_file.write(model_json)
        copyfile(h5_name_aux, h5_name)
        best_loss = test_loss

        best_models[output_var] = str(topology)
        best_losses[output_var] = str(test_loss)
    else:
        print("Model did NOT improve with topology " + str(topology))
    print()

os.remove(h5_name_aux)
print("Done with " + output_var)
print()

print("All done.")
print("Best topologies:")
print(best_models)
print("Best losses:")
print(best_losses)
