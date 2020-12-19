import os
import itertools
from shutil import copyfile
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from get_data import *

h5_name_aux = "models/modelaux.h5"

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# input_vars, output_var, data = get_data(file)
#
# # Split train set and validation set
# data_train, data_valid = train_test_split(data, test_size=0.1, shuffle=False)
# data_test, data_valid = train_test_split(data_valid, test_size=0.5, shuffle=False)

input_vars, output_var, data_train = get_data(train_file)
input_vars, output_var, data_valid = get_data(val_file)
input_vars, output_var, data_test = get_data(test_file)

best_models = {}
best_losses = {}

input_train = data_train[input_vars]
input_valid = data_valid[input_vars]
input_test = data_test[input_vars]

topologies = []
for layers in range(2, 4):
    topologies.extend([p for p in itertools.product([5, 10, 20, 30], repeat=layers) if
                       all([p[i] >= p[i + 1] for i in range(len(p) - 1)])])

best_loss = 7
print("Creating model...")

output_train = data_train[output_var]
output_valid = data_valid[output_var]
output_test = data_test[output_var]

for topology in topologies:
    print("Trying topology " + str(topology))
    # Build model
    model = Sequential()
    activation = 'softplus'
    for i, neurons in enumerate(topology):
        if i == 0:
            model.add(Dense(units=neurons, input_dim=len(input_vars), activation=activation))
        else:
            model.add(Dense(units=neurons, activation=activation))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    earlyStopping = EarlyStopping(monitor='val_loss', mode='min',
                                  patience=3, verbose=0)
    mcp_save = ModelCheckpoint(h5_name_aux, monitor='val_loss', mode='min',
                               save_best_only=True, verbose=0)
    reduce_lr_loss = ReduceLROnPlateau(monitor='val_loss', mode='min',
                                       factor=0.1, min_delta=0.05, patience=1,
                                       verbose=0)

    # Train model
    model.fit(input_train, output_train, epochs=1000, batch_size=1, shuffle=True,
              validation_data=(input_valid, output_valid), verbose=0,
              callbacks=[earlyStopping, mcp_save, reduce_lr_loss])

    test_loss, test_acc = model.evaluate(input_test, output_test, verbose=0)
    print(f'Test results - Loss: {test_loss} - Accuracy: {test_acc*100}%')
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
