# Name: Minh Trinh
# UTA_ID: 1001705984
# Date Modified:
# Description:

import numpy as np

def nn_2l_train_and_test(tr_data, tr_labels, test_data, test_labels, labels_to_ints, ints_to_labels, training_rounds):
   
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

    # print("Norm tr_data\n", tr_data) # TESTING normalization of 'tr_data'
    # print("Norm test_data\n", test_data) # TESTING normalization of 'test_data'

    len_unique_tr_labels = len(np.unique(tr_labels))
    #print(len_unique_tr_labels)
    ohv = np.eye(len_unique_tr_labels)[tr_labels].reshape(len(tr_labels), -1)
    #print(ohv[:, 0])

    # Gets random bias and each weight_d values following uniform distribution between -0.05 and 0.05
    weight = np.random.uniform(-0.05, 0.05, (len_unique_tr_labels, tr_data.shape[1]))
    bias = np.random.uniform(-0.05, 0.05, len_unique_tr_labels)
    # print("weight", weight)
    # print("bias", bias)
    eta = 1
    round = 1

    while round <= training_rounds:
        for p in range(len_unique_tr_labels):
            for n in range(tr_data.shape[0]):
                dotProd = np.dot(weight[p], tr_data[n]) + bias[p]
                z = 1/(1 + np.exp(-dotProd))

                dEdb = (z - ohv[n, p]) * (1 - z) * z
                bias[p] = bias[p] - eta * dEdb

                for d in range(tr_data.shape[1]):
                    dEdw = (z - ohv[n, p]) * (1 - z) * z * tr_data[n][d]
                    weight[p, d] = weight[p, d] - eta * dEdw

        eta = eta * 0.98
        round += 1

    len_unique_test_labels = len(np.unique(test_labels))
    z = np.zeros((len_unique_test_labels))
    accCount = 0
    tie = False

    for n in range(test_data.shape[0]):
        for p in range(len_unique_test_labels):
            dotProd = np.dot(weight[p], test_data[n]) + bias[p]
            z[p] = 1/(1 + np.exp(-dotProd))

        # print(z)
        max_class = np.where(z == z.max())
        # print(max_class)

        if len(max_class) > 1:
            tie = True
        
        object_id = n
        true_class = ints_to_labels[test_labels[n, 0]]
        predicted_class = ints_to_labels[max_class[0][0]]

        if tie == False and predicted_class == true_class:
            accuracy = 1
        elif tie == False and predicted_class != true_class:
            accuracy = 0
        elif tie == True and labels_to_ints[true_class] in max_class[:]:
            accuracy = 1/len(max_class)
        elif tie == True and labels_to_ints[true_class] not in max_class[:]:
            accuracy = 0

        accCount += accuracy
        print('ID=%5d, predicted=%10s, true=%10s, accuracy=%4.2f\n' % (object_id, str(predicted_class), str(true_class), accuracy))

    classification_accuracy = accCount/test_data.shape[0]
    print('classification accuracy=%6.4f\n' % (classification_accuracy))
