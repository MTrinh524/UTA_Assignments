# Name: Minh Trinh
# UTA_ID: 1001705984
# Date Modified: 
#   2/18/2023 - Normalized the inputs training and test data
#   2/19/2023 - Implemented the whole training portion for a single perceptron
#   2/20/2023 - Implemented testing to see if predicted and true classes matches up
#               and checks the accuracy given the test values
# Description:
#   Trains a single perceptron using some specified training set,
#   and will then evaluate the accuracy of the perceptron on some
#   specified test set.

import numpy as np

def perceptron_train_and_test(tr_data, tr_labels, test_data, test_labels, training_rounds):

    maxTuple_tr_data = np.unravel_index(np.absolute(tr_data).argmax(), tr_data.shape) # gets the tuple that stores the max value of 'tr_data'
    maxValue_tr_data = tr_data[maxTuple_tr_data[0]][maxTuple_tr_data[1]] # gets the ACTUAL max value of 'tr_data'

    maxTuple_test_data = np.unravel_index(np.absolute(test_data).argmax(), test_data.shape) # gets the tuple that stores the max value of 'test_data'
    maxValue_test_data = test_data[maxTuple_test_data[0]][maxTuple_test_data[1]] # gets the ACTUAL max value of 'test_data'

    # TESTING
    # print('tr_data.shape', tr_data.shape)
    # print('maxTuple_tr_data', maxTuple_tr_data)
    # print('maxValue_tr_data', maxValue_tr_data)
    # print('test_data.shape', test_data.shape)
    # print('maxTuple_test_data', maxTuple_test_data)
    # print('maxValue_test_data', maxValue_test_data)

    # Normalizes the values in all dimensions of 'tr_data'
    for row in range(tr_data.shape[0]):
        for col in range(tr_data.shape[1]):
            tr_data[row][col] /= maxValue_tr_data

    # Normalizes the values in all dimensions of 'test_data'
    for row in range(test_data.shape[0]):
        for col in range(test_data.shape[1]):
            test_data[row][col] /= maxValue_test_data

    # print("Norm tr_data\n", tr_data) # TESTING normalization of 'tr_data'
    # print("Norm test_data\n", test_data) # TESTING normalization of 'test_data'

    # Gets random bias and each weight_d values following uniform distribution between -0.05 and 0.05
    weight = np.random.uniform(-0.05, 0.05, tr_data.shape[1])
    bias = np.random.uniform(-0.05, 0.05)
    eta = 1
    round = 1

    # Training of the perceptron
    while round <= training_rounds:
        for n in range(tr_data.shape[0]):
            dotProd = np.dot(weight, tr_data[n]) + bias # Computes the dot product of weights and inputs for a unit
            z = 1/(1 + np.exp(-dotProd)) # Computes sigmoid function given 'dotProd'
            # loss = (1/2) * pow((tr_labels[n] - z), 2) # Computes the loss function (squared differences)

            dEdb = (z - tr_labels[n]) * (1 - z) * z # Partial derivative of loss function over bias
            bias = bias - eta * dEdb # Update bias

            for d in range(tr_data.shape[1]):
                dEdw = (z - tr_labels[n]) * (1 - z) * z * tr_data[n][d] # Partial derivative of loss function of weight
                weight[d] = weight[d] - eta * dEdw # Update weights

        eta = eta * 0.98 # Change the learning rate for next round
        round += 1 # Updates to the next training round

    # TESTING
    # print("Updated weights", weight)
    # print("Update bias", bias)

    accCount = 0 # Keeps count of how many classes are accurate

    for n in range(test_data.shape[0]):
        # Performs the sigmoid function on the test data and get corresponding outputs
        dotProd = np.dot(weight, test_data[n]) + bias
        z = 1/(1 + np.exp(-dotProd))
        
        object_id = n
        true_class = test_labels[n, 0]
        # Gets the predicted_class depending on the outputs
        if z < 0.5:
            predicted_class = 0
        elif z >= 0.5:
            predicted_class = 1

        # Gets the accuracy and increments the amount of accurate classes
        if predicted_class == true_class:
            accuracy = 1
        else:
            accuracy = 0

        accCount += accuracy
        print('ID=%5d, predicted=%10s, true=%10s, accuracy=%4.2f\n' % (object_id, str(predicted_class), str(true_class), accuracy))

    # The overall average accuracy of the classifcation accuracy
    print(accCount, test_data.shape[0])
    classification_accuracy = accCount/test_data.shape[0]
    print('classification accuracy=%6.4f\n' % (classification_accuracy))


