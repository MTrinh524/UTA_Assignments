# Name: Minh Trinh
# UTA_ID: 1001705984
# Date Modified:
# Description:

import numpy as np

def nn_train_and_test(tr_data, tr_labels, test_data, test_labels, labels_to_ints, ints_to_labels, parameters):

    maxTuple_tr_data = np.unravel_index(np.absolute(tr_data).argmax(), tr_data.shape) # gets the tuple that stores the max value of 'tr_data'
    maxValue_tr_data = tr_data[maxTuple_tr_data[0]][maxTuple_tr_data[1]] # gets the ACTUAL max value of 'tr_data'

    maxTuple_test_data = np.unravel_index(np.absolute(test_data).argmax(), test_data.shape) # gets the tuple that stores the max value of 'test_data'
    maxValue_test_data = test_data[maxTuple_test_data[0]][maxTuple_test_data[1]] # gets the ACTUAL max value of 'test_data'

    # Normalizes the values in all dimensions of 'tr_data'
    for row in range(tr_data.shape[0]):
        for col in range(tr_data.shape[1]):
            tr_data[row][col] /= maxValue_tr_data

    # Normalizes the values in all dimensions of 'test_data'
    for row in range(test_data.shape[0]):
        for col in range(test_data.shape[1]):
            test_data[row][col] /= maxValue_test_data

    len_unique_tr_labels = len(np.unique(tr_labels))
    ohv = np.eye(len_unique_tr_labels)[tr_labels].reshape(len(tr_labels), -1)
    parameters.units_per_layer.append(len_unique_tr_labels)
    # print(parameters.units_per_layer)
    weight = [None]*(parameters.num_layers - 1)
    bias = [None]*(parameters.num_layers - 1)
    # print(weight)

    for layer in range(parameters.num_layers-1):

        weight[layer] = np.random.uniform(-0.05, 0.05, (parameters.units_per_layer[layer], tr_data.shape[1]))
        bias[layer] = np.random.uniform(-0.05, 0.05, parameters.units_per_layer[layer])
    # print("weights\n", weight)
    # print("baises\n", bias)
    z = 
    print(z[0, 0])
    round = 1
    eta = 1

    while round <= parameters.training_rounds:

        for layer in range(parameters.num_layers-1):

            for p in range(parameters.units_per_layer[layer]):

                for n in range(tr_data.shape[0]):
                    if layer == 0:
                        dotProd = np.dot(weight[layer, p], tr_data[n]) + bias[layer, p]
                        z[p, n] = 1/(1 + np.exp(-dotProd))

                        dEdb = (z[p, n] - ohv[n, p]) * (1 - z[p, n]) * z[p, n]
                        bias[layer, p] = bias[layer, p] - eta * dEdb

                        for d in range(tr_data.shape[1]):
                            dEdw = (z[p, n] - ohv[n, p]) * (1 - z[p, n]) * z[p, n] * tr_data[n][d]
                            weight[layer, p, d] = weight[layer, p, d] - eta * dEdw

                    else:
                        dotProd = np.dot(weight[layer, p], z[p-1, n]) + bias[layer, p]
                        z[p, n] = 1/(1 + np.exp(-dotProd))
                        
                        dEdb = (z[p, n] - ohv[n, p]) * (1 - z[p, n]) * z[p, n]
                        bias[layer, p] = bias[layer, p] - eta * dEdb

                        for d in range(tr_data.shape[1]):
                            dEdw = (z[p, n] - ohv[n, p]) * (1 - z[p, n]) * z[p, n] * tr_data[n][d]
                            weight[layer, p, d] = weight[layer, p, d] - eta * dEdw


        eta = eta * 0.98
        round += 1

    len_unique_test_labels = len(np.unique(test_labels))
    accCount = 0

    for layer in range(parameters.num_layers-1):
        for n in range(test_data.shape[0]):
            for p in range


        

